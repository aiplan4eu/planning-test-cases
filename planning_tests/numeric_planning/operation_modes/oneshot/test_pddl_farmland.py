import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.farmland.pddl_farmland import farmland_2_100_1229, farmland_2_200_1229, farmland_2_300_1229, farmland_8_400_1229,farmland_10_400_1229, farmland_10_1000_1229
from unified_planning.environment import get_env
from unittest import TestCase, main



class TestHandmadeFarmland(TestCase):

    def setUp(self):
        self.farmland_2_100_1229 = farmland_2_100_1229(expected_version=1)
        self.farmland_2_200_1229 = farmland_2_200_1229(expected_version=1)
        self.farmland_2_300_1229 = farmland_2_300_1229(expected_version=1)
        self.farmland_8_400_1229 = farmland_8_400_1229(expected_version=1)
        self.farmland_10_400_1229 = farmland_10_400_1229(expected_version=1)
        self.farmland_10_1000_1229 = farmland_10_1000_1229(expected_version=1)

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

    def test_farmland_2_100_1229(self):
        self.execute_one_shot_planning_test(self.farmland_2_100_1229.get_problem())

    def test_farmland_2_200_1229(self):
        self.execute_one_shot_planning_test(self.farmland_2_200_1229.get_problem())

    def test_farmland_2_300_1229(self):
        self.execute_one_shot_planning_test(self.farmland_2_300_1229.get_problem())

    def test_farmland_8_400_1229(self):
        self.execute_one_shot_planning_test(self.farmland_8_400_1229.get_problem())

    def test_farmland_10_400_1229(self):
        self.execute_one_shot_planning_test(self.farmland_10_400_1229.get_problem())

    def test_farmland_10_1000_1229(self):
        self.execute_one_shot_planning_test(self.farmland_10_1000_1229.get_problem())

if __name__ == '__main__':
    main()

