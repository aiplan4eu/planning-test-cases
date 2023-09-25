import unified_planning
from unified_planning.shortcuts import *
from unified_planning.model.multi_agent import *
import unittest
from unittest import TestCase, main
from planning_tests.multiagent_planning.problems.ma_basic import UPMABasic


class TestMABasic(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.problem = UPMABasic(expected_version=1)

    def test_mabasic(self):
        up_problem = self.problem.get_problem()
        with OneshotPlanner(name="fmap") as planner:
            if planner.supports(up_problem.kind):
                result = planner.solve(up_problem, None, "1")
                with PlanValidator(name="fmap") as validator:
                    print("ok")
                    # check = validator.validate(up_problem, result.plan)
                    # self.assertTrue(check)


if __name__ == "__main__":
    main()
