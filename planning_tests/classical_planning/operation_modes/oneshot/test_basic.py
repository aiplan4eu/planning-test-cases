import pytest

from planning_tests.classical_planning.problems.problem_basic import UPBasic
from planning_tests.classical_planning.problems.problem_basic_unsolvable import UPBasicUnsolvable
from planning_tests.classical_planning.operation_modes.oneshot.util import run_oneshot_planner_on_solvable_problem

class TestBasic:
    @pytest.mark.all
    @pytest.mark.simple 
    def test_basic(self, oneshot_planner_name):
        problem = UPBasic(expected_version=1)
        optimal_cost = 1
        up_problem = problem.get_problem()
        run_oneshot_planner_on_solvable_problem(oneshot_planner_name, up_problem, optimal_cost)
