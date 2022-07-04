import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem


class UPNonLinearIncreaseEffects(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', IntType())
        a = InstantaneousAction('action1')
        a.add_increase_effect(x, Times(x, Times(x, x)))
        problem = Problem('nonlinear_increase_effects')
        problem.add_fluent(x)
        problem.add_action(a)
        problem.set_initial_value(x, 2)
        problem.add_goal(Equals(x, 10))
        return problem

    def get_description(self):
        return 'A simple problem with non linear increase effects'

    def version(self):
        return 1


class UPNonLinearAssignEffects(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', RealType())
        y = Fluent('y', RealType())
        a = InstantaneousAction('action1')
        a.add_effect(x, Div(x, Times(y, y)))
        problem = Problem('nonlinear_assign_effects')
        problem.add_fluent(x)
        problem.add_fluent(y)
        problem.add_action(a)
        problem.set_initial_value(x, 1)
        problem.set_initial_value(y, 2)
        problem.add_goal(Equals(x, 0.0625))
        return problem

    def get_description(self):
        return 'A simple problem with non linear assign effects'

    def version(self):
        return 1


class UPNonLinearConditionalEffects(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', IntType())
        y = Fluent('y', IntType())
        a = InstantaneousAction('action1')
        a.add_effect(fluent=x, value=Plus(x, 1), condition=Equals(Times(x, y), Times(x, x)))
        a.add_effect(fluent=y, value=Plus(y, 1), condition=Equals(Times(x, y), Times(x, x)))
        problem = Problem('nonlinear_conditional_effects')
        problem.add_fluent(x)
        problem.add_fluent(y)
        problem.add_action(a)
        problem.set_initial_value(x, 1)
        problem.set_initial_value(y, 1)
        problem.add_goal(Equals(Times(x, y), 25))
        return problem

    def get_description(self):
        return 'A simple problem with non linear conditional effects'

    def version(self):
        return 1




