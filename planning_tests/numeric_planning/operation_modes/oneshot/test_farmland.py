import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.farmland.farmland import farmland_2_100_1229, farmland_2_200_1229, farmland_2_300_1229, farmland_8_400_1229, farmland_10_400_1229, farmland_10_1000_1229
from unified_planning.environment import get_env
import pytest
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names


class TestFarmland:

	farmland_2_100_1229 = farmland_2_100_1229(expected_version=1)
	farmland_2_200_1229 = farmland_2_200_1229(expected_version=1)
	farmland_2_300_1229 = farmland_2_300_1229(expected_version=1)
	farmland_8_400_1229 = farmland_8_400_1229(expected_version=1)
	farmland_10_400_1229 = farmland_10_400_1229(expected_version=1)
	farmland_10_1000_1229 = farmland_10_1000_1229(expected_version=1)

 	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(farmland_2_100_1229.get_problem().kind)

	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("farmland_2_100",farmland_2_100_1229 ),
	("farmland_2_200_1229",farmland_2_200_1229 ),
	("farmland_2_300_1229", farmland_2_300_1229),
	("farmland_8_400_1229",farmland_8_400_1229),
	("farmland_10_400_1229",farmland_10_400_1229),
	("farmland_10_1000_1229",farmland_10_1000_1229)])
	def test_farmland(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),[problem_name +'.pddl'],planner_name)

	