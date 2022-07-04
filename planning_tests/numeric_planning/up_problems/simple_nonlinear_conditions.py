import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem


class UPGreaterThanEqualityNonLinearConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', IntType())
        y = Fluent('y', IntType())
        problem = Problem('simple_non_linear_GT_equality_conditions')
        problem.set_initial_value(x, 3)
        problem.set_initial_value(y, 2)
        problem.add_goal(Equals(Times(x, y), 24))

        a1 = InstantaneousAction('a1')
        a1.add_precondition(GT(Plus(Times(x, x), y), 10))
        a1.add_effect(x, 6)
        a1.add_effect(y, 4)

        problem.add_fluent(x)
        problem.add_action(a1)
        return problem

    def get_description(self):
        return 'A simple problem with non linear GT and equality conditions'

    def version(self):
        return 1


class UPLowerEqualNegativeNonLinearConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', IntType())
        y = Fluent('y', IntType())
        problem = Problem('simple_non_linear_LE_Negative_conditions')
        problem.set_initial_value(x, 3)
        problem.set_initial_value(y, 2)
        problem.add_goal(Not(Equals(Times(x, y), 24)))
        problem.add_goal(Not(Equals(Times(x, y), 6)))

        a1 = InstantaneousAction('a1')
        a1.add_precondition(LE(Plus(Times(x, x), y), 40))
        a1.add_effect(x, Plus(x, 3))
        a1.add_effect(y, Plus(y, 2))

        problem.add_fluent(x)
        problem.add_action(a1)
        return problem

    def get_description(self):
        return 'A simple problem with non linear LE and negative conditions'

    def version(self):
        return 1


