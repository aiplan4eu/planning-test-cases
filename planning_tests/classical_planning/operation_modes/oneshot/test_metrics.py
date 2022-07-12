import unified_planning
from unified_planning.shortcuts import *
from unified_planning.engines import OptimalityGuarantee, PlanGenerationResultStatus

from unittest import TestCase, main
from planning_tests.classical_planning.problems.problem_metric import UPCostMetricWithConstantCosts
from planning_tests.classical_planning.problems.problem_metric import UPLengthMetric

from planning_tests.classical_planning.operation_modes.oneshot.util import run_all_oneshot_planners_on_solvable_problem

class TestPlanCost(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.problem = UPCostMetricWithConstantCosts(expected_version=1)
        self.optimal_cost = 4

    def test_basic(self):
        up_problem = self.problem.get_problem()
        run_all_oneshot_planners_on_solvable_problem(up_problem, self.optimal_cost)


class TestPlanLength(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.problem = UPLengthMetric(expected_version=1)
        self.optimal_cost = 1

    def test_basic(self):
        up_problem = self.problem.get_problem()
        run_all_oneshot_planners_on_solvable_problem(up_problem, self.optimal_cost)


if __name__ == "__main__":
    main()
