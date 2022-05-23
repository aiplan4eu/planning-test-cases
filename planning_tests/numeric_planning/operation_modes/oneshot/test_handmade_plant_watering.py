import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.plant_watering.handmade_plant_watering import plant_watering_4_1, plant_watering_4_2, plant_watering_4_3
from unified_planning.environment import get_env
from unittest import TestCase, main



class TestHandmadePlantWatering(TestCase):

    def setUp(self):
        self.problem_4_1 = plant_watering_4_1(expected_version=1)
        self.problem_4_2 = plant_watering_4_2(expected_version=1)
        self.problem_4_3 = plant_watering_4_3(expected_version=1)
       

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

    def test_problem_4_1(self):
        self.execute_one_shot_planning_test(self.problem_4_1.get_problem())

    def test_problem_4_2(self):
        self.execute_one_shot_planning_test(self.problem_4_2.get_problem())

    def test_problem_4_3(self):
        self.execute_one_shot_planning_test(self.problem_4_3.get_problem())

    


if __name__ == '__main__':
    main()

