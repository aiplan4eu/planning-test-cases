import unified_planning
from unified_planning.shortcuts import *

from unittest import TestCase, main
from planning_tests.classical_planning.problems.problem_basic import UPBasic

class TestBasic(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.problem = UPBasic(expected_version=1)

    def test_basic(self):
        up_problem = self.problem.get_problem()

        planner_names = [n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()]

        for p in planner_names:
            with OneshotPlanner(name=p) as planner:
                if planner.supports(up_problem.kind()):
                    plan = planner.solve(up_problem)
                    with PlanValidator(problem_kind=up_problem.kind()) as validator:
                        check = validator.validate(up_problem, plan)
                        self.assertTrue(check)


if __name__ == "__main__":
    main()
