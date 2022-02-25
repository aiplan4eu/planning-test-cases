import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem


class UPDisjunctiveConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        obj = UserType('Obj')
        x = unified_planning.model.Object('x', obj)
        y = unified_planning.model.Object('y', obj)

        problem = Problem('disjunctive_linear_conditions')
        problem.add_objects([x, y])

        fun = Fluent('fun', IntType(), [obj])
        problem.add_fluent(fun, default_initial_value=0)

        action = InstantaneousAction('action1')
        action.add_precondition(Or(GT(fun(x), 10), GT(fun(y), 10)))
        action.add_effect(fun(y), Plus(fun(y), 10))
        problem.add_action(action)

        problem.set_initial_value(fun(x), 11)
        problem.add_goal(Or(Equals(fun(y), 10), LT(fun(x), 1)))
        return problem

    def get_description(self):
        return 'A simple problem with disjunctive linear conditions'

    def version(self):
        return 1


class UPExistentialConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        obj = UserType('Obj')
        x = unified_planning.model.Object('x', obj)
        y = unified_planning.model.Object('y', obj)

        problem = Problem('existential_linear_conditions')
        problem.add_objects([x, y])

        fun = Fluent('fun', IntType(), [obj])
        problem.add_fluent(fun, default_initial_value=0)

        action = InstantaneousAction('action1', param=obj)
        param = action.parameter('param')
        var = unified_planning.model.Variable('a', obj)
        action.add_precondition(Exists(GT(fun(var), 10), var))
        action.add_effect(fun(param), Plus(fun(param), 10))
        problem.add_action(action)

        problem.set_initial_value(fun(x), 11)

        problem.add_goal(Exists(Equals(fun(var), 10), var))

        return problem

    def get_description(self):
        return 'A simple problem with existential linear conditions'

    def version(self):
        return 1


class UPUniversalConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        obj = UserType('Obj')
        x = unified_planning.model.Object('x', obj)
        y = unified_planning.model.Object('y', obj)

        problem = Problem('universal_linear_conditions')
        problem.add_objects([x, y])

        fun = Fluent('fun', IntType(), [obj])
        problem.add_fluent(fun, default_initial_value=0)
        var = unified_planning.model.Variable('a', obj)

        action1 = InstantaneousAction('action1', param1=obj, param2=obj)
        param1 = action1.parameter('param1')
        param2 = action1.parameter('param2')

        action1.add_precondition(Forall(Equals(fun(var), 0), var))
        action1.add_effect(fun(param1), Plus(fun(param1), 5))
        action1.add_effect(fun(param2), Plus(fun(param2), 5))
        problem.add_action(action1)

        problem.add_goal(Forall(Equals(fun(var), 5), var))

        return problem

    def get_description(self):
        return 'A simple problem with universal linear conditions'

    def version(self):
        return 1


class UPComplexUniversalExistentialConditions(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        type1 = UserType('Type1')
        type2 = UserType('Type2')
        x = unified_planning.model.Object('x', type1)
        y = unified_planning.model.Object('y', type1)

        z = unified_planning.model.Object('z', type2)
        k = unified_planning.model.Object('k', type2)

        problem = Problem('universal_existential_linear_conditions')
        problem.add_objects([x, y, z, k])

        fun = Fluent('fun', RealType(), [type1, type2])
        problem.add_fluent(fun, default_initial_value=0)

        action = InstantaneousAction('action1', param1=type1, param2=type2)
        param1 = action.parameter('param1')
        param2 = action.parameter('param2')
        var1 = unified_planning.model.Variable('a', type1)
        var2 = unified_planning.model.Variable('b', type2)
        action.add_precondition(Forall(Exists(GT(fun(var1, var2), 0), var2), var1))
        action.add_effect(fun(param1, param2), Plus(fun(param1, param2), 1.5))
        problem.add_action(action)

        problem.set_initial_value(fun(x, z), 0.1)
        problem.set_initial_value(fun(y, k), 0.1)

        problem.add_goal(Forall(Exists(GT(fun(var1, var2), 1.5), var2), var1))

        return problem

    def get_description(self):
        return 'A simple problem with complex universal and existential linear conditions'

    def version(self):
        return 1
