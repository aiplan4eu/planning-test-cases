import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.up_problems.nonlinear_effects import UPNonLinearIncreaseEffects, UPNonLinearAssignEffects, UPNonLinearConditionalEffects
import pytest
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names


class TestNonLinearEffects:

	
	problem_nonlinear_increase_effects = UPNonLinearIncreaseEffects(expected_version=1)
	problem_nonlinear_assign_continuous_effects = UPNonLinearAssignEffects(expected_version=1)
	problem_nonlinear_assign_conditional_effects = UPNonLinearConditionalEffects(expected_version=1)

	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(problem_nonlinear_increase_effects.get_problem().kind)

 
	
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("test_increase_effects",problem_nonlinear_increase_effects ),
	("test_assign_continuous_effects",problem_nonlinear_assign_continuous_effects),
	("test_assign_conditional_effects",problem_nonlinear_assign_conditional_effects)])
	def test_nonlinear_effects(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),["none"],planner_name)






