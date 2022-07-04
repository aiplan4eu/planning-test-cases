
import unified_planning
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem


class plant_watering_4_1(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)
		
	def get_problem(self):
		obj = UserType('Obj')
		plant = UserType('plant')
		p1 = unified_planning.model.Object('p1', plant)
		p2 = unified_planning.model.Object('p2', plant)
		p3 = unified_planning.model.Object('p3', plant)
		p4 = unified_planning.model.Object('p4', plant)
		tap = unified_planning.model.Object('tap', obj)
		agent = unified_planning.model.Object('agent', obj)

		problem = Problem("plant_watering")
		problem.add_objects([p1,p2,p3,p4,agent,tap])

		
		x = Fluent('x', IntType(), o = obj)
		y = Fluent('y',IntType(),o = obj)
		xp = Fluent('xp', IntType(),p = plant)
		yp = Fluent('yp',IntType(),p = plant)
		problem.add_fluent(x, default_initial_value=1)
		problem.add_fluent(y, default_initial_value=1)
		problem.add_fluent(xp, default_initial_value=1)
		problem.add_fluent(yp, default_initial_value=1)
		carrying = Fluent('carrying',IntType())
		problem.add_fluent(carrying, default_initial_value=0)
		poured = Fluent('poured',IntType(), p = plant)
		problem.add_fluent(poured, default_initial_value=0)
		total_poured = Fluent('total_poured',IntType())
		problem.add_fluent(total_poured, default_initial_value=0)
		total_loaded = Fluent('total_loaded',IntType())
		problem.add_fluent(total_loaded, default_initial_value=0)
		max_int = Fluent('max_int',IntType())
		problem.add_fluent(max_int, default_initial_value=1)
		maxx = Fluent('maxx',IntType())
		problem.add_fluent(maxx, default_initial_value=1)
		maxy = Fluent('maxy',IntType())
		problem.add_fluent(maxy, default_initial_value=1)
		minx = Fluent('minx',IntType())
		problem.add_fluent(minx, default_initial_value=1)
		miny = Fluent('miny',IntType())
		problem.add_fluent(miny, default_initial_value=1)

		#actions
		move_up = InstantaneousAction('move_up')
		move_up.add_precondition(LT(y(agent), maxy))
		move_up.add_increase_effect(y(agent),1)
		problem.add_action(move_up)

		move_down = InstantaneousAction('move_down')
		move_down.add_precondition(GT(y(agent), miny))
		move_down.add_decrease_effect(y(agent),1)
		problem.add_action(move_down)

		move_right = InstantaneousAction("move_right")
		move_right.add_precondition(LT(x(agent), maxx))
		move_right.add_increase_effect(x(agent),1)
		problem.add_action(move_right)

		move_left = InstantaneousAction("move_left")
		move_left.add_precondition(GT(x(agent), minx))
		move_left.add_decrease_effect(x(agent),1)
		problem.add_action(move_left)

		move_up_left = InstantaneousAction("move_up_left")
		move_up_left.add_precondition(GT(x(agent), minx))
		move_up_left.add_precondition(LT(y(agent), maxy))
		move_up_left.add_increase_effect(y(agent),1)
		move_up_left.add_decrease_effect(x(agent),1)
		problem.add_action(move_up_left)

		move_up_right = InstantaneousAction("move_up_right")
		move_up_right.add_precondition(LT(x(agent), maxx))
		move_up_right.add_precondition(LT(y(agent), maxy))
		move_up_right.add_increase_effect(y(agent),1)
		move_up_right.add_increase_effect(x(agent),1)
		problem.add_action(move_up_right)

		move_down_left = InstantaneousAction("move_down_left")
		move_down_left.add_precondition(GT(x(agent), minx))
		move_down_left.add_precondition(GT(y(agent), miny))
		move_down_left.add_decrease_effect(y(agent),1)
		move_down_left.add_decrease_effect(x(agent),1)
		problem.add_action(move_down_left)

		move_down_right = InstantaneousAction("move_down_right")
		move_down_right.add_precondition(LT(x(agent), maxx))
		move_down_right.add_precondition(GT(y(agent), miny))
		move_down_right.add_increase_effect(y(agent),1)
		move_down_right.add_decrease_effect(x(agent),1)
		problem.add_action(move_down_right)



		load = InstantaneousAction("load")
		load.add_precondition(And(Equals(x(agent),x(tap)),Equals(y(agent),y(tap)),LT(total_loaded,max_int),LT(carrying,max_int)))
		load.add_increase_effect(total_loaded,1)
		load.add_increase_effect(carrying,1)
		problem.add_action(load)

		pour = InstantaneousAction("pour", p = plant)
		p = pour.parameter("p")
		pour.add_precondition(And(Equals(x(agent),xp(p)),Equals(y(agent),yp(p)),GE(carrying,1),LE(total_poured,max_int),LE(poured(p),max_int)))
		pour.add_increase_effect(total_poured,1)
		pour.add_increase_effect(poured(p),1)
		pour.add_decrease_effect(carrying,1)
		problem.add_action(pour)



		#valori iniziali
		problem.set_initial_value(max_int,80)
		problem.set_initial_value(maxx,4)
		problem.set_initial_value(maxy,4)
		problem.set_initial_value(minx,1)
		problem.set_initial_value(miny,1)
		problem.set_initial_value(x(agent),3)
		problem.set_initial_value(y(agent),1)
		problem.set_initial_value(xp(p1),2)
		problem.set_initial_value(yp(p1),2)
		problem.set_initial_value(xp(p2),2)
		problem.set_initial_value(yp(p2),2)
		problem.set_initial_value(xp(p3),1)
		problem.set_initial_value(xp(p3),1)
		problem.set_initial_value(x(tap),3)
		problem.set_initial_value(y(tap),3)


		#goal del problema
		problem.add_goal(And(Equals(poured(p1),4),Equals(poured(p2),2),Equals(poured(p3),7),Equals(poured(p4),9)))
		problem.add_goal(Equals(total_poured,Plus(poured(p1),Plus(poured(p2),Plus(poured(p3),poured(p4))))))
		
		return problem
	
	def get_description(self):
		return 'time to water those plants'

	def version(self):
		return 1


