from unified_planning.shortcuts import *
from planning_tests.numeric_planning.problems.constant_additive_effects import UPConstantIncreaseEffects, UPConstantDecreaseEffects, extend_problem
from unittest import TestCase, main


class TestLinearEffects(TestCase):

    def setUp(self):
        self.problem_increase = UPConstantIncreaseEffects(expected_version=1)
        self.problem_decrease = UPConstantDecreaseEffects(expected_version=1)

    @staticmethod
    def execute_one_shot_planning_test(problem, expected_plan_length=None, planner_names=None):
        if planner_names is None:
            planner_names = [n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()]

        results = {}
        for p in planner_names:
            with OneshotPlanner(name=p) as planner:
                if planner.supports(problem.kind):
                    plan = planner.solve(problem)
                    with PlanValidator(problem_kind=problem.kind) as validator:
                        check = validator.validate(problem, plan.plan)
                        if expected_plan_length is not None:
                            check = check and len(plan.plan.actions) == expected_plan_length
                        results[p] = check
                        assert check

        print(f'Planners executed: {" ".join(results.keys())}')

    def test_increase_effect(self):
        self.execute_one_shot_planning_test(self.problem_increase.get_problem(), expected_plan_length=1)

    def test_decrease_effect(self):
        self.execute_one_shot_planning_test(self.problem_decrease.get_problem(), expected_plan_length=2)

    def test_increase_and_decrease_effects(self):
        problem = Problem('mixed_test')
        for extension in [self.problem_increase.problem_extension, self.problem_decrease.problem_extension]:
            extend_problem(problem, extension)
        self.execute_one_shot_planning_test(problem, expected_plan_length=3)


if __name__ == '__main__':
    main()


