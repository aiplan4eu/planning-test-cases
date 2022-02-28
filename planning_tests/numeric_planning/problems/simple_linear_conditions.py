import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem


class UPGreaterThanConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', RealType())
        problem = Problem('GT_linear_conditions')
        problem.set_initial_value(x, 5.1)
        problem.add_goal(GT(x, 10))

        a1 = InstantaneousAction('a1')
        a1.add_precondition(GT(x, 5.05))
        a1.add_effect(x, Plus(x, 5.09))

        problem.add_fluent(x)
        problem.add_action(a1)
        return problem

    def get_description(self):
        return 'A simple problem with linear GT conditions'

    def version(self):
        return 1


class UPLowerThanConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', RealType())
        problem = Problem('LT_linear_conditions')
        problem.set_initial_value(x, 5.1)
        problem.add_goal(LT(x, 0.1))

        a1 = InstantaneousAction('a1')
        a1.add_precondition(LT(x, 5.15))
        a1.add_effect(x, Minus(x, 5.01))

        problem.add_fluent(x)
        problem.add_action(a1)
        return problem

    def get_description(self):
        return 'A simple problem with linear LT conditions'

    def version(self):
        return 1


class UPGreaterLowerConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', IntType())
        problem = Problem('GTE_LTE_linear_conditions')
        problem.set_initial_value(x, 0)
        problem.add_goal(GE(x, 10))

        a1 = InstantaneousAction('increase-to-5')
        a1.add_precondition(LT(x, 5))
        a1.add_effect(x, Plus(x, 5))

        a2 = InstantaneousAction('increase-to-10')
        a2.add_precondition(GT(x, 4))
        a2.add_precondition(LE(x, 9))
        a2.add_effect(x, Plus(x, 5))

        problem.add_fluent(x)
        problem.add_action(a1)
        problem.add_action(a2)
        return problem

    def get_description(self):
        return 'A simple problem with linear GT/LT/GE/LE conditions'

    def version(self):
        return 1


class UPNegativeConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', IntType())
        a = InstantaneousAction('action1')
        a.add_precondition(Not(Equals(x, 10)))
        a.add_effect(x, Minus(x, 10))
        problem = Problem('negative_linear_conditions')
        problem.add_fluent(x)
        problem.add_action(a)
        problem.set_initial_value(x, 0)
        problem.add_goal(Not(Equals(x, 0)))
        return problem

    def get_description(self):
        return 'A simple problem with negative linear conditions'

    def version(self):
        return 1


class UPEqualityConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x', IntType())
        a = InstantaneousAction('action1')
        a.add_effect(x, Minus(x, 10))
        problem = Problem('equality_linear_conditions')
        problem.add_fluent(x)
        problem.add_action(a)
        problem.set_initial_value(x, 10)
        problem.add_goal(Equals(x, 0))
        return problem

    def get_description(self):
        return 'A simple problem with linear equality conditions'

    def version(self):
        return 1
