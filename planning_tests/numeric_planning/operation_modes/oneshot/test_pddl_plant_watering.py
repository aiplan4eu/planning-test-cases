import unified_planning
from unified_planning.model import problem_kind
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.plant_watering.pddl_plant_watering import plant_watering_4_1, plant_watering_4_2, plant_watering_4_3, plant_watering_18_2, plant_watering_20_3
from unified_planning.environment import get_env
from unittest import TestCase, main
import os
from planning_tests.correct_output import correct
import pytest

#path = '/home/valerik/Desktop/programmazione/planning/planning-test-cases/planning_tests/numeric_planning/pddl_problems/plant_watering/'

class TestPddlPlantWatering:

 
    problem_4_1 = plant_watering_4_1(expected_version=1)
    problem_4_2 = plant_watering_4_2(expected_version=1)
    problem_4_3 = plant_watering_4_3(expected_version=1)
    problem_18_2 = plant_watering_18_2(expected_version=1)
    problem_20_3 = plant_watering_20_3(expected_version=1)

    @staticmethod
    def execute_one_shot_planning_test(problem,name):
        planner_names = [n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()]

        results = {}
        for p in planner_names:
            with OneshotPlanner(name=p) as planner:
                if planner.supports(problem.kind):
                    plan = planner.solve(problem)
                    #open(f"output","w").write('\n'.join([str(act) for act in plan.plan.actions]))
                    #correct("output")
                    #os.system("./validate -v  "+ path +"plant_watering_domain.pddl "+ path + name +" output")
                    with PlanValidator(problem_kind=problem.kind) as validator:
                        check = validator.validate(problem, plan.plan)
                        results[p] = check
                        assert check
        print(f'Problem kind: {" " }')
        print(problem.kind)
        print(f'Planners executed: {" ".join(results.keys())}')

    #@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_problem_4_1(self):
        self.execute_one_shot_planning_test(self.problem_4_1.get_problem(),'plant_watering_4_1.pddl')

    #@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_problem_4_2(self):
        self.execute_one_shot_planning_test(self.problem_4_2.get_problem(),'plant_watering_4_2.pddl')

    #@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_problem_4_3(self):
        self.execute_one_shot_planning_test(self.problem_4_3.get_problem(),'plant_watering_4_3.pddl')

    #@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_problem_18_2(self):
        self.execute_one_shot_planning_test(self.problem_18_2.get_problem(),'plant_watering_18_2.pddl')

    #@pytest.mark.parametrize("planner_name",[n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()])
    def test_problem_20_3(self):
        self.execute_one_shot_planning_test(self.problem_20_3.get_problem(),'plant_watering_20_3.pddl')

    