class plant_watering_4_2(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)
		
	def get_problem(self):
		obj = UserType('Obj')
		p1 = unified_planning.model.Object('p1', obj)
		p2 = unified_planning.model.Object('p2', obj)
		p3 = unified_planning.model.Object('p3', obj)
		p4 = unified_planning.model.Object('p4', obj)
		tap = unified_planning.model.Object('tap', obj)
		agent = unified_planning.model.Object('agent', obj)

		problem = Problem("plant_watering")
		problem.add_objects([p1,p2,p3,p4,agent,tap])

		
		x = Fluent('x', IntType(), o=obj)
		y = Fluent('y',IntType(),o = obj)
		problem.add_fluent(x, default_initial_value=1)
		problem.add_fluent(y, default_initial_value=1)
		carrying = Fluent('carrying',IntType())
		problem.add_fluent(carrying, default_initial_value=0)
		poured = Fluent('poured',IntType(), o = obj)
		problem.add_fluent(poured, default_initial_value=0)
		total_poured = Fluent('total_poured',IntType())
		problem.add_fluent(total_poured, default_initial_value=0)
		total_loaded = Fluent('total_loaded',IntType())
		problem.add_fluent(total_loaded, default_initial_value=0)
		max_int = Fluent('max_int',IntType())
		problem.add_fluent(max_int, default_initial_value=1)
		maxx = Fluent('maxx',IntType())
		problem.add_fluent(maxx, default_initial_value=1)
		maxy = Fluent('maxy',IntType())
		problem.add_fluent(maxy, default_initial_value=1)
		minx = Fluent('minx',IntType())
		problem.add_fluent(minx, default_initial_value=1)
		miny = Fluent('miny',IntType())
		problem.add_fluent(miny, default_initial_value=1)

		#actions
		move_up = InstantaneousAction('move_up')
		move_up.add_precondition(LT(y(agent), maxy))
		move_up.add_increase_effect(y(agent),1)
		problem.add_action(move_up)

		move_down = InstantaneousAction('move_down')
		move_down.add_precondition(GT(y(agent), miny))
		move_down.add_decrease_effect(y(agent),1)
		problem.add_action(move_down)

		move_right = InstantaneousAction("move_right")
		move_right.add_precondition(LT(x(agent), maxx))
		move_right.add_increase_effect(x(agent),1)
		problem.add_action(move_right)

		move_left = InstantaneousAction("move_left")
		move_left.add_precondition(GT(x(agent), minx))
		move_left.add_decrease_effect(x(agent),1)
		problem.add_action(move_left)

		move_up_left = InstantaneousAction("move_up_left")
		move_up_left.add_precondition(GT(x(agent), minx))
		move_up_left.add_precondition(LT(y(agent), maxy))
		move_up_left.add_increase_effect(y(agent),1)
		move_up_left.add_decrease_effect(x(agent),1)
		problem.add_action(move_up_left)

		move_up_right = InstantaneousAction("move_up_right")
		move_up_right.add_precondition(LT(x(agent), maxx))
		move_up_right.add_precondition(LT(y(agent), maxy))
		move_up_right.add_increase_effect(y(agent),1)
		move_up_right.add_increase_effect(x(agent),1)
		problem.add_action(move_up_right)

		move_down_left = InstantaneousAction("move_down_left")
		move_down_left.add_precondition(GT(x(agent), minx))
		move_down_left.add_precondition(GT(y(agent), miny))
		move_down_left.add_decrease_effect(y(agent),1)
		move_down_left.add_decrease_effect(x(agent),1)
		problem.add_action(move_down_left)

		move_down_right = InstantaneousAction("move_down_right")
		move_down_right.add_precondition(LT(x(agent), maxx))
		move_down_right.add_precondition(GT(y(agent), miny))
		move_down_right.add_increase_effect(y(agent),1)
		move_down_right.add_decrease_effect(x(agent),1)
		problem.add_action(move_down_right)



		load = InstantaneousAction("load")
		load.add_precondition(And(Equals(x(agent),x(tap)),Equals(y(agent),y(tap)),LT(total_loaded,max_int),LT(carrying,max_int)))
		load.add_increase_effect(total_loaded,1)
		load.add_increase_effect(carrying,1)
		
	
		problem.add_action(load)

		pourp1 = InstantaneousAction("pourp1")
		pourp1.add_precondition(And(Equals(x(agent),x(p1)),Equals(y(agent),y(p1)),GE(carrying,1),LE(total_poured,max_int),LE(poured(p1),max_int)))
		pourp1.add_increase_effect(total_poured,1)
		pourp1.add_increase_effect(poured(p1),1)
		pourp1.add_decrease_effect(carrying,1)
		problem.add_action(pourp1)

		pourp2 = InstantaneousAction("pourp2")
		pourp2.add_precondition(And(Equals(x(agent),x(p2)),Equals(y(agent),y(p2)),GE(carrying,1),LE(total_poured,max_int),LE(poured(p2),max_int)))
		pourp2.add_increase_effect(total_poured,1)
		pourp2.add_increase_effect(poured(p2),1)
		pourp2.add_decrease_effect(carrying,1)
		problem.add_action(pourp2)

		pourp3 = InstantaneousAction("pourp3")
		pourp3.add_precondition(And(Equals(x(agent),x(p3)),Equals(y(agent),y(p3)),GE(carrying,1),LE(total_poured,max_int),LE(poured(p3),max_int)))
		pourp3.add_increase_effect(total_poured,1)
		pourp3.add_increase_effect(poured(p3),1)
		pourp3.add_decrease_effect(carrying,1)
		problem.add_action(pourp3)

		pourp4 = InstantaneousAction("pourp4")
		pourp4.add_precondition(And(Equals(x(agent),x(p4)),Equals(y(agent),y(p4)),GE(carrying,1),LE(total_poured,max_int),LE(poured(p4),max_int)))
		pourp4.add_increase_effect(total_poured,1)
		pourp4.add_increase_effect(poured(p4),1)
		pourp4.add_decrease_effect(carrying,1)
		problem.add_action(pourp4)


		#valori iniziali
		problem.set_initial_value(max_int,80)
		problem.set_initial_value(maxx,4)
		problem.set_initial_value(maxy,4)
		problem.set_initial_value(minx,1)
		problem.set_initial_value(miny,1)
		problem.set_initial_value(x(agent),4)
		problem.set_initial_value(y(agent),1)
		problem.set_initial_value(x(p1),3)
		problem.set_initial_value(y(p1),3)
		problem.set_initial_value(x(p2),1)
		problem.set_initial_value(y(p2),1)
		problem.set_initial_value(x(p3),1)
		problem.set_initial_value(x(p3),1)
		problem.set_initial_value(x(tap),3)
		problem.set_initial_value(y(tap),3)
		problem.set_initial_value(y(p4),4)
		problem.set_initial_value(x(p4),4)


		#goal del problema
		problem.add_goal(And(Equals(poured(p1),10),Equals(poured(p2),3),Equals(poured(p3),4),Equals(poured(p4),6)))
		problem.add_goal(Equals(total_poured,Plus(poured(p1),Plus(poured(p2),Plus(poured(p3),poured(p4))))))
		
		return problem
	
	def get_description(self):
		return 'time to water those plants'

	def version(self):
		return 1


