import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.block_grouping.handmade_block_grouping import blocksworld_5_5_2_1, blocksworld_5_5_2_2, blocksworld_5_5_2_3
from unified_planning.environment import get_env
from unittest import TestCase, main



class TestHandmadeBlockGrouping(TestCase):

    def setUp(self):
        self.blocksworld_5_5_2_1 = blocksworld_5_5_2_1(expected_version=1)
        self.blocksworld_5_5_2_2 = blocksworld_5_5_2_2(expected_version=1)
        self.blocksworld_5_5_2_3 = blocksworld_5_5_2_3(expected_version=1)

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

    def test_blocksworld_5_5_2_1(self):
        self.execute_one_shot_planning_test(self.blocksworld_5_5_2_1.get_problem())

    def test_blocksworld_5_5_2_2(self):
        self.execute_one_shot_planning_test(self.blocksworld_5_5_2_2.get_problem())

    def test_blocksworld_5_5_2_3(self):
        self.execute_one_shot_planning_test(self.blocksworld_5_5_2_3.get_problem())


if __name__ == '__main__':
    main()

