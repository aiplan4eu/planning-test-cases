import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem

class UPConditionalEffects(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x')
        y = Fluent('y')
        a = InstantaneousAction('a')
        a.add_effect(x, True)
        b = InstantaneousAction('b')
        b.add_effect(y, True, x)
        problem = Problem('conditional_effect')
        problem.add_fluent(x)
        problem.add_fluent(y)
        problem.add_action(a)
        problem.add_action(b)
        problem.set_initial_value(x, False)
        problem.set_initial_value(y, False)
        problem.add_goal(y)
        return problem

    def get_description(self):
        return 'Simple problem with conditional effect'

    def version(self):
        return 1
