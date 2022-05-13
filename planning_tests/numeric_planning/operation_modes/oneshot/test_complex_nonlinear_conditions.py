import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.up_problems.complex_nonlinear_conditions import UPNonLinearDisjunctiveConditions, UPNonLinearExistentialConditions, UPNonLinearUniversalConditions
from unified_planning.environment import get_env
from unittest import TestCase, main


class TestComplexNonLinearConditions(TestCase):

    def setUp(self):
        self.problem_nonlinear_disjunctive_conditions = UPNonLinearDisjunctiveConditions(expected_version=1)
        self.problem_nonlinear_existential_conditions = UPNonLinearExistentialConditions(expected_version=1)
        self.problem_nonlinear_universal_conditions = UPNonLinearUniversalConditions(expected_version=1)

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

    def test_disjunctive_conditions(self):
        self.execute_one_shot_planning_test(self.problem_nonlinear_disjunctive_conditions.get_problem())

    def test_existential_conditions(self):
        self.execute_one_shot_planning_test(self.problem_nonlinear_existential_conditions.get_problem())

    def test_universal_conditions(self):
        self.execute_one_shot_planning_test(self.problem_nonlinear_universal_conditions.get_problem())


if __name__ == '__main__':
    main()
