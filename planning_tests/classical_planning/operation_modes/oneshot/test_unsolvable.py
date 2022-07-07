import unified_planning as up
from unified_planning.shortcuts import *
from unified_planning.engines import OptimalityGuarantee, PlanGenerationResultStatus

from unittest import TestCase, main
from planning_tests.classical_planning.problems.problem_basic import UPBasic
from planning_tests.classical_planning.problems.problem_basic_unsolvable import UPBasicUnsolvable

from planning_tests.classical_planning.operation_modes.oneshot.util import run_all_oneshot_planners_on_unsolvable_problem

class TestUnsolvable(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.unsolvable_problem = UPBasicUnsolvable(expected_version=1)

    def _run_solver_and_check_result(self, planner, problem):
        up_problem = problem.get_problem()
        result = planner.solve(up_problem)
        if result.plan:
            assert result.status is PlanGenerationResultStatus.SOLVED_OPTIMALLY
            assert problem.optimal_cost() == len(result.plan.actions)
            with PlanValidator(problem_kind=up_problem.kind) as validator:
                check = validator.validate(up_problem, result.plan)
                self.assertTrue(check)
        else:
            assert result.status in (PlanGenerationResultStatus.UNSOLVABLE_PROVEN,
                                     PlanGenerationResultStatus.UNSOLVABLE_INCOMPLETELY)
            if result.status == PlanGenerationResultStatus.UNSOLVABLE_PROVEN:
                assert problem.optimal_cost() == -1
                # TODO need constant for unsolvability of task
                # instead of using -1


    def test_optimal_on_unsolvable(self):
        problem = self.unsolvable_problem
        up_problem = problem.get_problem()
        run_all_oneshot_planners_on_unsolvable_problem(up_problem)


if __name__ == "__main__":
    main()
