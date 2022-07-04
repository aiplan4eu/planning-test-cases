

import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem


class sailing_1_1_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)
		
	def get_problem(self):

		b = UserType('b')
		p = UserType('p')

		p0 = unified_planning.model.Object("p0",p)
		b0 = unified_planning.model.Object("b0",b)

		problem = Problem("sailing")
		problem.add_objects([b0,p0])

		#fluents
		x = Fluent('x', IntType(), o=b)
		problem.add_fluent(x, default_initial_value=0)
		y = Fluent('y', IntType(), o=b)
		problem.add_fluent(y, default_initial_value=0)
		d = Fluent('d', IntType(), o = p)
		problem.add_fluent(d,default_initial_value=0)

		#actions
		go_north_east = InstantaneousAction('go_north_east',b01 = b)
		b01 = go_north_east.parameter("b01")
		go_north_east.add_increase_effect(x(b01),1.5)
		go_north_east.add_increase_effect(y(b01),1.5)
		problem.add_action(go_north_east)

		go_north_west = InstantaneousAction('go_north_west',b01 = b)
		b01 = go_north_west.parameter("b01")
		go_north_west.add_decrease_effect(x(b01),1.5)
		go_north_west.add_increase_effect(y(b01),1.5)
		problem.add_action(go_north_west)









		return problem
	
	def get_description(self):
		return 'farming is important and it will ever be'

	def version(self):
		return 1