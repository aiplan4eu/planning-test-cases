import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.sailing.sailing import sailing_1_1_1229, sailing_1_2_1229, sailing_1_3_1229, sailing_3_3_1229, sailing_4_10_1229
from unified_planning.environment import get_env
import pytest
import sys


class TestSailing:


	sailing_1_1_1229 = sailing_1_1_1229(expected_version=1)
	sailing_1_2_1229 = sailing_1_2_1229(expected_version=1)
	sailing_1_3_1229 = sailing_1_3_1229(expected_version=1)
	sailing_3_3_1229 = sailing_3_3_1229(expected_version=1)
	sailing_4_10_1229 = sailing_4_10_1229(expected_version=1)
	  

	@staticmethod
	def execute_one_shot_planning_test(problem,planner_name):
	
		results = {}
		
		with OneshotPlanner(name=planner_name) as planner:
				if planner.supports(problem.kind):
					plan = planner.solve(problem)
					with PlanValidator(problem_kind=problem.kind) as validator:
						check = validator.validate(problem, plan.plan)
						results[planner_name] = check
						assert check

		print(f'Planners executed: {" ".join(results.keys())}')

	@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
	def test_sailing_1_1_1229(self,planner_name):
		self.execute_one_shot_planning_test(self.sailing_1_1_1229.get_problem(),planner_name)

	@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
	def test_sailing_1_2_1229(self,planner_name):
		self.execute_one_shot_planning_test(self.sailing_1_2_1229.get_problem(),planner_name)

	@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
	def test_sailing_1_3_1229(self,planner_name):
		self.execute_one_shot_planning_test(self.sailing_1_3_1229.get_problem(),planner_name)

	@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
	def test_sailing_3_3_1229(self,planner_name):
		self.execute_one_shot_planning_test(self.sailing_3_3_1229.get_problem(),planner_name)

	@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
	@pytest.mark.skipif((len(sys.argv)<2 or sys.argv[1] == '-s' or sys.argv[1] == '-simple'), reason ="currently running in simple mode")
	def test_sailing_4_10_1229(self,planner_name):
		self.execute_one_shot_planning_test(self.sailing_4_10_1229.get_problem(),planner_name)  
