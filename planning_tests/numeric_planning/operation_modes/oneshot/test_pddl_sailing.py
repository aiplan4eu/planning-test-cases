import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.sailing.pddl_sailing import sailing_1_1_1229, sailing_1_2_1229, sailing_1_3_1229, sailing_3_3_1229, sailing_4_10_1229
from unified_planning.environment import get_env
from unittest import TestCase, main



class TestPddlSailing(TestCase):

    def setUp(self):
        self.sailing_1_1_1229 = sailing_1_1_1229(expected_version=1)
        self.sailing_1_2_1229 = sailing_1_2_1229(expected_version=1)
        self.sailing_1_3_1229 = sailing_1_3_1229(expected_version=1)
        self.sailing_3_3_1229 = sailing_3_3_1229(expected_version=1)
        self.sailing_4_10_1229 = sailing_4_10_1229(expected_version=1)
      

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

    def test_sailing_1_1_1229(self):
        self.execute_one_shot_planning_test(self.sailing_1_1_1229.get_problem())

    def test_sailing_1_2_1229(self):
        self.execute_one_shot_planning_test(self.sailing_1_2_1229.get_problem())


    def test_sailing_1_3_1229(self):
        self.execute_one_shot_planning_test(self.sailing_1_3_1229.get_problem())

    def test_sailing_3_3_1229(self):
        self.execute_one_shot_planning_test(self.sailing_3_3_1229.get_problem())

    def test_sailing_4_10_1229(self):
        self.execute_one_shot_planning_test(self.sailing_4_10_1229.get_problem())        

if __name__ == '__main__':
    main()
