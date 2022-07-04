import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.block_grouping.handmade_block_grouping import blocksworld_5_5_2_1, blocksworld_5_5_2_2, blocksworld_5_5_2_3
from unified_planning.environment import get_env
import pytest
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names


class TestHandmadeBlockGrouping:


	block_grouping_5_5_2_1 = blocksworld_5_5_2_1(expected_version=1)
	block_grouping_5_5_2_2 = blocksworld_5_5_2_2(expected_version=1)
	block_grouping_5_5_2_3 = blocksworld_5_5_2_3(expected_version=1)

	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(block_grouping_5_5_2_1.get_problem().kind)

	@pytest.mark.all
	@pytest.mark.block_grouping
	@pytest.mark.simple
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("block_grouping_5_5_2_1",block_grouping_5_5_2_1 ),
	("block_grouping_5_5_2_2",block_grouping_5_5_2_2 ),
	("block_grouping_5_5_2_3", block_grouping_5_5_2_3)])
	def test_block_grouping(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name,[problem_name +'.pddl'])






