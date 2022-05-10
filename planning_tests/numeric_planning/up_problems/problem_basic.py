import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem

class UPBasic(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', IntType())
        y = Fluent('y', IntType())
        a = InstantaneousAction('a')
        a.add_precondition(GE(y, 10))
        a.add_effect(x, Plus(x, 10))
        a.add_effect(y, Minus(y, 10))
        problem = Problem('basic_numeric')
        problem.add_fluent(x)
        problem.add_fluent(y)
        problem.add_action(a)
        problem.set_initial_value(x, 0)
        problem.set_initial_value(y, 10)
        problem.add_goal(GE(x, 10))
        return problem

    def get_description(self):
        return 'Just a basic test'

    def version(self):
        return 1
