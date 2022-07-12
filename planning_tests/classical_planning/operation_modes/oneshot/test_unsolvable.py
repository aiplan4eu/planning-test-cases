from unittest import TestCase, main

from planning_tests.classical_planning.problems.problem_basic_unsolvable import UPBasicUnsolvable
from planning_tests.classical_planning.operation_modes.oneshot.util import run_all_oneshot_planners_on_unsolvable_problem

class TestUnsolvable(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.unsolvable_problem = UPBasicUnsolvable(expected_version=1)

    def test_optimal_on_unsolvable(self):
        problem = self.unsolvable_problem
        up_problem = problem.get_problem()
        run_all_oneshot_planners_on_unsolvable_problem(up_problem)


if __name__ == "__main__":
    main()
