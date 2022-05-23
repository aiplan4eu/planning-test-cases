import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.fn_counters.handame_fn_counters import fn_counters_2, fn_counters_4
from unified_planning.environment import get_env
from unittest import TestCase, main
import pytest


class TestHandmadeFNCounters(TestCase):

    def setUp(self):
        self.fn_counters_2 = fn_counters_2(expected_version=1)
        self.fn_counters_4 = fn_counters_4(expected_version=1)

    @staticmethod
    def execute_one_shot_planning_test(problem):
        planner_names = [n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()]

        results = {}
        for p in planner_names:
            with OneshotPlanner(name=p) as planner:
                if planner.supports(problem.kind):
                    plan = planner.solve(problem)
                    with PlanValidator(problem_kind=problem.kind) as validator:
                        check = validator.validate(problem, plan.plan)
                        results[p] = check
                        assert check

        print(f'Planners executed: {" ".join(results.keys())}')

    @pytest.mark.xfail(reason="incorrect formulation of the problem")
    def test_fn_counters_2(self):
        self.execute_one_shot_planning_test(self.fn_counters_2.get_problem())
    @pytest.mark.xfail(reason="incorrect formulation of the problem")
    def test_fn_counters_4(self):
        self.execute_one_shot_planning_test(self.fn_counters_4.get_problem())



if __name__ == '__main__':
    main()

