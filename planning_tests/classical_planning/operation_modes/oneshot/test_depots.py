import unified_planning
from unified_planning.environment import get_env
from unified_planning.shortcuts import *
from planning_tests.classical_planning.pddl_problems.depots.depots import depots_pfile1, depots_pfile2, depots_pfile3
from planning_tests.classical_planning.operation_modes.oneshot.util import run_oneshot_planner_on_solvable_problem
import pytest
import sys


class TestDepots:

    planner_names = [n for n in get_env().factory.engines
                     if get_env().factory.engine(n).is_oneshot_planner()]


    depots_pfile1 = depots_pfile1(expected_version=1)
    depots_pfile2 = depots_pfile2(expected_version=1)
    depots_pfile3 = depots_pfile3(expected_version=1)


    @pytest.mark.all
    @pytest.mark.simple 
    @pytest.mark.depots
    @pytest.mark.parametrize("planner_name", planner_names)
    @pytest.mark.parametrize("problem_name, problem, optimal_cost",
            [
                ("depots_pfile1", depots_pfile1, 10),
                ("depots_pfile2", depots_pfile2, 15),
            ])
    def test_depots(self, planner_name, problem_name, problem, optimal_cost):
        up_problem = problem.get_problem()
        validate = False
        run_oneshot_planner_on_solvable_problem(planner_name, up_problem, optimal_cost, validate)


    @pytest.mark.all
    @pytest.mark.medium  # trivial for satisficing but already taking some time for optimal planner
    @pytest.mark.depots
    @pytest.mark.parametrize("planner_name", planner_names)
    @pytest.mark.parametrize("problem_name, problem, optimal_cost", [ ("depots_pfile3", depots_pfile3, 27), ])
    def test_depots_medium(self, planner_name, problem_name, problem, optimal_cost):
        up_problem = problem.get_problem()
        validate = False
        run_oneshot_planner_on_solvable_problem(planner_name, up_problem, optimal_cost, validate)
