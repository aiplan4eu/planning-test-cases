import pytest

from planning_tests.classical_planning.operation_modes.oneshot.util import run_oneshot_planner_on_solvable_problem
from planning_tests.classical_planning.problems.problem_metric import UPCostMetricWithConstantCosts
from planning_tests.classical_planning.problems.problem_metric import UPLengthMetric

class TestMetric:
    @pytest.mark.all
    @pytest.mark.simple 
    def test_plan_cost(self, oneshot_planner_name):
        problem = UPCostMetricWithConstantCosts(expected_version=1)
        up_problem = problem.get_problem()
        optimal_cost = 4
        run_oneshot_planner_on_solvable_problem(oneshot_planner_name, up_problem, optimal_cost)

    @pytest.mark.all
    @pytest.mark.simple 
    def test_plan_length(self, oneshot_planner_name):
        problem = UPLengthMetric(expected_version=1)
        up_problem = problem.get_problem()
        optimal_cost = 1
        run_oneshot_planner_on_solvable_problem(oneshot_planner_name, up_problem, optimal_cost)
