import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem

class fn_counters_2(TestCaseProblem):
	
	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		obj = UserType("Obj")
		c1 = unified_planning.model.Object("c1",obj)
		c0 = unified_planning.model.Object("c0",obj)

		problem = Problem("fn-counters")
		problem.add_objects([c0,c1])

		#fluents
		value = Fluent("value",IntType(), o = obj)
		problem.add_fluent(value,default_initial_value=0)
		max_int = Fluent("max_int",IntType())
		problem.add_fluent(max_int,default_initial_value=1)

		#actions
		increment = InstantaneousAction("increment", c = obj)
		c = increment.parameter("c")
		increment.add_precondition(LT(value(c),max_int))
		increment.add_increase_effect(value(c),1)
		problem.add_action(increment)


		decrement = InstantaneousAction("decrement", c = obj)
		c = decrement.parameter("c")
		increment.add_precondition(GE(value(c),1))
		increment.add_decrease_effect(value(c),1)
		problem.add_action(decrement)


		#initial values
		problem.set_initial_value(value(c0),0)
		problem.set_initial_value(value(c0),0)
		problem.set_initial_value(max_int,4)


		#goals
		problem.add_goal(LT(value(c0),value(c1)))

		return problem
	
	def get_description(self):
		return 'just some integer values'

	def version(self):
		return 1


class fn_counters_4(TestCaseProblem):
	
	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		obj = UserType("Obj")
		c1 = unified_planning.model.Object("c1",obj)
		c0 = unified_planning.model.Object("c0",obj)
		c2 = unified_planning.model.Object("c2",obj)
		c3 = unified_planning.model.Object("c3",obj)

		problem = Problem("fn-counters")
		problem.add_objects([c0,c1,c2,c3])

		#fluents
		value = Fluent("value",IntType(), o = obj)
		problem.add_fluent(value,default_initial_value=0)
		max_int = Fluent("max_int",IntType())
		problem.add_fluent(max_int,default_initial_value=1)

		#actions
		increment = InstantaneousAction("increment", c = obj)
		c = increment.parameter("c")
		increment.add_precondition(LT(value(c),max_int))
		increment.add_increase_effect(value(c),1)
		problem.add_action(increment)


		decrement = InstantaneousAction("decrement", c = obj)
		c = decrement.parameter("c")
		increment.add_precondition(GE(value(c),1))
		increment.add_decrease_effect(value(c),1)
		problem.add_action(decrement)


		#initial values
		problem.set_initial_value(value(c0),0)
		problem.set_initial_value(value(c0),0)
		problem.set_initial_value(max_int,8)


		#goals
		problem.add_goal(LT(value(c0),value(c1)))
		problem.add_goal(LT(value(c1),value(c2)))
		problem.add_goal(LT(value(c2),value(c3)))

		return problem
	
	def get_description(self):
		return 'just some integer values'

	def version(self):
		return 1





	