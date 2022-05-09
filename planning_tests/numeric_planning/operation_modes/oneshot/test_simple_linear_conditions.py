import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.problems.simple_linear_conditions import UPEqualityConditions, UPGreaterLowerConditions, UPNegativeConditions, UPGreaterThanConditions, UPLowerThanConditions
from unified_planning.environment import get_env
from unittest import TestCase, main


class TestSimpleLinearConditions(TestCase):

    def setUp(self):
        self.problem_equality = UPEqualityConditions(expected_version=1)
        self.problem_negative_conditions = UPNegativeConditions(expected_version=1)
        self.problem_grater_lower_conditions = UPGreaterLowerConditions(expected_version=1)
        self.problem_lower_than_conditions = UPGreaterThanConditions(expected_version=1)
        self.problem_grater_than_conditions = UPLowerThanConditions(expected_version=1)

    @staticmethod
    def execute_one_shot_planning_test(problem):
        planner_names = [n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()]

        results = {}
        for p in planner_names:
            with OneshotPlanner(name=p) as planner:
                if planner.supports(problem.kind):
                    plan = planner.solve(problem)
                    with PlanValidator(problem_kind=problem.kind) as validator:
                        check = validator.validate(problem, plan.plan)
                        results[p] = check
                        assert check

        print(f'Planners executed: {" ".join(results.keys())}')

    def test_equality(self):
        self.execute_one_shot_planning_test(self.problem_equality.get_problem())

    def test_negative_conditions(self):
        self.execute_one_shot_planning_test(self.problem_negative_conditions.get_problem())

    def test_greater_than_conditions(self):
        self.execute_one_shot_planning_test(self.problem_grater_lower_conditions.get_problem())

    def test_lower_than_conditions(self):
        self.execute_one_shot_planning_test(self.problem_grater_than_conditions.get_problem())

    def test_greater_lower_conditions(self):
        self.execute_one_shot_planning_test(self.problem_lower_than_conditions.get_problem())


if __name__ == '__main__':
    main()


