import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.block_grouping.block_grouping import block_grouping_5_5_2_1, block_grouping_5_5_2_2, block_grouping_5_5_2_3, block_grouping_20_25_6_3, block_grouping_20_25_6_2, block_grouping_11_10_2_2
from unified_planning.environment import get_env
# from planning_tests.correct_output import correct
import os
import pytest
import sys
#import pkg_resources

#path = '/home/valerik/Desktop/programmazione/planning/planning-test-cases/planning_tests/numeric_planning/pddl_problems/block_grouping/'
#path = pkg_resources.resource_filename(__name__,'planning-test-cases/planning_tests/numeric_planning/pddl_problems/block_grouping/')

class TestBlockGrouping:

	blocksworld_5_5_2_1 = block_grouping_5_5_2_1(expected_version=1)
	blocksworld_5_5_2_2 = block_grouping_5_5_2_2(expected_version=1)
	blocksworld_5_5_2_3 = block_grouping_5_5_2_3(expected_version=1)
	blocksworld_11_10_2_2 = block_grouping_11_10_2_2(expected_version=1)
	blocksworld_20_25_6_2 = block_grouping_20_25_6_2(expected_version=1)
	blocksworld_20_25_6_3 = block_grouping_20_25_6_3(expected_version=1)

	@staticmethod
	def execute_one_shot_planning_test(problem,name,planner_name):
		
		results = {}
		with OneshotPlanner(name=planner_name) as planner:
				if planner.supports(problem.kind):
					plan = planner.solve(problem)
					
					#if len(sys.argv) > 2 :
					#	if sys.argv[2] == '-v' or sys.argv[2] == '-verbose':
					#		open(f"output","w").write('\n'.join([str(act) for act in plan.plan.actions]))
					#		correct("output")
					#		os.system("./validate "+ path +"block_grouping_domain.pddl "+ path + name +" output")

					with PlanValidator(problem_kind=problem.kind) as validator:
						check = validator.validate(problem, plan.plan)
						results[planner_name] = check
						assert check == True

		print(f'Planners executed: {" ".join(results.keys())}')

	@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
	def test_block_grouping_5_5_2_1(self,planner_name):
		self.execute_one_shot_planning_test(self.blocksworld_5_5_2_1.get_problem(),'block_grouping_5_5_2_1.pddl',planner_name)

	@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
	def test_block_grouping_5_5_2_2(self,planner_name):
		self.execute_one_shot_planning_test(self.blocksworld_5_5_2_2.get_problem(),'block_grouping_5_5_2_2.pddl',planner_name)

	@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
	def test_block_grouping_5_5_2_3(self,planner_name):
		self.execute_one_shot_planning_test(self.blocksworld_5_5_2_3.get_problem(),'block_grouping_5_5_2_3.pddl',planner_name)

	@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
	def test_block_grouping_11_10_2_2(self,planner_name):
		self.execute_one_shot_planning_test(self.blocksworld_11_10_2_2.get_problem(),'block_grouping_11_10_2_2.pddl',planner_name)

	@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
	@pytest.mark.skipif((len(sys.argv)<2 or sys.argv[1] == '-s' or sys.argv[1] == '-simple'), reason ="currently running in simple mode")
	def test_block_grouping_20_25_6_2(self,planner_name):
		self.execute_one_shot_planning_test(self.blocksworld_20_25_6_2.get_problem(),'block_grouping_20_25_6_2.pddl',planner_name)
	
	@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
	@pytest.mark.skipif((len(sys.argv)<2 or sys.argv[1] == '-s' or sys.argv[1] == '-simple'),reason ="currently running in simple mode")
	def test_block_grouping_20_25_6_3(self,planner_name):
		self.execute_one_shot_planning_test(self.blocksworld_20_25_6_3.get_problem(),'block_grouping_20_25_6_3.pddl',planner_name)