class plant_watering_4_3(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)
		
	def get_problem(self):
		obj = UserType('Obj')
		p1 = unified_planning.model.Object('p1', obj)
		p2 = unified_planning.model.Object('p2', obj)
		p3 = unified_planning.model.Object('p3', obj)
		p4 = unified_planning.model.Object('p4', obj)
		tap = unified_planning.model.Object('tap', obj)
		agent = unified_planning.model.Object('agent', obj)

		problem = Problem("plant_watering")
		problem.add_objects([p1,p2,p3,p4,agent,tap])

		
		x = Fluent('x', IntType(), o=obj)
		y = Fluent('y',IntType(),o = obj)
		problem.add_fluent(x, default_initial_value=1)
		problem.add_fluent(y, default_initial_value=1)
		carrying = Fluent('carrying',IntType())
		problem.add_fluent(carrying, default_initial_value=0)
		poured = Fluent('poured',IntType(), o = obj)
		problem.add_fluent(poured, default_initial_value=0)
		total_poured = Fluent('total_poured',IntType())
		problem.add_fluent(total_poured, default_initial_value=0)
		total_loaded = Fluent('total_loaded',IntType())
		problem.add_fluent(total_loaded, default_initial_value=0)
		max_int = Fluent('max_int',IntType())
		problem.add_fluent(max_int, default_initial_value=1)
		maxx = Fluent('maxx',IntType())
		problem.add_fluent(maxx, default_initial_value=1)
		maxy = Fluent('maxy',IntType())
		problem.add_fluent(maxy, default_initial_value=1)
		minx = Fluent('minx',IntType())
		problem.add_fluent(minx, default_initial_value=1)
		miny = Fluent('miny',IntType())
		problem.add_fluent(miny, default_initial_value=1)

		#actions
		move_up = InstantaneousAction('move_up')
		move_up.add_precondition(LT(y(agent), maxy))
		move_up.add_increase_effect(y(agent),1)
		problem.add_action(move_up)

		move_down = InstantaneousAction('move_down')
		move_down.add_precondition(GT(y(agent), miny))
		move_down.add_decrease_effect(y(agent),1)
		problem.add_action(move_down)

		move_right = InstantaneousAction("move_right")
		move_right.add_precondition(LT(x(agent), maxx))
		move_right.add_increase_effect(x(agent),1)
		problem.add_action(move_right)

		move_left = InstantaneousAction("move_left")
		move_left.add_precondition(GT(x(agent), minx))
		move_left.add_decrease_effect(x(agent),1)
		problem.add_action(move_left)

		move_up_left = InstantaneousAction("move_up_left")
		move_up_left.add_precondition(GT(x(agent), minx))
		move_up_left.add_precondition(LT(y(agent), maxy))
		move_up_left.add_increase_effect(y(agent),1)
		move_up_left.add_decrease_effect(x(agent),1)
		problem.add_action(move_up_left)

		move_up_right = InstantaneousAction("move_up_right")
		move_up_right.add_precondition(LT(x(agent), maxx))
		move_up_right.add_precondition(LT(y(agent), maxy))
		move_up_right.add_increase_effect(y(agent),1)
		move_up_right.add_increase_effect(x(agent),1)
		problem.add_action(move_up_right)

		move_down_left = InstantaneousAction("move_down_left")
		move_down_left.add_precondition(GT(x(agent), minx))
		move_down_left.add_precondition(GT(y(agent), miny))
		move_down_left.add_decrease_effect(y(agent),1)
		move_down_left.add_decrease_effect(x(agent),1)
		problem.add_action(move_down_left)

		move_down_right = InstantaneousAction("move_down_right")
		move_down_right.add_precondition(LT(x(agent), maxx))
		move_down_right.add_precondition(GT(y(agent), miny))
		move_down_right.add_increase_effect(y(agent),1)
		move_down_right.add_decrease_effect(x(agent),1)
		problem.add_action(move_down_right)



		load = InstantaneousAction("load")
		load.add_precondition(And(Equals(x(agent),x(tap)),Equals(y(agent),y(tap)),LT(total_loaded,max_int),LT(carrying,max_int)))
		load.add_increase_effect(total_loaded,1)
		load.add_increase_effect(carrying,1)
		
	
		problem.add_action(load)

		pourp1 = InstantaneousAction("pourp1")
		pourp1.add_precondition(And(Equals(x(agent),x(p1)),Equals(y(agent),y(p1)),GE(carrying,1),LE(total_poured,max_int),LE(poured(p1),max_int)))
		pourp1.add_increase_effect(total_poured,1)
		pourp1.add_increase_effect(poured(p1),1)
		pourp1.add_decrease_effect(carrying,1)
		problem.add_action(pourp1)

		pourp2 = InstantaneousAction("pourp2")
		pourp2.add_precondition(And(Equals(x(agent),x(p2)),Equals(y(agent),y(p2)),GE(carrying,1),LE(total_poured,max_int),LE(poured(p2),max_int)))
		pourp2.add_increase_effect(total_poured,1)
		pourp2.add_increase_effect(poured(p2),1)
		pourp2.add_decrease_effect(carrying,1)
		problem.add_action(pourp2)

		pourp3 = InstantaneousAction("pourp3")
		pourp3.add_precondition(And(Equals(x(agent),x(p3)),Equals(y(agent),y(p3)),GE(carrying,1),LE(total_poured,max_int),LE(poured(p3),max_int)))
		pourp3.add_increase_effect(total_poured,1)
		pourp3.add_increase_effect(poured(p3),1)
		pourp3.add_decrease_effect(carrying,1)
		problem.add_action(pourp3)

		pourp4 = InstantaneousAction("pourp4")
		pourp4.add_precondition(And(Equals(x(agent),x(p4)),Equals(y(agent),y(p4)),GE(carrying,1),LE(total_poured,max_int),LE(poured(p4),max_int)))
		pourp4.add_increase_effect(total_poured,1)
		pourp4.add_increase_effect(poured(p4),1)
		pourp4.add_decrease_effect(carrying,1)
		problem.add_action(pourp4)


		#valori iniziali
		problem.set_initial_value(max_int,80)
		problem.set_initial_value(maxx,4)
		problem.set_initial_value(maxy,4)
		problem.set_initial_value(minx,1)
		problem.set_initial_value(miny,1)
		problem.set_initial_value(x(agent),1)
		problem.set_initial_value(y(agent),4)
		problem.set_initial_value(x(p1),3)
		problem.set_initial_value(y(p1),3)
		problem.set_initial_value(x(p2),4)
		problem.set_initial_value(y(p2),4)
		problem.set_initial_value(x(p3),4)
		problem.set_initial_value(x(p3),4)
		problem.set_initial_value(x(tap),1)
		problem.set_initial_value(y(tap),1)
		problem.set_initial_value(y(p4),3)
		problem.set_initial_value(x(p4),3)


		#goal del problema
		problem.add_goal(And(Equals(poured(p1),10),Equals(poured(p2),5),Equals(poured(p3),7),Equals(poured(p4),4)))
		problem.add_goal(Equals(total_poured,Plus(poured(p1),Plus(poured(p2),Plus(poured(p3),poured(p4))))))
		
		return problem
	
	def get_description(self):
		return 'time to water those plants'

	def version(self):
		return 1

