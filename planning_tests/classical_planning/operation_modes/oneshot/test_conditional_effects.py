from unittest import TestCase, main

from planning_tests.classical_planning.problems.problem_conditional_effects import UPConditionalEffects
from planning_tests.classical_planning.operation_modes.oneshot.util import run_all_oneshot_planners_on_solvable_problem

class TestConditionalEffects(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.problem = UPConditionalEffects(expected_version=1)
        self.optimal_cost = 2

    def test_basic(self):
        up_problem = self.problem.get_problem()
        run_all_oneshot_planners_on_solvable_problem(up_problem, self.optimal_cost)


if __name__ == "__main__":
    main()
