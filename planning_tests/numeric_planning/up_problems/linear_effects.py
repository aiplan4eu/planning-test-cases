import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem


class UPConditionalEffects(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', IntType())
        a = InstantaneousAction('action1')
        a.add_effect(condition=Equals(x, 0), fluent=x, value=Plus(x, 11))
        problem = Problem('linear_conditional_effects')
        problem.add_fluent(x)
        problem.add_action(a)
        problem.set_initial_value(x, 0)
        problem.add_goal(GT(x, 10))
        return problem

    def get_description(self):
        return 'A simple problem with linear conditional effects'

    def version(self):
        return 1



