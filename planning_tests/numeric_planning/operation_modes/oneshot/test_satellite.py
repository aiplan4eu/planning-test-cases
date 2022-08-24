import unified_planning
from unified_planning.shortcuts import*
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names
from planning_tests.numeric_planning.pddl_problems.satellite.satellite import satellite_pfile1
import pytest
import sys


class TestSatellite:

    satellite_pfile1 = satellite_pfile1(expected_version=1)
   

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(satellite_pfile1.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple 
    @pytest.mark.satellite
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("satellite_pfile1",satellite_pfile1 )])
    def test_satellite(self,planner_name,problem_name,problem):
        print(problem.get_problem().kind)
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name,[problem_name +'.pddl'])