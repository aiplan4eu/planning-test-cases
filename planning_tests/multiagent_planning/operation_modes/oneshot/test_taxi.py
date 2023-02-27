import unified_planning
from unified_planning.shortcuts import *
from unified_planning.model.multi_agent import *
import unittest
from unittest import TestCase, main
from planning_tests.multiagent_planning.problems.taxi import UPTaxi


class TestTaxi(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.problem = UPTaxi(expected_version=1)

    def test_taxi(self):
        up_problem = self.problem.get_problem()
        with OneshotPlanner(name="fmap") as planner:
            if planner.supports(up_problem.kind):
                result = planner.solve(up_problem, None, "2")
                with PlanValidator(name="fmap") as validator:
                    print("ok")
                    # check = validator.validate(up_problem, result.plan)
                    # self.assertTrue(check)


if __name__ == "__main__":
    main()
