# TODO test somewhere that presumably optimal planners declare themeselves such
import pytest

from planning_tests.classical_planning.problems.problem_basic import UPBasic
from planning_tests.classical_planning.problems.problem_basic_unsolvable import UPBasicUnsolvable
from planning_tests.classical_planning.problems.problem_metric import UPCostMetricWithConstantCosts
from planning_tests.classical_planning.problems.problem_metric import UPLengthMetric
from planning_tests.classical_planning.problems.problem_conditional_effects import UPConditionalEffects
from planning_tests.classical_planning.pddl_problems.depots.depots import depots_pfile1, depots_pfile2, depots_pfile3
from planning_tests.classical_planning.pddl_problems.tpp.tpp import tpp_pfile1, tpp_pfile2, tpp_pfile3, tpp_pfile6
from planning_tests.classical_planning.problems.problem_conditional_effects import UPConditionalEffects
from unified_planning.engines import OptimalityGuarantee, PlanGenerationResultStatus
from unified_planning.engines import ValidationResultStatus

from unified_planning.shortcuts import *

unified_planning.shortcuts.get_env().credits_stream = None # silence credits
    
@pytest.fixture(scope="class")
def result_cache():
    class ResultCache:
        def __init__(self):
            self._results = dict()

        def result(self, oneshot_planner_name, problem):
            if (oneshot_planner_name, problem) not in self._results:
                up_problem = problem.get_problem()
                with OneshotPlanner(name=oneshot_planner_name) as planner:
                    res = planner.solve(up_problem)
                    self._results[(oneshot_planner_name, problem)] = res
            return self._results[(oneshot_planner_name, problem)]

    return ResultCache()


basic = UPBasic(expected_version=1)
conditional_effects = UPConditionalEffects(expected_version=1)
cost_metric = UPCostMetricWithConstantCosts(expected_version=1)
length_metric = UPLengthMetric(expected_version=1)
conditional_effects = UPConditionalEffects(expected_version=1)
depots_pfile1 = depots_pfile1(expected_version=1)
depots_pfile2 = depots_pfile2(expected_version=1)
depots_pfile3 = depots_pfile3(expected_version=1)
tpp_pfile1 = tpp_pfile1(expected_version=1)
tpp_pfile2 = tpp_pfile2(expected_version=1)
tpp_pfile3 = tpp_pfile3(expected_version=1)
tpp_pfile6 = tpp_pfile6(expected_version=1)

@pytest.mark.all
@pytest.mark.solvable
@pytest.mark.parametrize("problem_name, problem, optimal_cost",
    [
        pytest.param('prob_basic', basic, 1, marks=pytest.mark.simple),
        pytest.param('prob_cond_effects', conditional_effects, 2, marks=pytest.mark.simple),
        pytest.param('prob_cost_metric', cost_metric, 4,
            marks=pytest.mark.simple),
        pytest.param('prob_length_metric', length_metric, 1,
            marks=pytest.mark.simple),
        pytest.param('prob_cond_effects', conditional_effects, 2,
            marks=pytest.mark.simple),
        pytest.param("depots_pfile1", depots_pfile1, 10,
            marks=[pytest.mark.simple, pytest.mark.depots]),
        pytest.param("depots_pfile2", depots_pfile2, 15,
            marks=[pytest.mark.simple, pytest.mark.depots]),
        pytest.param("depots_pfile3", depots_pfile3, 27,
            marks=[pytest.mark.medium, pytest.mark.depots]),
        pytest.param("tpp_pfile1", tpp_pfile1, 5,
            marks=[pytest.mark.simple, pytest.mark.TPP]),
        pytest.param("tpp_pfile2", tpp_pfile2, 8,
            marks=[pytest.mark.simple, pytest.mark.TPP]),
        pytest.param("tpp_pfile3", tpp_pfile3, 11,
            marks=[pytest.mark.simple, pytest.mark.TPP]),
        pytest.param("tpp_pfile6", tpp_pfile6, 25,
            marks=[pytest.mark.medium, pytest.mark.TPP]),
    ])
class TestSolvable:

    def test_plan_validates(self, oneshot_planner_name, problem_name, problem, optimal_cost, result_cache):
        up_problem = problem.get_problem()
        if not OneshotPlanner(name=oneshot_planner_name).supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(oneshot_planner_name))
        result = result_cache.result(oneshot_planner_name, problem)
        if not result.plan:
            pytest.skip("{} did not find a plan".format(oneshot_planner_name))
        # The plan validator does not support metrics, so we remove this part
        # from the instance
        # TODO remove workaraound once resolved in UP
        metrics = up_problem.quality_metrics
        validation_problem = up_problem
        if metrics:
            validation_problem = validation_problem.clone()
            validation_problem.clear_quality_metrics()
       
        with PlanValidator(problem_kind=validation_problem.kind) as validator:
            check = validator.validate(validation_problem, result.plan)
            assert check.status is ValidationResultStatus.VALID

    def test_optimal_quality(self, oneshot_planner_name, problem_name, problem,
                             optimal_cost, result_cache):
        up_problem = problem.get_problem()
        if not OneshotPlanner(name=oneshot_planner_name).supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(oneshot_planner_name))
        result = result_cache.result(oneshot_planner_name, problem)
        if result.status is not PlanGenerationResultStatus.SOLVED_OPTIMALLY:
            pytest.skip("{} does not claim solution to be optimal".format(oneshot_planner_name))
        if optimal_cost is not None:
            metrics = up_problem.quality_metrics
            if metrics:
                assert len(metrics) == 1 # this is not a test assertion
                # but asserts the scope of this test function

                # another assertion for the scope of this util
                # function; not testing the planner
                assert (isinstance(metrics[0], up.model.metrics.MinimizeActionCosts)  or
                        isinstance(metrics[0], up.model.metrics.MinimizeSequentialPlanLength))

                if isinstance(metrics[0], up.model.metrics.MinimizeActionCosts):
                    cost_function = metrics[0].costs
                    default = metrics[0].default
                    cost = sum(cost_function.get(a.action, default).constant_value()
                               for a in result.plan.actions)
                    assert cost == optimal_cost
            else:
                assert optimal_cost == len(result.plan.actions)

    def test_valid_result_status(self, oneshot_planner_name, problem_name, problem, optimal_cost, result_cache):
        up_problem = problem.get_problem()
        if not OneshotPlanner(name=oneshot_planner_name).supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(oneshot_planner_name))
        result = result_cache.result(oneshot_planner_name, problem)
        if result.plan:
            # if the planner guarantees optimality, this should be reflected in
            # the result status
            planner = get_env().factory.engine(oneshot_planner_name)
            if planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
                assert result.status is PlanGenerationResultStatus.SOLVED_OPTIMALLY
            else:
                assert result.status in (PlanGenerationResultStatus.SOLVED_OPTIMALLY,
                                         PlanGenerationResultStatus.SOLVED_SATISFICING)
        else:
            assert result.status != PlanGenerationResultStatus.INTERNAL_ERROR
            # We are only running the test on solvable instances
            assert result.status != PlanGenerationResultStatus.UNSOLVABLE_PROVEN
            assert result.status in (PlanGenerationResultStatus.TIMEOUT,
                                     PlanGenerationResultStatus.MEMOUT,
                                     PlanGenerationResultStatus.UNSUPPORTED_PROBLEM,
                                     PlanGenerationResultStatus.UNSOLVABLE_INCOMPLETELY)
