import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.fn_counters_inv.pddl_fn_counters_inv import fn_counters_inv_16
from unified_planning.environment import get_env
from unittest import TestCase, main



class TestPddlFNCountersInv(TestCase):

    def setUp(self):
        self.fn_counters_inv_16 = fn_counters_inv_16(expected_version=1)


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

    def test_fn_counters_inv_16(self):
        self.execute_one_shot_planning_test(self.fn_counters_inv_16.get_problem())





if __name__ == '__main__':
    main()

