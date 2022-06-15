import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.up_problems.complex_linear_conditions import UPDisjunctiveConditions, UPExistentialConditions, UPUniversalConditions, UPComplexUniversalExistentialConditions
from unified_planning.environment import get_env
import pytest
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names


class TestComplexLinearConditions:

   
	problem_disjunctive_conditions = UPDisjunctiveConditions(expected_version=1)
	problem_existential_conditions = UPExistentialConditions(expected_version=1)
	problem_universal_conditions = UPUniversalConditions(expected_version=1)
	problem_universal_existential_conditions = UPComplexUniversalExistentialConditions(expected_version=1)

 	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(problem_disjunctive_conditions.get_problem().kind)


	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("test_disjunctive_conditions",problem_disjunctive_conditions),
	("test_existential_conditions",problem_existential_conditions ),
	("test_universal_conditions",problem_universal_conditions),
	("test_universal_existential_conditions",problem_universal_existential_conditions)])
	def test_complex_conditions(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),["none"],planner_name)





