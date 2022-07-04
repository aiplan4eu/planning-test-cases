import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.up_problems.simple_nonlinear_conditions import UPGreaterThanEqualityNonLinearConditions, UPLowerEqualNegativeNonLinearConditions
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names
import pytest


class TestSimpleNonLinearConditions:

	
	problem_gt_equality_nonlinear_conditions = UPGreaterThanEqualityNonLinearConditions(expected_version=1)
	problem_le_negative_nonlinear_conditions = UPLowerEqualNegativeNonLinearConditions(expected_version=1)


	planner_names = get_planner_names(problem_gt_equality_nonlinear_conditions.get_problem().kind)

	#lpg doesnt support non linear numeric conditions, but there isnt a difference in problem.kind right now
	@pytest.mark.all
	@pytest.mark.simple_nonlinear_conditions
	@pytest.mark.simple		
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("test_gt_equality_nonlinear_conditions",problem_gt_equality_nonlinear_conditions),
	("test_le_negative_nonlinear_conditions",problem_le_negative_nonlinear_conditions)])
	def test_simple_nonlinear_conditions(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)




