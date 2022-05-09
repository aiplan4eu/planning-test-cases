import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.problems.complex_linear_conditions import UPDisjunctiveConditions, UPExistentialConditions, UPUniversalConditions, UPComplexUniversalExistentialConditions
from unified_planning.environment import get_env
from unittest import TestCase, main


class TestComplexLinearConditions(TestCase):

    def setUp(self):
        self.problem_disjunctive_conditions = UPDisjunctiveConditions(expected_version=1)
        self.problem_existential_conditions = UPExistentialConditions(expected_version=1)
        self.problem_universal_conditions = UPUniversalConditions(expected_version=1)
        self.problem_universal_existential_conditions = UPComplexUniversalExistentialConditions(expected_version=1)

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

    def test_disjunctive_conditions(self):
        self.execute_one_shot_planning_test(self.problem_disjunctive_conditions.get_problem())

    def test_existential_conditions(self):
        self.execute_one_shot_planning_test(self.problem_existential_conditions.get_problem())

    def test_universal_conditions(self):
        self.execute_one_shot_planning_test(self.problem_universal_conditions.get_problem())

    def test_universal_existential_conditions(self):
        self.execute_one_shot_planning_test(self.problem_universal_existential_conditions.get_problem())


if __name__ == '__main__':
    main()
