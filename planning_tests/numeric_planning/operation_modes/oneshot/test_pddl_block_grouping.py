import unified_planning
from unified_planning.shortcuts import *
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names
from planning_tests.numeric_planning.pddl_problems.block_grouping.pddl_block_grouping import block_grouping_5_5_2_1, block_grouping_5_5_2_2, block_grouping_5_5_2_3, block_grouping_11_10_2_2, block_grouping_20_25_6_2, block_grouping_20_25_6_3
from unified_planning.environment import get_env
import pytest
import sys


class TestPddlBlockGrouping:

	block_grouping_5_5_2_1 = block_grouping_5_5_2_1(expected_version=1)
	block_grouping_5_5_2_2 = block_grouping_5_5_2_2(expected_version=1)
	block_grouping_5_5_2_3 = block_grouping_5_5_2_3(expected_version=1)
	block_grouping_11_10_2_2 = block_grouping_11_10_2_2(expected_version=1)
	block_grouping_20_25_6_2 = block_grouping_20_25_6_2(expected_version=1)
	block_grouping_20_25_6_3 = block_grouping_20_25_6_3(expected_version=1)

	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(block_grouping_5_5_2_1.get_problem().kind)

 
	@pytest.mark.block
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("block_grouping_5_5_2_1",block_grouping_5_5_2_1 ),
	("block_grouping_5_5_2_2",block_grouping_5_5_2_2 ),
	("block_grouping_5_5_2_3", block_grouping_5_5_2_3),
	("block_grouping_11_10_2_2",block_grouping_11_10_2_2)])
	def test_block_grouping(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),[problem_name +'.pddl'],planner_name)

	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("block_grouping_20_25_6_2",block_grouping_20_25_6_2 ),
	("block_grouping_20_25_6_3",block_grouping_20_25_6_3 )])
	@pytest.mark.skipif((len(sys.argv)<2 or sys.argv[1] == '-s' or sys.argv[1] == '-simple'),reason ="currently running in simple mode")
	def test_block_grouping_medium(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),[problem_name +'.pddl'],planner_name)

	