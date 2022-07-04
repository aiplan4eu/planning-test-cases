from unified_planning.shortcuts import *
from planning_tests.numeric_planning.up_problems.constant_additive_effects import UPConstantIncreaseEffects, UPConstantDecreaseEffects, extend_problem
from planning_tests.utility.planner_names import get_planner_names
from planning_tests.utility.util import TestUtil
import pytest


class TestLinearEffects:

	
	problem_increase = UPConstantIncreaseEffects(expected_version=1)
	problem_decrease = UPConstantDecreaseEffects(expected_version=1)

	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(problem_increase.get_problem().kind)


	@pytest.mark.all
	@pytest.mark.constant_additive_effects
	@pytest.mark.simple
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem,expected_plan_length",[("test_increase_effect",problem_increase,1),
	("test_decrease_effect",problem_decrease,2 ),])
	def test_constant_additive_effects(self,planner_name,problem_name,problem,expected_plan_length):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name,"",expected_plan_length)


	@pytest.mark.all
	@pytest.mark.constant_additive_effects
	@pytest.mark.simple
	@pytest.mark.parametrize("planner_name",planner_names)
	def test_increase_and_decrease_effects(self,planner_name):
		problem = Problem('mixed_test')
		for extension in [self.problem_increase.problem_extension, self.problem_decrease.problem_extension]:
			extend_problem(problem, extension)
		TestUtil.execute_one_shot_planning_test(problem,planner_name,"", expected_plan_length=3)




