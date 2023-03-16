# TODO test somewhere that presumably optimal planners declare themeselves such
import pytest

from planning_tests.numeric_planning import (
        UPEqualityConditions,
        UPNegativeConditions,
        UPGreaterLowerConditions,
        UPGreaterThanConditions,
        UPLowerThanConditions,
        depots_pfile1,
        depots_pfile2,
        depots_pfile3,
        depots_pfile10,
        depots_pfile11,
        rovers_pfile2,
        rovers_pfile3,
        rovers_pfile4,
        rovers_pfile5,
        )
from unified_planning.engines import (OptimalityGuarantee,
        PlanGenerationResultStatus, ValidationResultStatus,AnytimeGuarantee)

from unified_planning.shortcuts import *

unified_planning.shortcuts.get_environment().credits_stream = None # silence credits


@pytest.fixture()
def is_simple(request):
    return "simple" in  (m.name for m in request.node.own_markers)

@pytest.fixture(scope="class")
def result_cache():
    class ResultCache:
        def __init__(self):
            self._results = dict()

        def result(self, anytime_planner_name, problem,timeout):
            if (anytime_planner_name, problem) not in self._results:
                up_problem = problem.get_problem()
                with AnytimePlanner(name=anytime_planner_name) as planner:
                    solutions = []
                    for p in planner.get_solutions(up_problem,timeout):
                        if p.plan is not None:
                            solutions.append(p)
                    self._results[(anytime_planner_name, problem)] = solutions
            return self._results[(anytime_planner_name, problem)]

    return ResultCache()


equality_conditions = UPEqualityConditions(expected_version=1)
negative_conditions = UPNegativeConditions(expected_version=1)
greater_lower_conditions = UPGreaterLowerConditions(expected_version=1)
lower_than_conditions = UPGreaterThanConditions(expected_version=1)
greater_than_conditions = UPLowerThanConditions(expected_version=1)
depots_pfile1 = depots_pfile1(expected_version=1)
depots_pfile2 = depots_pfile2(expected_version=1)
depots_pfile3 = depots_pfile3(expected_version=1)
depots_pfile10 = depots_pfile10(expected_version=1)
depots_pfile11 = depots_pfile11(expected_version=1)
rovers_pfile2 = rovers_pfile2(expected_version=1)
rovers_pfile3 = rovers_pfile3(expected_version=1)
rovers_pfile4 = rovers_pfile4(expected_version=1)
rovers_pfile5 = rovers_pfile5(expected_version=1)


@pytest.mark.all
@pytest.mark.solvable
@pytest.mark.anytime
@pytest.mark.anytime_numeric
@pytest.mark.parametrize("problem_name, problem, optimal_cost, timeout",
    [
        pytest.param('prob_eq_conditions', equality_conditions, None, 10,
            marks=[pytest.mark.simple,pytest.mark.simple_linear_conditions]),
        pytest.param('prob_neg_conditions', negative_conditions, None, 10,
            marks=[pytest.mark.simple,pytest.mark.simple_linear_conditions]), 
        pytest.param('prob_gt_lw_conditions', greater_lower_conditions, None, 10,
            marks=[pytest.mark.simple,pytest.mark.simple_linear_conditions]), 
        pytest.param('prob_lw_conditions', lower_than_conditions, None, 10,
            marks=[pytest.mark.simple,pytest.mark.simple_linear_conditions]), 
        pytest.param('prob_gt_conditions', greater_than_conditions, None, 10,
            marks=[pytest.mark.simple,pytest.mark.simple_linear_conditions]),   
        pytest.param("depots_pfile1", depots_pfile1, 10, 10,
            marks=[pytest.mark.simple, pytest.mark.depots]),
        pytest.param("depots_pfile2", depots_pfile2, 15, 10,
            marks=[pytest.mark.simple, pytest.mark.depots]),
        pytest.param("depots_pfile3", depots_pfile3, 27, 10,
            marks=[pytest.mark.simple, pytest.mark.depots]),
        pytest.param("depots_pfile10", depots_pfile10, None, 10,
            marks=[pytest.mark.medium, pytest.mark.depots]),
        pytest.param("depots_pfile11", depots_pfile11, None, 10,
            marks=[pytest.mark.medium, pytest.mark.depots]),
        pytest.param("rovers_pfile2", rovers_pfile2, 8, 10,
            marks=[pytest.mark.simple, pytest.mark.rovers]),
        pytest.param("rovers_pfile3", rovers_pfile3, 11, 10,
            marks=[pytest.mark.simple, pytest.mark.rovers]),
        pytest.param("rovers_pfile4", rovers_pfile4, 8, 10,
            marks=[pytest.mark.simple, pytest.mark.rovers]),
        pytest.param("rovers_pfile5", rovers_pfile2, None, 10,
            marks=[pytest.mark.medium, pytest.mark.rovers]),
    ])
