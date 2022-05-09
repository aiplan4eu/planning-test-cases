import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.problems.simple_nonlinear_conditions import UPGreaterThanEqualityNonLinearConditions, UPLowerEqualNegativeNonLinearConditions
from unittest import TestCase, main


class TestSimpleNonLinearConditions(TestCase):

    def setUp(self):
        self.problem_gt_equality_nonlinear_conditions = UPGreaterThanEqualityNonLinearConditions(expected_version=1)
        self.problem_le_negative_nonlinear_conditions = UPLowerEqualNegativeNonLinearConditions(expected_version=1)

    @staticmethod
    def execute_one_shot_planning_test(problem):
        planner_names = ['enhsp']

        results = {}
        for p in planner_names:
            with OneshotPlanner(name=p) as planner:
                if planner.supports(problem.kind):
                    plan = planner.solve(problem)
                    with PlanValidator(name='sequential_plan_validator') as validator:
                        check = validator.validate(problem, plan.plan)
                        results[p] = check
                        assert check

        print(f'Planners executed: {" ".join(results.keys())}')

    def test_gt_equality_nonlinear_conditions(self):
        self.execute_one_shot_planning_test(self.problem_gt_equality_nonlinear_conditions.get_problem())

    def test_le_negative_nonlinear_conditions(self):
        self.execute_one_shot_planning_test(self.problem_le_negative_nonlinear_conditions.get_problem())


if __name__ == '__main__':
    main()
