import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.fn_counters.pddl_fn_counters import fn_counters_2, fn_counters_4, fn_counters_8, fn_counters_20
import pytest
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names


class TestPddlFNCounters:

	
	fn_counters_2 = fn_counters_2(expected_version=1)
	fn_counters_4 = fn_counters_4(expected_version=1)
	fn_counters_8 = fn_counters_8(expected_version=1)
	fn_counters_20 = fn_counters_20(expected_version=1)

	  	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(fn_counters_2.get_problem().kind)

 
	@pytest.mark.all
	@pytest.mark.fn_counters
	@pytest.mark.simple	
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("fn_counters_2",fn_counters_2 ),
	("fn_counters_4",fn_counters_4),
	("fn_counters_8",fn_counters_8)])
	def test_fn_counters(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name,[problem_name +'.pddl'])


	

