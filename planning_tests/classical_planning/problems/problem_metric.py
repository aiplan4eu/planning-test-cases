# In this problem, one can either apply a single action for high cost
# or instead 3 actions for overall lower cost.

import unified_planning
from unified_planning.shortcuts import *
from unified_planning.model.metrics import MinimizeActionCosts, MinimizeSequentialPlanLength

from planning_tests.commons.problem import TestCaseProblem


def get_problem():
    x = Fluent('x')
    y = Fluent('y')
    g = Fluent('g')
    a_exp = InstantaneousAction('o_expensive')
    a_exp.add_effect(g, True)
    a_cheap_1 = InstantaneousAction('o_cheap_1')
    a_cheap_1.add_effect(x, True)
    a_cheap_2 = InstantaneousAction('o_cheap_2')
    a_cheap_2.add_precondition(x)
    a_cheap_2.add_effect(y, True)
    a_cheap_3 = InstantaneousAction('o_cheap_3')
    a_cheap_3.add_precondition(y)
    a_cheap_3.add_effect(g, True)
    problem = Problem('metric_impact')
    problem.add_fluent(x)
    problem.add_fluent(y)
    problem.add_fluent(g)
    problem.add_action(a_exp)
    problem.add_action(a_cheap_1)
    problem.add_action(a_cheap_2)
    problem.add_action(a_cheap_3)
    problem.set_initial_value(g, False)
    problem.set_initial_value(x, False)
    problem.set_initial_value(y, False)
    problem.add_goal(g)
    costs = {a_exp:Int(5), a_cheap_1:Int(1), a_cheap_2:Int(1), a_cheap_3:Int(2)}
    return problem, costs


class UPCostMetricWithConstantCosts(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        problem, costs = get_problem()
        metric = MinimizeActionCosts(costs, 1)
        problem.add_quality_metric(metric)
        return problem

    def get_description(self):
        return 'Problem for testing cost metric'

    def version(self):
        return 1


class UPLengthMetric(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        problem, costs = get_problem()
        metric = MinimizeSequentialPlanLength()
        problem.add_quality_metric(metric)
        return problem

    def get_description(self):
        return 'Problem for testing sequential plan length metric'

    def version(self):
        return 1
