import pytest

from planning_tests.classical_planning.problems.problem_basic import UPBasic
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


@pytest.fixture()
def is_simple(request):
    return "simple" in  (m.name for m in request.node.own_markers)

@pytest.fixture(scope="class")
def result_cache():
    class ResultCache:
        def __init__(self):
            self._results = dict()

        def result(self, grounder_name, problem):
            if (grounder_name, problem) not in self._results:
                up_problem = problem.get_problem()
                with Compiler(name=oneshot_planner_name) as grounder:
                    assert(grounder.supports_compilation(CompilationKind.GROUNDING)
                    res = grouinder.compile(up_problem, CompilationKind.GROUNDING)
                    self._results[(grounder_name, problem)] = res
            return self._results[(grounder_name, problem)]

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
class TestGrounding:

    def test_plan_transfers(self, grounder_name, problem_name, problem,
            result_cache, is_simple):
        up_problem = problem.get_problem()
        grounder = Compiler(name=grounder_name)
        if not grounder.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(grounder_name))
        result = result_cache.result(grounder_name, problem)
        map_back = result.map_back_action_instance
        ground_problem = result.problem

        # solve ground_problem with arbitrary planner


        up_problem = problem.get_problem()

        planner = OneshotPlanner(name=oneshot_planner_name)
        if not planner.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(oneshot_planner_name))
        if not is_simple and planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
            pytest.skip("skip optimal planner on non-simple task")
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

    def test_map_back_action_instance_is_complete(self, grounder_name,
            problem_name, problem, result_cache):
        up_problem = problem.get_problem()
        grounder = Compiler(name=grounder_name)
        if not grounder.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(grounder_name))
        result = result_cache.result(grounder_name, problem)
        map_back = result.map_back_action_instance
        ground_problem = result.problem
        for a in ground_problem.actions:
            assert a in map_back_action_instance


    def test_result_is_grounded(self, grounder_name, problem_name,
            problem, result_cache):
        up_problem = problem.get_problem()
        grounder = Compiler(name=grounder_name)
        if not grounder.supports(up_problem.kind):
            pytest.skip("Grounder {} does not support problem kind".format(grounder_name))
        result = result_cache.result(grounder_name, problem)
       
        ground_problem = result.problem
        for a in ground_problem.actions:
            assert not a.parameters

        assert 'UNIVERSAL_CONDITIONS' not in ground_problem.kind.features
        assert 'EXISTENTIAL_CONDITIONS' not in ground_problem.kind.features

        
