import upf
from upf.shortcuts import *

from unittest import TestCase, main
from planning_tests.numeric_planning.problems.problem_basic import UPFBasic

class TestBasic(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.problem = UPFBasic(expected_version=1)

    def test_basic(self):
        upf_problem = self.problem.get_problem()

        planner_names = [n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()]

        for p in planner_names:
            with OneshotPlanner(name=p) as planner:
                if planner.supports(upf_problem.kind()):
                    plan = planner.solve(upf_problem)
                    with PlanValidator(problem_kind=upf_problem.kind()) as validator:
                        check = validator.validate(upf_problem, plan)
                        self.assertTrue(check)


if __name__ == "__main__":
    main()
