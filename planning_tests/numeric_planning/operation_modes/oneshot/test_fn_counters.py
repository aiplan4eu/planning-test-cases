import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.fn_counters.fn_counters import fn_counters_2, fn_counters_4, fn_counters_8
from unified_planning.environment import get_env
import pytest



class TestHandmadeFNCounters:

    fn_counters_2 = fn_counters_2(expected_version=1)
    fn_counters_4 = fn_counters_4(expected_version=1)
    fn_counters_8 = fn_counters_8(expected_version=1)
   

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
    def test_fn_counters_2(self,planner_name):
        self.execute_one_shot_planning_test(self.fn_counters_2.get_problem(),planner_name)

    @pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_fn_counters_4(self,planner_name):
        self.execute_one_shot_planning_test(self.fn_counters_4.get_problem(),planner_name)

    @pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_fn_counters_8(self,planner_name):
        self.execute_one_shot_planning_test(self.fn_counters_8.get_problem(),planner_name)

