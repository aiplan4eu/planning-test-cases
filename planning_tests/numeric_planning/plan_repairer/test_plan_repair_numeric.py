# TODO test somewhere that presumably optimal planners declare themeselves such
import pytest

from planning_tests.numeric_planning import (
        rovers_pfile3,
        rovers_pfile3_bad_plan1
        )
from unified_planning.engines import (OptimalityGuarantee,
        PlanGenerationResultStatus, ValidationResultStatus)

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

        def result(self, repairer_planner_name, problem, bad_plan):
            if (repairer_planner_name, problem,bad_plan) not in self._results:
                up_problem = problem.get_problem()
                up_plan =  bad_plan.get_plan(up_problem)
                with PlanRepairer(name=repairer_planner_name) as planner:
                    res = planner.repair(up_problem, up_plan)
                    self._results[(repairer_planner_name, problem,bad_plan)] = res
            return self._results[(repairer_planner_name, problem, bad_plan)]

    return ResultCache()



rovers_pfile3 = rovers_pfile3(expected_version=1)
rovers_pfile3_bad_plan1 = rovers_pfile3_bad_plan1()



@pytest.mark.all
@pytest.mark.solvable
@pytest.mark.repairer
@pytest.mark.repairer_numeric
@pytest.mark.parametrize("problem_name, problem, optimal_cost, bad_plan",
    [
        
        pytest.param("rovers_pfile3", rovers_pfile3, 11, rovers_pfile3_bad_plan1, 
            marks=[pytest.mark.simple, pytest.mark.rovers]),
    
    ])
class TestSolvable:

    def test_plan_validates(self, repairer_planner_name, problem_name, problem,
            optimal_cost,bad_plan, result_cache, is_simple):
        up_problem = problem.get_problem()
        up_plan = bad_plan.get_plan(up_problem)
        planner = PlanRepairer(name=repairer_planner_name)
        if not planner.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(repairer_planner_name))
        if not is_simple and planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
            pytest.skip("skip optimal planner on non-simple task")
        result = result_cache.result(repairer_planner_name, problem, bad_plan)
        if not result.plan:
            pytest.skip("{} did not find a plan".format(repairer_planner_name))
        # The plan validator does not support metrics, so we remove this part
        # from the instance
        # TODO remove workaraound once resolved in UP
        metrics = up_problem.quality_metrics
        validation_problem = up_problem
        if metrics:
            validation_problem = validation_problem.clone()
            validation_problem.clear_quality_metrics()
       
        with PlanValidator(problem_kind=validation_problem.kind) as validator:
            badcheck = validator.validate(validation_problem, up_plan)
            check = validator.validate(validation_problem, result.plan)
            assert badcheck.status is ValidationResultStatus.INVALID
            assert check.status is ValidationResultStatus.VALID



    def test_valid_result_status(self, repairer_planner_name, problem_name,
            problem, optimal_cost,bad_plan, result_cache, is_simple):
        up_problem = problem.get_problem()
        planner = PlanRepairer(name=repairer_planner_name)
        if not planner.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(repairer_planner_name))
        if not is_simple and planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
            pytest.skip("skip optimal planner on non-simple task")
        result = result_cache.result(repairer_planner_name, problem,bad_plan)
        if result.plan:
            # if the planner guarantees optimality, this should be reflected in
            # the result status
            metrics = up_problem.quality_metrics
            if not metrics:
                assert result.status is PlanGenerationResultStatus.SOLVED_SATISFICING
            else:
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