class TestSolvable:

    def test_plan_validates(self, anytime_planner_name, problem_name, problem,
            optimal_cost,timeout, result_cache, is_simple):
        up_problem = problem.get_problem()
        planner = AnytimePlanner(name=anytime_planner_name)
        if not planner.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(anytime_planner_name))
        if not is_simple and planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
            pytest.skip("skip optimal planner on non-simple task")
        results = result_cache.result(anytime_planner_name, problem,timeout)
        if not results[0].plan:
            pytest.skip("{} did not find a plan".format(anytime_planner_name))
        # The plan validator does not support metrics, so we remove this part
        # from the instance
        # TODO remove workaraound once resolved in UP
        metrics = up_problem.quality_metrics
        validation_problem = up_problem
        if metrics:
            validation_problem = validation_problem.clone()
            validation_problem.clear_quality_metrics()

        total_solutions = len(results)
        if total_solutions > 1:
            total_solutions = total_solutions -1
        for i in range(1,total_solutions):
            result = results[i]
            with PlanValidator(problem_kind=validation_problem.kind) as validator:
                check = validator.validate(validation_problem, result.plan)
                assert check.status is ValidationResultStatus.VALID
    
    def test_anytime_guarantee(self, anytime_planner_name, problem_name, problem,
            optimal_cost,timeout, result_cache, is_simple):
        up_problem = problem.get_problem()
        planner = AnytimePlanner(name=anytime_planner_name)
        if not planner.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(anytime_planner_name))
        if not is_simple and planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
            pytest.skip("skip optimal planner on non-simple task")
        if not planner.ensures(AnytimeGuarantee.INCREASING_QUALITY):
             pytest.skip("{} does not support increasing quality".format(anytime_planner_name))
        results = result_cache.result(anytime_planner_name, problem,timeout)
        if not results[0].plan:
            pytest.skip("{} did not find a plan".format(anytime_planner_name))
        # The plan validator does not support metrics, so we remove this part
        # from the instance
        # TODO remove workaraound once resolved in UP
        metrics = up_problem.quality_metrics
        validation_problem = up_problem
        if metrics:
            validation_problem = validation_problem.clone()
            validation_problem.clear_quality_metrics()

        total_solutions = len(results)
        if total_solutions > 1:
            total_solutions = total_solutions -1
        for i in range(1,total_solutions):
            result = results[i]
            with PlanValidator(problem_kind=validation_problem.kind) as validator:
                check = validator.validate(validation_problem, result.plan)
                assert len(result.plan.actions) <= len(results[i-1].plan.actions)


    

    # def test_valid_result_status(self, anytime_planner_name, problem_name,
    #         problem, optimal_cost,timeout, result_cache, is_simple):
    #     up_problem = problem.get_problem()
    #     planner = AnytimePlanner(name=anytime_planner_name)
    #     if not planner.supports(up_problem.kind):
    #         pytest.skip("{} does not support problem kind".format(anytime_planner_name))
    #     if not is_simple and planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
    #         pytest.skip("skip optimal planner on non-simple task")
    #     if not planner.ensures(AnytimeGuarantee.INCREASING_QUALITY):
    #          pytest.skip("{} does not support increasing quality".format(anytime_planner_name))
    #     results = result_cache.result(anytime_planner_name, problem,timeout)
    #     result = results[-1]
        
    #     if result.plan:
    #         # if the planner guarantees optimality, this should be reflected in
    #         # the result status
    #         metrics = up_problem.quality_metrics
    #         if not metrics:
    #             assert result.status is PlanGenerationResultStatus.SOLVED_SATISFICING
    #         else:
    #             if planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
    #                 assert result.status is PlanGenerationResultStatus.SOLVED_OPTIMALLY
    #             else:
    #                 assert result.status in (PlanGenerationResultStatus.SOLVED_OPTIMALLY,
    #                                      PlanGenerationResultStatus.SOLVED_SATISFICING)
    #     else:
    #         assert result.status != PlanGenerationResultStatus.INTERNAL_ERROR
    #         # We are only running the test on solvable instances
    #         assert result.status != PlanGenerationResultStatus.UNSOLVABLE_PROVEN
    #         assert result.status in (PlanGenerationResultStatus.TIMEOUT,
    #                              PlanGenerationResultStatus.MEMOUT,
    #                              PlanGenerationResultStatus.UNSUPPORTED_PROBLEM,
    #                              PlanGenerationResultStatus.UNSOLVABLE_INCOMPLETELY)
