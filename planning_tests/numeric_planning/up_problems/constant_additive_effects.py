import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem


def extend_problem(problem, function):
    initial_values_to_add, goals_to_add, fluents_to_add, actions_to_add, objects_to_add = function()

    for key, value in initial_values_to_add:
        problem.set_initial_value(key, value)

    for goal in goals_to_add:
        problem.add_goal(goal)

    for fluent in fluents_to_add:
        problem.add_fluent(fluent)

    for action in actions_to_add:
        problem.add_action(action)

    problem.add_objects(objects_to_add)

    return problem


class UPConstantIncreaseEffects(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)
        self.signature = 'constant_increase_effect'

    def problem_extension(self):
        x = Fluent(f'x_{self.signature}', IntType())
        a = InstantaneousAction(f'action_{self.signature}')
        a.add_increase_effect(x, 10)

        initial_values = [(x, 0)]
        goals = [Equals(x, 10)]
        fluents = [x]
        actions = [a]
        objects = []

        return initial_values, goals, fluents, actions, objects

    def get_problem(self):
        problem = Problem(self.signature)
        return extend_problem(problem, self.problem_extension)

    def get_description(self):
        return 'A simple problem with constant increase effects'

    def version(self):
        return 1


class UPConstantDecreaseEffects(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)
        self.signature = 'constant_decrease_effect'

    def problem_extension(self):
        x = Fluent(f'x_{self.signature}', IntType())
        a = InstantaneousAction(f'action_{self.signature}')
        a.add_decrease_effect(x, 5)

        initial_values = [(x, 10)]
        goals = [Equals(x, 0)]
        fluents = [x]
        actions = [a]
        objects = []

        return initial_values, goals, fluents, actions, objects

    def get_problem(self):
        problem = Problem(self.signature)
        return extend_problem(problem, self.problem_extension)

    def get_description(self):
        return 'A simple problem with constant decrease effects'

    def version(self):
        return 1