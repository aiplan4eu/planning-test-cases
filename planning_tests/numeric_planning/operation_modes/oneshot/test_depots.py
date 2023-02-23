import unified_planning
from unified_planning.shortcuts import*
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names, get_planner_names_opt
from planning_tests.numeric_planning.pddl_problems.depots.depots import depots_pfile1, depots_pfile2, depots_pfile3, depots_pfile10, depots_pfile11
import pytest



class TestDepots:

    depots_pfile1 = depots_pfile1(expected_version=1)
    depots_pfile2 = depots_pfile2(expected_version=1)
    depots_pfile3 = depots_pfile3(expected_version=1)
    depots_pfile10 = depots_pfile10(expected_version=1)
    depots_pfile11 = depots_pfile11(expected_version=1)

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(depots_pfile1.get_problem().kind)
    planner_names_opt = get_planner_names_opt(depots_pfile1.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple 
    @pytest.mark.depots
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("depots_pfile1",depots_pfile1 ),
    ("depots_pfile2",depots_pfile2 ),
    ("depots_pfile3",depots_pfile3 )])
    def test_depots(self,planner_name,problem_name,problem):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name,[problem_name +'.pddl'])


    @pytest.mark.all
    @pytest.mark.medium
    @pytest.mark.depots
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("depots_pfile10",depots_pfile10 ),
    ("depots_pfile11",depots_pfile11 )])
    def test_depots_medium(self,planner_name,problem_name,problem):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name,[problem_name +'.pddl'])

    @pytest.mark.optimal
    @pytest.mark.depotsopt
    @pytest.mark.parametrize("planner_name",planner_names_opt)
    @pytest.mark.parametrize("problem_name,problem,expected_plan_length",[("depots_pfile1",depots_pfile1,10 ),
    ("depots_pfile2",depots_pfile2,15),
    ("depots_pfile3",depots_pfile3,27)])
    def test_depots_optimal(self,planner_name,problem_name,problem,expected_plan_length):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name,[problem_name +'.pddl'],expected_plan_length)

