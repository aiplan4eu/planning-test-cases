
import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem

class blocksworld_5_5_2_1(TestCaseProblem):

	def __init__(self, expected_version):
			TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		#objects
		obj = UserType('Obj')
		b1 = unified_planning.model.Object("b1",obj)
		b2 = unified_planning.model.Object("b2",obj)
		b3 = unified_planning.model.Object("b3",obj)
		b4 = unified_planning.model.Object("b4",obj)
		b5 = unified_planning.model.Object("b5",obj)

		problem = Problem("block-grouping")
		problem.add_objects([b1,b2,b3,b4,b5])

		#fluents
		x = Fluent('x', IntType(), o=obj)
		y = Fluent('y',IntType(),o = obj)
		problem.add_fluent(x, default_initial_value=1)
		problem.add_fluent(y, default_initial_value=1)
		maxx = Fluent('maxx',IntType())
		problem.add_fluent(maxx, default_initial_value=1)
		maxy = Fluent('maxy',IntType())
		problem.add_fluent(maxy, default_initial_value=1)
		minx = Fluent('minx',IntType())
		problem.add_fluent(minx, default_initial_value=1)
		miny = Fluent('miny',IntType())
		problem.add_fluent(miny, default_initial_value=1)

		#actions
		move_up = InstantaneousAction('move_up',p1=obj)
		p1 = move_up.parameter('p1')
		move_up.add_precondition(LT(y(p1), maxy))
		move_up.add_increase_effect(y(p1),1)
		problem.add_action(move_up)

		move_down = InstantaneousAction('move_down',p1=obj)
		p1 = move_down.parameter("p1")
		move_down.add_precondition(GT(y(p1), miny))
		move_down.add_decrease_effect(y(p1),1)
		problem.add_action(move_down)

		move_right = InstantaneousAction("move_right",p1=obj)
		p1 = move_right.parameter('p1')
		move_right.add_precondition(LT(x(p1), maxx))
		move_right.add_increase_effect(x(p1),1)
		problem.add_action(move_right)

		move_left = InstantaneousAction("move_left",p1 = obj)
		p1 = move_left.parameter('p1')
		move_left.add_precondition(GT(x(p1), minx))
		move_left.add_decrease_effect(x(p1),1)
		problem.add_action(move_left)


		#initial values
		problem.set_initial_value(x(b3),1)
		problem.set_initial_value(y(b3),3)
		problem.set_initial_value(x(b4),3)
		problem.set_initial_value(y(b4),4)
		problem.set_initial_value(x(b2),2)
		problem.set_initial_value(y(b2),2)
		problem.set_initial_value(x(b1),5)
		problem.set_initial_value(y(b1),1)
		problem.set_initial_value(x(b5),5)
		problem.set_initial_value(y(b5),5)
		problem.set_initial_value(maxx,5)
		problem.set_initial_value(minx,1)
		problem.set_initial_value(maxy,5)
		problem.set_initial_value(miny,1)

		#goals
		problem.add_goal(Or(Not(Equals(x(b1),x(b2))),Not(Equals(y(b1),y(b2)))))
		problem.add_goal(Equals(x(b1),x(b3)))
		problem.add_goal(Equals(y(b1),y(b3)))
		problem.add_goal(Or(Not(Equals(x(b1),x(b4))),Not(Equals(y(b1),y(b4)))))
		problem.add_goal(Equals(x(b1),x(b5)))
		problem.add_goal(Equals(y(b1),y(b5)))
		problem.add_goal(Or(Not(Equals(x(b2),x(b3))),Not(Equals(y(b2),y(b3)))))
		problem.add_goal(Equals(x(b2),x(b4)))
		problem.add_goal(Equals(y(b2),y(b4)))
		problem.add_goal(Or(Not(Equals(x(b2),x(b5))),Not(Equals(y(b2),y(b5)))))
		problem.add_goal(Or(Not(Equals(x(b3),x(b4))),Not(Equals(y(b3),y(b4)))))
		problem.add_goal(Equals(x(b3),x(b5)))
		problem.add_goal(Equals(y(b3),y(b5)))
		problem.add_goal(Or(Not(Equals(x(b4),x(b5))),Not(Equals(y(b4),y(b5)))))

		return problem
	
	def get_description(self):
		return 'a world made of blocks'

	def version(self):
		return 1

