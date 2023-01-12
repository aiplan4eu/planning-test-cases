import pytest
from planning_tests.temporal_planning.up_problems.majsp import Majsp
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names


class TestMajsp:

    problem_majsp_1 = Majsp_1(expected_version=1)

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(problem_majsp_1.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("test_majsp_1",problem_majsp_1)])
    def test_majsp_1(self,planner_name,problem,problem_name):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)

    problem_majsp_2 = Majsp_2(expected_version=1)

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(problem_majsp_2.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("test_majsp_2",problem_majsp_2)])
    def test_majsp_2(self,planner_name,problem,problem_name):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)

    problem_majsp_3 = Majsp_3(expected_version=1)

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(problem_majsp_3.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("test_majsp_3",problem_majsp_3)])
    def test_majsp_3(self,planner_name,problem,problem_name):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)

    problem_majsp_4 = Majsp_4(expected_version=1)

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(problem_majsp_4.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("test_majsp_4",problem_majsp_4)])
    def test_majsp_4(self,planner_name,problem,problem_name):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)

    problem_majsp_5 = Majsp_5(expected_version=1)

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(problem_majsp_5.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("test_majsp_5",problem_majsp_5)])
    def test_majsp_5(self,planner_name,problem,problem_name):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)

    problem_majsp_6 = Majsp_6(expected_version=1)

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(problem_majsp_6.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("test_majsp_6",problem_majsp_6)])
    def test_majsp_6(self,planner_name,problem,problem_name):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)

    problem_majsp_7 = Majsp_7(expected_version=1)

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(problem_majsp_7.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("test_majsp_7",problem_majsp_7)])
    def test_majsp_7(self,planner_name,problem,problem_name):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)

    problem_majsp_8 = Majsp_8(expected_version=1)

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(problem_majsp_8.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("test_majsp_8",problem_majsp_8)])
    def test_majsp_8(self,planner_name,problem,problem_name):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)

    problem_majsp_9 = Majsp_9(expected_version=1)

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(problem_majsp_9.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("test_majsp_9",problem_majsp_9)])
    def test_majsp_9(self,planner_name,problem,problem_name):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)

    problem_majsp_10 = Majsp_10(expected_version=1)

    #we check only the first problem, since the domain is the same for all the problems
    planner_names = get_planner_names(problem_majsp_10.get_problem().kind)

    @pytest.mark.all
    @pytest.mark.simple
    @pytest.mark.parametrize("planner_name",planner_names)
    @pytest.mark.parametrize("problem_name,problem",[("test_majsp_10",problem_majsp_10)])
    def test_majsp_10(self,planner_name,problem,problem_name):
        TestUtil.execute_one_shot_planning_test(problem.get_problem(),planner_name)
