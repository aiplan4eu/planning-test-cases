import unified_planning
from unified_planning.model import problem
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.up_problems.simple_linear_conditions import UPEqualityConditions, UPGreaterLowerConditions, UPNegativeConditions, UPGreaterThanConditions, UPLowerThanConditions
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import anytime_names
import pytest


class TestSimpleLinearConditions:

	
	problem_equality = UPEqualityConditions(expected_version=1)
	problem_negative_conditions = UPNegativeConditions(expected_version=1)
	problem_greater_lower_conditions = UPGreaterLowerConditions(expected_version=1)
	problem_lower_than_conditions = UPGreaterThanConditions(expected_version=1)
	problem_greater_than_conditions = UPLowerThanConditions(expected_version=1)

	planner_names = anytime_names(problem_equality.get_problem().kind)



	@pytest.mark.all
	@pytest.mark.simple_linear_conditions
	@pytest.mark.simple	
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("test_equality",problem_equality ),
	("test_negative_conditions",problem_negative_conditions ),
	("test_greater_than_conditions", problem_greater_than_conditions),
	("test_lower_than_conditions",problem_lower_than_conditions),
	("test_greater_lower_conditions", problem_greater_lower_conditions)])
	def test_simple_linear_conditions(self,planner_name,problem_name,problem):
		TestUtil.execute_anytime_planning_test(problem.get_problem(),planner_name)