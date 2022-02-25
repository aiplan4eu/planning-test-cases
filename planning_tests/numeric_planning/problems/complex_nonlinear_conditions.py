import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem


class UPNonLinearDisjunctiveConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        obj = UserType('Obj')
        x = unified_planning.model.Object('x', obj)
        y = unified_planning.model.Object('y', obj)

        problem = Problem('disjunctive_nonlinear_conditions')
        problem.add_objects([x, y])

        fun = Fluent('fun', RealType(), [obj])
        problem.add_fluent(fun)

        action = InstantaneousAction('action1')
        action.add_precondition(Or(Equals(Div(fun(y), fun(x)), 1.5), LT(fun(y), 2)))
        action.add_effect(fun(y), 10)
        problem.add_action(action)

        problem.set_initial_value(fun(x), 2)
        problem.set_initial_value(fun(y), 3)
        problem.add_goal(Or(Equals(Times(fun(x), fun(y)), 20), GT(fun(y), 100)))
        return problem

    def get_description(self):
        return 'A simple problem with disjunctive nonlinear conditions'

    def version(self):
        return 1


class UPNonLinearExistentialConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        obj = UserType('Obj')
        x = unified_planning.model.Object('x', obj)
        y = unified_planning.model.Object('y', obj)

        problem = Problem('existential_nonlinear_conditions')
        problem.add_objects([x, y])

        fun = Fluent('fun', IntType(), [obj])
        problem.add_fluent(fun)

        action = InstantaneousAction('action1')

        a = Variable('a', obj)
        condition = Exists(Equals(Times(fun(a), fun(x)), 6), a)

        action.add_precondition(condition)
        action.add_effect(fun(y), 4)
        problem.add_action(action)

        problem.set_initial_value(fun(x), 2)
        problem.set_initial_value(fun(y), 3)

        problem.add_goal(Exists(Equals(Times(fun(a), fun(x)), 8), a))
        return problem

    def get_description(self):
        return 'A simple problem with existential nonlinear conditions'

    def version(self):
        return 1


class UPNonLinearUniversalConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        obj = UserType('Obj')
        x = unified_planning.model.Object('x', obj)
        y = unified_planning.model.Object('y', obj)

        problem = Problem('universal_nonlinear_conditions')
        problem.add_objects([x, y])

        fun = Fluent('fun', IntType(), [obj])
        problem.add_fluent(fun)

        action = InstantaneousAction('action1')

        a = Variable('a', obj)
        condition = Forall(GT(Times(fun(a), fun(a)), 3), a)

        action.add_precondition(condition)
        action.add_effect(fun(x), 3)
        problem.add_action(action)

        problem.set_initial_value(fun(x), 2)
        problem.set_initial_value(fun(y), 3)

        problem.add_goal(Forall(Equals(Times(fun(a), fun(a)), 9), a))
        return problem

    def get_description(self):
        return 'A simple problem with universal nonlinear conditions'

    def version(self):
        return 1