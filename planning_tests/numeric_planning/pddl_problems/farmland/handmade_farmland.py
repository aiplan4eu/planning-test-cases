

import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem


class farmland_2_100_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)
		
	def get_problem(self):

		farm = UserType("farm")
		f0 = unified_planning.model.Object("f0",farm)
		f1 = unified_planning.model.Object("f1",farm)

		problem = Problem("farmland")
		problem.add_objects([f0,f1])

		#fluents
		x = Fluent('x', IntType(), o=farm)
		problem.add_fluent(x, default_initial_value=0)
		cost = Fluent("cost",IntType())
		problem.add_fluent(cost,default_initial_value=0)
		adj = Fluent("adj",IntType(),f01 = farm, f02 = farm)
		problem.add_fluent(adj,default_initial_value=0)


		#actions
		move_fast = InstantaneousAction("move_fast",f01 = farm, f02 = farm)
		f01 = move_fast.parameter("f01")
		f02 = move_fast.parameter("f02")
		move_fast.add_precondition(Not(Equals(f01,f02)))
		move_fast.add_precondition(GE(x(f01),4))
		move_fast.add_precondition(Equals(adj(f01,f02),1))
		move_fast.add_decrease_effect(x(f01),4)
		move_fast.add_increase_effect(x(f02),2)
		move_fast.add_increase_effect(cost,1)
		problem.add_action(move_fast)


		move_slow = InstantaneousAction("move_slow",f01 = farm, f02 = farm)
		f01 = move_slow.parameter("f01")
		f02 = move_slow.parameter("f02")
		move_slow.add_precondition(Not(Equals(f01,f02)))
		move_slow.add_precondition(GE(x(f01),1))
		move_slow.add_precondition(Equals(adj(f01,f02),1))
		move_slow.add_decrease_effect(x(f01),1)
		move_slow.add_increase_effect(x(f02),1)
		problem.add_action(move_slow)

		#intial values
		problem.set_initial_value(x(f0),100)
		problem.set_initial_value(x(f1),1)
		problem.set_initial_value(adj(f0,f1),1)
		problem.set_initial_value(adj(f1,f0),1)

		#goals
		problem.add_goal(GE(x(f0),1))
		problem.add_goal(GE(x(f1),1))
		problem.add_goal(GE(Plus(Times(1.0,x(f0)),Plus(Times(1.7,x(f1)),0)),140))

		return problem
	
	def get_description(self):
		return 'farming is important and it will ever be'

	def version(self):
		return 1

class farmland_2_200_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)
		
	def get_problem(self):

		farm = UserType("farm")
		f0 = unified_planning.model.Object("f0",farm)
		f1 = unified_planning.model.Object("f1",farm)

		problem = Problem("farmland")
		problem.add_objects([f0,f1])

		#fluents
		x = Fluent('x', IntType(), o=farm)
		problem.add_fluent(x, default_initial_value=0)
		cost = Fluent("cost",IntType())
		problem.add_fluent(cost,default_initial_value=0)
		adj = Fluent("adj",IntType(),f01 = farm, f02 = farm)
		problem.add_fluent(adj,default_initial_value=0)


		#actions
		move_fast = InstantaneousAction("move_fast",f01 = farm, f02 = farm)
		f01 = move_fast.parameter("f01")
		f02 = move_fast.parameter("f02")
		move_fast.add_precondition(Not(Equals(f01,f02)))
		move_fast.add_precondition(GE(x(f01),4))
		move_fast.add_precondition(Equals(adj(f01,f02),1))
		move_fast.add_decrease_effect(x(f01),4)
		move_fast.add_increase_effect(x(f02),2)
		move_fast.add_increase_effect(cost,1)
		problem.add_action(move_fast)


		move_slow = InstantaneousAction("move_slow",f01 = farm, f02 = farm)
		f01 = move_slow.parameter("f01")
		f02 = move_slow.parameter("f02")
		move_slow.add_precondition(Not(Equals(f01,f02)))
		move_slow.add_precondition(GE(x(f01),1))
		move_slow.add_precondition(Equals(adj(f01,f02),1))
		move_slow.add_decrease_effect(x(f01),1)
		move_slow.add_increase_effect(x(f02),1)
		problem.add_action(move_slow)

		#intial values
		problem.set_initial_value(x(f0),200)
		problem.set_initial_value(x(f1),1)
		problem.set_initial_value(adj(f0,f1),1)
		problem.set_initial_value(adj(f1,f0),1)

		#goals
		problem.add_goal(GE(x(f0),1))
		problem.add_goal(GE(x(f1),1))
		problem.add_goal(GE(Plus(Times(1.0,x(f0)),Plus(Times(1.7,x(f1)),0)),280))

		return problem
	
	def get_description(self):
		return 'farming is important and it will ever be'

	def version(self):
		return 1
		

class farmland_2_300_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)
		
	def get_problem(self):

		farm = UserType("farm")
		f0 = unified_planning.model.Object("f0",farm)
		f1 = unified_planning.model.Object("f1",farm)

		problem = Problem("farmland")
		problem.add_objects([f0,f1])

		#fluents
		x = Fluent('x', IntType(), o=farm)
		problem.add_fluent(x, default_initial_value=0)
		cost = Fluent("cost",IntType())
		problem.add_fluent(cost,default_initial_value=0)
		adj = Fluent("adj",IntType(),f01 = farm, f02 = farm)
		problem.add_fluent(adj,default_initial_value=0)


		#actions
		move_fast = InstantaneousAction("move_fast",f01 = farm, f02 = farm)
		f01 = move_fast.parameter("f01")
		f02 = move_fast.parameter("f02")
		move_fast.add_precondition(Not(Equals(f01,f02)))
		move_fast.add_precondition(GE(x(f01),4))
		move_fast.add_precondition(Equals(adj(f01,f02),1))
		move_fast.add_decrease_effect(x(f01),4)
		move_fast.add_increase_effect(x(f02),2)
		move_fast.add_increase_effect(cost,1)
		problem.add_action(move_fast)


		move_slow = InstantaneousAction("move_slow",f01 = farm, f02 = farm)
		f01 = move_slow.parameter("f01")
		f02 = move_slow.parameter("f02")
		move_slow.add_precondition(Not(Equals(f01,f02)))
		move_slow.add_precondition(GE(x(f01),1))
		move_slow.add_precondition(Equals(adj(f01,f02),1))
		move_slow.add_decrease_effect(x(f01),1)
		move_slow.add_increase_effect(x(f02),1)
		problem.add_action(move_slow)

		#intial values
		problem.set_initial_value(x(f0),300)
		problem.set_initial_value(x(f1),1)
		problem.set_initial_value(adj(f0,f1),1)
		problem.set_initial_value(adj(f1,f0),1)

		#goals
		problem.add_goal(GE(x(f0),1))
		problem.add_goal(GE(x(f1),1))
		problem.add_goal(GE(Plus(Times(1.0,x(f0)),Plus(Times(1.7,x(f1)),0)),420))

		return problem
	
	def get_description(self):
		return 'farming is important and it will ever be'

	def version(self):
		return 1
