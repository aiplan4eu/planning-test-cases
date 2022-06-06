import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.block_grouping.handmade_block_grouping import blocksworld_5_5_2_1, blocksworld_5_5_2_2, blocksworld_5_5_2_3
from unified_planning.environment import get_env
import pytest



class TestHandmadeBlockGrouping:


    blocksworld_5_5_2_1 = blocksworld_5_5_2_1(expected_version=1)
    blocksworld_5_5_2_2 = blocksworld_5_5_2_2(expected_version=1)
    blocksworld_5_5_2_3 = blocksworld_5_5_2_3(expected_version=1)

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
    def test_blocksworld_5_5_2_1(self,planner_name):
        self.execute_one_shot_planning_test(self.blocksworld_5_5_2_1.get_problem(),planner_name)

    @pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_blocksworld_5_5_2_2(self,planner_name):
        self.execute_one_shot_planning_test(self.blocksworld_5_5_2_2.get_problem(),planner_name)

    @pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_blocksworld_5_5_2_3(self,planner_name):
        self.execute_one_shot_planning_test(self.blocksworld_5_5_2_3.get_problem(),planner_name)




