import unified_planning as up
from unified_planning.shortcuts import *
from unified_planning.engines import OptimalityGuarantee, PlanGenerationResultStatus

from unittest import TestCase, main
from planning_tests.classical_planning.problems.problem_basic import UPBasic
from planning_tests.classical_planning.problems.problem_basic_unsolvable import UPBasicUnsolvable

class TestOptimal(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.solvable_problem = UPBasic(expected_version=1)
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

    def test_optimal_on_solvable(self):
        problem = self.solvable_problem
        up_problem = problem.get_problem()
        optimal = OptimalityGuarantee.SOLVED_OPTIMALLY
        planner_names = [n for n, s in get_env().factory.engines.items()
                        if s.is_oneshot_planner() and
                        s.satisfies(optimal)]

        print()
        for p in planner_names:
            with OneshotPlanner(name=p) as planner:
                if planner.supports(up_problem.kind):
                    print("Testing optimal planner", p, "on solvable task")
                    self._run_solver_and_check_result(planner, problem)

    def test_optimal_on_unsolvable(self):
        problem = self.unsolvable_problem
        up_problem = problem.get_problem()
        optimal = OptimalityGuarantee.SOLVED_OPTIMALLY
        planner_names = [n for n, s in get_env().factory.engines.items()
                        if s.is_oneshot_planner() and
                        s.satisfies(optimal)]
        up_problem = self.unsolvable_problem.get_problem()

        print()
        for p in planner_names:
            with OneshotPlanner(name=p) as planner:
                if planner.supports(up_problem.kind):
                    print("Testing optimal planner", p, "on unsolvable task")
                    self._run_solver_and_check_result(planner, problem)


if __name__ == "__main__":
    main()
