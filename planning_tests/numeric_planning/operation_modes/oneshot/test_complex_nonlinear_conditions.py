import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.up_problems.complex_nonlinear_conditions import UPNonLinearDisjunctiveConditions, UPNonLinearExistentialConditions, UPNonLinearUniversalConditions
from planning_tests.utility.planner_names import get_planner_names
from planning_tests.utility.util import TestUtil
import pytest

class TestComplexNonLinearConditions:


	problem_nonlinear_disjunctive_conditions = UPNonLinearDisjunctiveConditions(expected_version=1)
	problem_nonlinear_existential_conditions = UPNonLinearExistentialConditions(expected_version=1)
	problem_nonlinear_universal_conditions = UPNonLinearUniversalConditions(expected_version=1)

	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(problem_nonlinear_disjunctive_conditions.get_problem().kind)

	@pytest.mark.all
	@pytest.mark.complex_nonlinear_conditions
	@pytest.mark.simple
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("test_nonlinear_disjunctive_conditions",problem_nonlinear_disjunctive_conditions),
	("test_nonlinear_existential_conditions",problem_nonlinear_existential_conditions ),
	("test_nonlinear_universal_conditions",problem_nonlinear_universal_conditions)])
	def test_nonlinear_complex_conditions(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)




