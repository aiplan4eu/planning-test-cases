import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.farmland.pddl_farmland import farmland_2_100_1229, farmland_2_200_1229, farmland_2_300_1229, farmland_8_400_1229,farmland_10_400_1229, farmland_10_1000_1229
from unified_planning.environment import get_env
import pytest



class TestPddlFarmland:

    
    farmland_2_100_1229 = farmland_2_100_1229(expected_version=1)
    farmland_2_200_1229 = farmland_2_200_1229(expected_version=1)
    farmland_2_300_1229 = farmland_2_300_1229(expected_version=1)
    farmland_8_400_1229 = farmland_8_400_1229(expected_version=1)
    farmland_10_400_1229 = farmland_10_400_1229(expected_version=1)
    farmland_10_1000_1229 = farmland_10_1000_1229(expected_version=1)

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
    def test_farmland_2_100_1229(self,planner_name):
        self.execute_one_shot_planning_test(self.farmland_2_100_1229.get_problem(),planner_name)

    @pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_farmland_2_200_1229(self,planner_name):
        self.execute_one_shot_planning_test(self.farmland_2_200_1229.get_problem(),planner_name)

    @pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_farmland_2_300_1229(self,planner_name):
        self.execute_one_shot_planning_test(self.farmland_2_300_1229.get_problem(),planner_name)

    @pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_farmland_8_400_1229(self,planner_name):
        self.execute_one_shot_planning_test(self.farmland_8_400_1229.get_problem(),planner_name)

    @pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_farmland_10_400_1229(self,planner_name):
        self.execute_one_shot_planning_test(self.farmland_10_400_1229.get_problem(),planner_name)

    @pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_farmland_10_1000_1229(self,planner_name):
        self.execute_one_shot_planning_test(self.farmland_10_1000_1229.get_problem(),planner_name)