class blocksworld_5_5_2_2(TestCaseProblem):

	def __init__(self, expected_version):
			TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		#objects
		obj = UserType('Obj')
		b1 = unified_planning.model.Object("b1",obj)
		b2 = unified_planning.model.Object("b2",obj)
		b3 = unified_planning.model.Object("b3",obj)
		b4 = unified_planning.model.Object("b4",obj)
		b5 = unified_planning.model.Object("b5",obj)

		problem = Problem("blocksworld")
		problem.add_objects([b1,b2,b3,b4,b5])

		#fluents
		x = Fluent('x', IntType(), o=obj)
		y = Fluent('y',IntType(),o = obj)
		problem.add_fluent(x, default_initial_value=1)
		problem.add_fluent(y, default_initial_value=1)
		maxx = Fluent('maxx',IntType())
		problem.add_fluent(maxx, default_initial_value=1)
		maxy = Fluent('maxy',IntType())
		problem.add_fluent(maxy, default_initial_value=1)
		minx = Fluent('minx',IntType())
		problem.add_fluent(minx, default_initial_value=1)
		miny = Fluent('miny',IntType())
		problem.add_fluent(miny, default_initial_value=1)

		#actions
		move_up = InstantaneousAction('move_up',p1=obj)
		p1 = move_up.parameter('p1')
		move_up.add_precondition(LT(y(p1), maxy))
		move_up.add_increase_effect(y(p1),1)
		problem.add_action(move_up)

		move_down = InstantaneousAction('move_down',p1=obj)
		p1 = move_down.parameter("p1")
		move_down.add_precondition(GT(y(p1), miny))
		move_down.add_decrease_effect(y(p1),1)
		problem.add_action(move_down)

		move_right = InstantaneousAction("move_right",p1=obj)
		p1 = move_right.parameter('p1')
		move_right.add_precondition(LT(x(p1), maxx))
		move_right.add_increase_effect(x(p1),1)
		problem.add_action(move_right)

		move_left = InstantaneousAction("move_left",p1 = obj)
		p1 = move_left.parameter('p1')
		move_left.add_precondition(GT(x(p1), minx))
		move_left.add_decrease_effect(x(p1),1)
		problem.add_action(move_left)


		#initial values
		problem.set_initial_value(x(b3),2)
		problem.set_initial_value(y(b3),1)
		problem.set_initial_value(x(b4),2)
		problem.set_initial_value(y(b4),2)
		problem.set_initial_value(x(b2),5)
		problem.set_initial_value(y(b2),1)
		problem.set_initial_value(x(b1),4)
		problem.set_initial_value(y(b1),5)
		problem.set_initial_value(x(b5),3)
		problem.set_initial_value(y(b5),2)
		problem.set_initial_value(maxx,5)
		problem.set_initial_value(minx,1)
		problem.set_initial_value(maxy,5)
		problem.set_initial_value(miny,1)

		#goals
		problem.add_goal(Or(Not(Equals(x(b1),x(b2))),Not(Equals(y(b1),y(b2)))))
		problem.add_goal(Equals(x(b1),x(b4)))
		problem.add_goal(Equals(y(b1),y(b4)))
		problem.add_goal(Or(Not(Equals(x(b1),x(b3))),Not(Equals(y(b1),y(b3)))))
		problem.add_goal(Equals(x(b1),x(b5)))
		problem.add_goal(Equals(y(b1),y(b5)))
		problem.add_goal(Or(Not(Equals(x(b2),x(b4))),Not(Equals(y(b2),y(b4)))))
		problem.add_goal(Equals(x(b2),x(b3)))
		problem.add_goal(Equals(y(b2),y(b3)))
		problem.add_goal(Or(Not(Equals(x(b2),x(b5))),Not(Equals(y(b2),y(b5)))))
		problem.add_goal(Or(Not(Equals(x(b3),x(b4))),Not(Equals(y(b3),y(b4)))))
		problem.add_goal(Equals(x(b4),x(b5)))
		problem.add_goal(Equals(y(b4),y(b5)))
		problem.add_goal(Or(Not(Equals(x(b3),x(b5))),Not(Equals(y(b3),y(b5)))))

		return problem
	
	def get_description(self):
		return 'a world made of blocks'

	def version(self):
		return 1


