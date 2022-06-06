import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.fn_counters_inv.pddl_fn_counters_inv import fn_counters_inv_16
from unified_planning.environment import get_env
import pytest
import sys



class TestPddlFNCountersInv:

    
    fn_counters_inv_16 = fn_counters_inv_16(expected_version=1)


    @staticmethod
    def execute_one_shot_planning_test(problem,planner_name):
        results = {}
        with OneshotPlanner(name=planner_name) as planner:
                if planner.supports(problem.kind):
                    plan = planner.solve(problem)
                    with PlanValidator(problem_kind=problem.kind) as validator:
                        check = validator.validate(problem, plan.plan)
                        results[planner_name] = check
                        assert check

        print(f'Planners executed: {" ".join(results.keys())}')

    @pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    @pytest.mark.skipif((len(sys.argv)<2 or sys.argv[1] == '-s' or sys.argv[1] == '-simple'), reason ="currently running in simple mode")
    def test_fn_counters_inv_16(self,planner_name):
        self.execute_one_shot_planning_test(self.fn_counters_inv_16.get_problem(),planner_name)






