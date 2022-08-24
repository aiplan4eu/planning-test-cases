import unified_planning
from unified_planning.shortcuts import *
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names
from planning_tests.numeric_planning.pddl_problems.TPP.TPP import TPP_p01
import pytest
import sys


class TestTPP:

	TPP_p01 = TPP_p01(expected_version=1)
	

	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(TPP_p01.get_problem().kind)
	#planner_names = ["enhsp"]

	@pytest.mark.all
	@pytest.mark.simple 
	@pytest.mark.TPP
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("TPP_p01",TPP_p01 )])
	def test_TPP(self,planner_name,problem_name,problem):
		print(problem.get_problem().kind)
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name,[problem_name +'.pddl'])