import upf
from upf.shortcuts import *

from unittest import TestCase, main
from ptc.classical_planning.problems.problem_basic import Basic1

class Check1(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.problem = Basic1(expected_version=1)

    def test_basic(self):
        upf_problem = self.problem.get_problem()
        a = upf_problem.action('a')

        with OneshotPlanner(name='pyperplan') as planner:
            plan = planner.solve(upf_problem)
            with PlanValidator(problem_kind=upf_problem.kind()) as validator:
                check = validator.validate(upf_problem, plan)
                self.assertTrue(check)


if __name__ == "__main__":
    main()