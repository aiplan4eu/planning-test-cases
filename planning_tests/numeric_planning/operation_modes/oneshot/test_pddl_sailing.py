import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.sailing.pddl_sailing import sailing_1_1_1229, sailing_1_2_1229, sailing_1_3_1229, sailing_3_3_1229, sailing_4_10_1229
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names
import pytest
import sys


class TestPddlSailing:


	sailing_1_1_1229 = sailing_1_1_1229(expected_version=1)
	sailing_1_2_1229 = sailing_1_2_1229(expected_version=1)
	sailing_1_3_1229 = sailing_1_3_1229(expected_version=1)
	sailing_3_3_1229 = sailing_3_3_1229(expected_version=1)
	sailing_4_10_1229 = sailing_4_10_1229(expected_version=1)
	  
	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(sailing_1_1_1229.get_problem().kind)

 
	
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("sailing_1_1_1229",sailing_1_1_1229),
	("sailing_1_2_1229",sailing_1_2_1229),
	("sailing_1_3_1229",sailing_1_3_1229),
	("sailing_3_3_1229",sailing_3_3_1229)])
	def test_sailing(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),[problem_name +'.pddl'],planner_name)

	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("sailing_4_10_1229",sailing_4_10_1229)])
	@pytest.mark.skipif((len(sys.argv)<2 or sys.argv[1] == '-s' or sys.argv[1] == '-simple'),reason ="currently running in simple mode")
	def test_sailing_medium(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),[problem_name +'.pddl'],planner_name)

	

