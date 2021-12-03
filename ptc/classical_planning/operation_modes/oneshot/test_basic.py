import upf
from upf.shortcuts import *

from unittest import TestCase, main
from ptc.classical_planning.problems.problem_basic import Basic1, Basic2

class Check1(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.problems = {Basic1(version=1): 10}

    def test_basic(self):
        upf_problem = self.problems[0].get_problem()
        a = upf_problem.action('a')

        with OneshotPlanner(name='pyperplan') as planner:
            plan = planner.solve(upf_problem)
            with PlanValidator(problem_kind=upf_problem.kind()) as validator:
                check = validator.validate(upf_problem, plan)
                self.assertTrue(check)

    def test_advanced(self):
        upf_problem = self.problems[1].get_problem()
        a = upf_problem.action('a')

        with OneshotPlanner(name='pyperplan') as planner:
            plan = planner.solve(upf_problem)
            with PlanValidator(problem_kind=upf_problem.kind()) as validator:
                check = validator.validate(upf_problem, plan)
                self.assertTrue(check)


if __name__ == "__main__":
    main()