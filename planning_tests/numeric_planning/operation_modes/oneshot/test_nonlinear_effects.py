import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.problems.nonlinear_effects import UPNonLinearIncreaseEffects, UPNonLinearAssignEffects, UPNonLinearConditionalEffects
from unittest import TestCase, main


class TestNonLinearEffects(TestCase):

    def setUp(self):
        self.problem_nonlinear_increase_effects = UPNonLinearIncreaseEffects(expected_version=1)
        self.problem_nonlinear_assign_continuous_effects = UPNonLinearAssignEffects(expected_version=1)
        self.problem_nonlinear_assign_conditional_effects = UPNonLinearConditionalEffects(expected_version=1)

    @staticmethod
    def execute_one_shot_planning_test(problem):
        planner_names = ['enhsp']

        results = {}
        for p in planner_names:
            with OneshotPlanner(name=p) as planner:
                if planner.supports(problem.kind()):
                    plan = planner.solve(problem)
                    with PlanValidator(name='sequential_plan_validator') as validator:
                        check = validator.validate(problem, plan)
                        results[p] = check
                        assert check

        print(f'Planners executed: {" ".join(results.keys())}')

    def test_increase_effects(self):
        self.execute_one_shot_planning_test(self.problem_nonlinear_increase_effects.get_problem())

    def test_assign_continuous_effects(self):
        self.execute_one_shot_planning_test(self.problem_nonlinear_assign_continuous_effects.get_problem())

    def test_assign_conditional_effects(self):
        self.execute_one_shot_planning_test(self.problem_nonlinear_assign_conditional_effects.get_problem())


if __name__ == '__main__':
    main()


