import pytest

from planning_tests.classical_planning.problems.problem_basic_unsolvable import UPBasicUnsolvable
from planning_tests.classical_planning.operation_modes.oneshot.util import run_oneshot_planner_on_unsolvable_problem

class TestUnsolvable:
    
    @pytest.mark.all
    @pytest.mark.simple 
    def test_unsolvable_problem(self, oneshot_planner_name):
        problem = UPBasicUnsolvable(expected_version=1)
        up_problem = problem.get_problem()
        run_oneshot_planner_on_unsolvable_problem(oneshot_planner_name, up_problem)
