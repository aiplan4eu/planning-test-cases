import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.up_problems.linear_effects import UPConditionalEffects
import pytest
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names


class TestLinearEffects:

   
	problem_conditional_effects = UPConditionalEffects(expected_version=1)

	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(problem_conditional_effects.get_problem().kind)

	@pytest.mark.all
	@pytest.mark.linear_effects
	@pytest.mark.simple
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("test_conditional_effect",problem_conditional_effects)])
	def test_conditonal_effect(self,planner_name,problem,problem_name):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)