class blocksworld_5_5_2_3(TestCaseProblem):

	def __init__(self, expected_version):
			TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		#objects
		obj = UserType('Obj')
		b1 = unified_planning.model.Object("b1",obj)
		b2 = unified_planning.model.Object("b2",obj)
		b3 = unified_planning.model.Object("b3",obj)
		b4 = unified_planning.model.Object("b4",obj)
		b5 = unified_planning.model.Object("b5",obj)

		problem = Problem("blocksworld")
		problem.add_objects([b1,b2,b3,b4,b5])

		#fluents
		x = Fluent('x', IntType(), o=obj)
		y = Fluent('y',IntType(),o = obj)
		problem.add_fluent(x, default_initial_value=1)
		problem.add_fluent(y, default_initial_value=1)
		maxx = Fluent('maxx',IntType())
		problem.add_fluent(maxx, default_initial_value=1)
		maxy = Fluent('maxy',IntType())
		problem.add_fluent(maxy, default_initial_value=1)
		minx = Fluent('minx',IntType())
		problem.add_fluent(minx, default_initial_value=1)
		miny = Fluent('miny',IntType())
		problem.add_fluent(miny, default_initial_value=1)

		#actions
		move_up = InstantaneousAction('move_up',p1=obj)
		p1 = move_up.parameter('p1')
		move_up.add_precondition(LT(y(p1), maxy))
		move_up.add_increase_effect(y(p1),1)
		problem.add_action(move_up)

		move_down = InstantaneousAction('move_down',p1=obj)
		p1 = move_down.parameter("p1")
		move_down.add_precondition(GT(y(p1), miny))
		move_down.add_decrease_effect(y(p1),1)
		problem.add_action(move_down)

		move_right = InstantaneousAction("move_right",p1=obj)
		p1 = move_right.parameter('p1')
		move_right.add_precondition(LT(x(p1), maxx))
		move_right.add_increase_effect(x(p1),1)
		problem.add_action(move_right)

		move_left = InstantaneousAction("move_left",p1 = obj)
		p1 = move_left.parameter('p1')
		move_left.add_precondition(GT(x(p1), minx))
		move_left.add_decrease_effect(x(p1),1)
		problem.add_action(move_left)


		#initial values
		problem.set_initial_value(x(b3),4)
		problem.set_initial_value(y(b3),3)
		problem.set_initial_value(x(b4),1)
		problem.set_initial_value(y(b4),4)
		problem.set_initial_value(x(b2),4)
		problem.set_initial_value(y(b2),5)
		problem.set_initial_value(x(b1),2)
		problem.set_initial_value(y(b1),3)
		problem.set_initial_value(x(b5),1)
		problem.set_initial_value(y(b5),4)
		problem.set_initial_value(maxx,5)
		problem.set_initial_value(minx,1)
		problem.set_initial_value(maxy,5)
		problem.set_initial_value(miny,1)

		#goals
		
		problem.add_goal(Equals(x(b1),x(b2)))
		problem.add_goal(Equals(y(b1),y(b2)))
		problem.add_goal(Equals(x(b1),x(b3)))
		problem.add_goal(Equals(y(b1),y(b3)))
		problem.add_goal(Equals(x(b1),x(b4)))
		problem.add_goal(Equals(y(b1),y(b4)))
		problem.add_goal(Equals(x(b1),x(b5)))
		problem.add_goal(Equals(y(b1),y(b5)))
		problem.add_goal(Equals(x(b2),x(b3)))
		problem.add_goal(Equals(y(b2),y(b3)))
		problem.add_goal(Equals(x(b2),x(b4)))
		problem.add_goal(Equals(y(b2),y(b4)))
		problem.add_goal(Equals(x(b2),x(b5)))
		problem.add_goal(Equals(y(b2),y(b5)))
		problem.add_goal(Equals(x(b3),x(b4)))
		problem.add_goal(Equals(y(b3),y(b4)))
		problem.add_goal(Equals(x(b3),x(b5)))
		problem.add_goal(Equals(y(b3),y(b5)))
		problem.add_goal(Equals(x(b4),x(b5)))
		problem.add_goal(Equals(y(b4),y(b5)))
	

		return problem
	
	def get_description(self):
		return 'a world made of blocks'

	def version(self):
		return 1