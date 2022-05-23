from attr import validate
import unified_planning
from unified_planning.shortcuts import *
from planning_tests.correct_output import correct
from planning_tests.numeric_planning.pddl_problems.block_grouping.pddl_block_grouping import block_grouping_5_5_2_1, block_grouping_5_5_2_2, block_grouping_5_5_2_3, block_grouping_11_10_2_2, block_grouping_20_25_6_2, block_grouping_20_25_6_3
from unified_planning.environment import get_env
from unittest import TestCase, main
import os

#path = '/home/valerik/Desktop/programmazione/planning/planning-test-cases/planning_tests/numeric_planning/pddl_problems/block_grouping/'

class TestPddlBlockGrouping(TestCase):

    

    def setUp(self):
        self.blocksworld_5_5_2_1 = block_grouping_5_5_2_1(expected_version=1)
        self.blocksworld_5_5_2_2 = block_grouping_5_5_2_2(expected_version=1)
        self.blocksworld_5_5_2_3 = block_grouping_5_5_2_3(expected_version=1)
        self.blocksworld_11_10_2_2 = block_grouping_11_10_2_2(expected_version=1)
        self.blocksworld_20_25_6_2 = block_grouping_20_25_6_2(expected_version=1)
        self.blocksworld_20_25_6_3 = block_grouping_20_25_6_3(expected_version=1)

    
 
    @staticmethod
    def execute_one_shot_planning_test(problem,name):
        planner_names = [n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()]

        results = {}
        for p in planner_names: 
            with OneshotPlanner(name=p) as planner:
                if planner.supports(problem.kind):
                    plan = planner.solve(problem)
                    #open(f"output","w").write('\n'.join([str(act) for act in plan.plan.actions]))
                    #correct("output")
                    #os.system("./validate -v  "+ path +"block_grouping_domain.pddl "+ path + name +" output")
                    with PlanValidator(problem_kind=problem.kind) as validator:
                        check = validator.validate(problem, plan.plan)
                        results[p] = check
                        assert check
                

        print(f'Planners executed: {" ".join(results.keys())}')

    

    def test_block_grouping_5_5_2_1(self):
        self.execute_one_shot_planning_test(self.blocksworld_5_5_2_1.get_problem(),'block_grouping_5_5_2_1.pddl')

    def test_block_grouping_5_5_2_2(self):
        self.execute_one_shot_planning_test(self.blocksworld_5_5_2_2.get_problem(),'block_grouping_5_5_2_2.pddl')

    def test_block_grouping_5_5_2_3(self):
        self.execute_one_shot_planning_test(self.blocksworld_5_5_2_3.get_problem(),'block_grouping_5_5_2_3.pddl')

    def test_block_grouping_11_10_2_2(self):
        self.execute_one_shot_planning_test(self.blocksworld_11_10_2_2.get_problem(),'block_grouping_11_10_2_2.pddl')

    def test_block_grouping_20_25_6_2(self):
        self.execute_one_shot_planning_test(self.blocksworld_20_25_6_2.get_problem(),'block_grouping_20_25_6_2.pddl')

    def test_block_grouping_20_25_6_3(self):
        self.execute_one_shot_planning_test(self.blocksworld_20_25_6_3.get_problem(),'block_grouping_20_25_6_3.pddl')


if __name__ == '__main__':
    main()

