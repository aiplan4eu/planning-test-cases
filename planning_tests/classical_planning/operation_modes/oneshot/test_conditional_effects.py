import pytest

from planning_tests.classical_planning.problems.problem_conditional_effects import UPConditionalEffects
from planning_tests.classical_planning.operation_modes.oneshot.util import run_oneshot_planner_on_solvable_problem

class TestConditionalEffects:
    @pytest.mark.all
    @pytest.mark.simple 
    def test_conditional_effect(self, oneshot_planner_name):
        problem = UPConditionalEffects(expected_version=1)
        optimal_cost = 2
        up_problem = problem.get_problem()
        run_oneshot_planner_on_solvable_problem(oneshot_planner_name, up_problem, optimal_cost)
