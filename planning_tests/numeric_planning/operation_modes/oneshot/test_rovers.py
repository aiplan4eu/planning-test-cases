import unified_planning
from unified_planning.shortcuts import*
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names
from planning_tests.numeric_planning.pddl_problems.rovers.rovers import  rovers_pfile2,rovers_pfile3,rovers_pfile4,rovers_pfile5
import pytest
import sys


class TestRovers:

    rovers_pfile3 = rovers_pfile3(expected_version=1)
    rovers_pfile2 = rovers_pfile2(expected_version=1)
    rovers_pfile4 = rovers_pfile4(expected_version=1)
    rovers_pfile5 = rovers_pfile5(expected_version=1)
    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(rovers_pfile2.get_problem().kind)

    
    @pytest.mark.all
    @pytest.mark.simple 
    @pytest.mark.rovers
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("rovers_pfile2",rovers_pfile2 ),
    ("rovers_pfile3",rovers_pfile3 ),
    ("rovers_pfile4",rovers_pfile4 )])
    def test_rovers(self,planner_name,problem_name,problem):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name,[problem_name +'.pddl'])


    @pytest.mark.all
    @pytest.mark.medium 
    @pytest.mark.rovers
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("rovers_pfile5",rovers_pfile5 )])
    def test_rovers_medium(self,planner_name,problem_name,problem):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name,[problem_name +'.pddl'])

