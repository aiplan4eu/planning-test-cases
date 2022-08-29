from unified_planning.shortcuts import *
from planning_tests.classical_planning.pddl_problems.depots.depots import depots_pfile1, depots_pfile2, depots_pfile3
from planning_tests.classical_planning.operation_modes.oneshot.util import run_oneshot_planner_on_solvable_problem
import pytest

class TestDepots:

    depots_pfile1 = depots_pfile1(expected_version=1)
    depots_pfile2 = depots_pfile2(expected_version=1)
    depots_pfile3 = depots_pfile3(expected_version=1)

    @pytest.mark.all
    @pytest.mark.depots
    @pytest.mark.parametrize("problem_name, problem, optimal_cost",
            [
                pytest.param("depots_pfile1", depots_pfile1, 10, marks=pytest.mark.simple),
                pytest.param("depots_pfile2", depots_pfile2, 15, marks=pytest.mark.simple),
                pytest.param("depots_pfile3", depots_pfile3, 27, marks=pytest.mark.medium),
            ])
    def test_depots(self, oneshot_planner_name, problem_name, problem, optimal_cost):
        up_problem = problem.get_problem()
        validate = False
        run_oneshot_planner_on_solvable_problem(oneshot_planner_name, up_problem, optimal_cost, validate)
