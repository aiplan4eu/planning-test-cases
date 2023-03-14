import pkg_resources
import unified_planning
from unified_planning.shortcuts import *
from planning_tests.commons.problem import TestCaseProblem
from fractions import Fraction
from collections import OrderedDict
import unified_planning as up

class sailing_1_2_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):
		env = up.environment.get_environment()
		emgr = env.expression_manager
		tm = env.type_manager
		type_person = tm.UserType("person")
		type_boat = tm.UserType("boat")
		fluent_saved = up.model.Fluent("saved", tm.BoolType(), _signature=OrderedDict([("t", type_person)]))
		fluent_x = up.model.Fluent("x", tm.RealType(None, None), _signature=OrderedDict([("b", type_boat)]))
		fluent_y = up.model.Fluent("y", tm.RealType(None, None), _signature=OrderedDict([("b", type_boat)]))
		fluent_d = up.model.Fluent("d", tm.RealType(None, None), _signature=OrderedDict([("t", type_person)]))
		object_b0 = up.model.Object("b0", type_boat)
		object_p0 = up.model.Object("p0", type_person)
		object_p1 = up.model.Object("p1", type_person)
		problem_initial_defaults = {}
		problem_initial_defaults[tm.BoolType()] = emgr.FALSE()
		problem = up.model.Problem("instance_1_2_1229", env, initial_defaults=problem_initial_defaults)
		problem.add_object(object_b0)
		problem.add_object(object_p0)
		problem.add_object(object_p1)
		problem.add_fluent(fluent_saved, default_initial_value=emgr.FALSE())
		problem.add_fluent(fluent_x)
		problem.add_fluent(fluent_y)
		problem.add_fluent(fluent_d)
		act_go_north_east = up.model.InstantaneousAction("go_north_east", _parameters=OrderedDict([("b", type_boat)]))
		act_go_north_east.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		act_go_north_east.add_increase_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		problem.add_action(act_go_north_east)
		act_go_north_west = up.model.InstantaneousAction("go_north_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_north_west.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		act_go_north_west.add_increase_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		problem.add_action(act_go_north_west)
		act_go_est = up.model.InstantaneousAction("go_est", _parameters=OrderedDict([("b", type_boat)]))
		act_go_est.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(3), condition=emgr.TRUE())
		problem.add_action(act_go_est)
		act_go_west = up.model.InstantaneousAction("go_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_west.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(3), condition=emgr.TRUE())
		problem.add_action(act_go_west)
		act_go_south_west = up.model.InstantaneousAction("go_south_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south_west.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		act_go_south_west.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south_west)
		act_go_south_east = up.model.InstantaneousAction("go_south_east", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south_east.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		act_go_south_east.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south_east)
		act_go_south = up.model.InstantaneousAction("go_south", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south)
		act_save_person = up.model.InstantaneousAction("save_person", _parameters=OrderedDict([("b", type_boat), ("t", type_person)]))
		act_save_person.add_precondition(emgr.And(emgr.LE(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Plus(fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))))), emgr.LE(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Minus(fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))))), emgr.LE(emgr.Plus(fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat)))), emgr.Plus(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Int(25))), emgr.LE(emgr.Minus(fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat)))), emgr.Plus(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Int(25)))))
		act_save_person.add_effect(fluent=fluent_saved(emgr.ParameterExp(up.model.Parameter("t", type_person))), value=emgr.TRUE(), condition=emgr.TRUE())
		problem.add_action(act_save_person)
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_b0)), emgr.Int(7))
		problem.set_initial_value(fluent_y(emgr.ObjectExp(object_b0)), emgr.Int(0))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p0)), emgr.Int(-370))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p1)), emgr.Int(-58))
		problem.add_goal(goal=emgr.And(fluent_saved(emgr.ObjectExp(object_p0)), fluent_saved(emgr.ObjectExp(object_p1))))

		return problem

	def get_description(self):
		return 'sailing'

	def version(self):
		return 1

class sailing_1_1_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):
		env = up.environment.get_environment()
		emgr = env.expression_manager
		tm = env.type_manager
		type_person = tm.UserType("person")
		type_boat = tm.UserType("boat")
		fluent_saved = up.model.Fluent("saved", tm.BoolType(), _signature=OrderedDict([("t", type_person)]))
		fluent_x = up.model.Fluent("x", tm.RealType(None, None), _signature=OrderedDict([("b", type_boat)]))
		fluent_y = up.model.Fluent("y", tm.RealType(None, None), _signature=OrderedDict([("b", type_boat)]))
		fluent_d = up.model.Fluent("d", tm.RealType(None, None), _signature=OrderedDict([("t", type_person)]))
		object_b0 = up.model.Object("b0", type_boat)
		object_p0 = up.model.Object("p0", type_person)
		problem_initial_defaults = {}
		problem_initial_defaults[tm.BoolType()] = emgr.FALSE()
		problem = up.model.Problem("instance_1_1_1229", env, initial_defaults=problem_initial_defaults)
		problem.add_object(object_b0)
		problem.add_object(object_p0)
		problem.add_fluent(fluent_saved, default_initial_value=emgr.FALSE())
		problem.add_fluent(fluent_x)
		problem.add_fluent(fluent_y)
		problem.add_fluent(fluent_d)
		act_go_north_east = up.model.InstantaneousAction("go_north_east", _parameters=OrderedDict([("b", type_boat)]))
		act_go_north_east.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		act_go_north_east.add_increase_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		problem.add_action(act_go_north_east)
		act_go_north_west = up.model.InstantaneousAction("go_north_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_north_west.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		act_go_north_west.add_increase_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		problem.add_action(act_go_north_west)
		act_go_est = up.model.InstantaneousAction("go_est", _parameters=OrderedDict([("b", type_boat)]))
		act_go_est.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(3), condition=emgr.TRUE())
		problem.add_action(act_go_est)
		act_go_west = up.model.InstantaneousAction("go_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_west.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(3), condition=emgr.TRUE())
		problem.add_action(act_go_west)
		act_go_south_west = up.model.InstantaneousAction("go_south_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south_west.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		act_go_south_west.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south_west)
		act_go_south_east = up.model.InstantaneousAction("go_south_east", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south_east.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		act_go_south_east.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south_east)
		act_go_south = up.model.InstantaneousAction("go_south", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south)
		act_save_person = up.model.InstantaneousAction("save_person", _parameters=OrderedDict([("b", type_boat), ("t", type_person)]))
		act_save_person.add_precondition(emgr.And(emgr.LE(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Plus(fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))))), emgr.LE(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Minus(fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))))), emgr.LE(emgr.Plus(fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat)))), emgr.Plus(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Int(25))), emgr.LE(emgr.Minus(fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat)))), emgr.Plus(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Int(25)))))
		act_save_person.add_effect(fluent=fluent_saved(emgr.ParameterExp(up.model.Parameter("t", type_person))), value=emgr.TRUE(), condition=emgr.TRUE())
		problem.add_action(act_save_person)
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_b0)), emgr.Int(3))
		problem.set_initial_value(fluent_y(emgr.ObjectExp(object_b0)), emgr.Int(0))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p0)), emgr.Int(-370))
		problem.add_goal(goal=fluent_saved(emgr.ObjectExp(object_p0)))


		return problem

	def get_description(self):
		return 'sailing'

	def version(self):
		return 1

class sailing_1_3_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):


		env = up.environment.get_environment()
		emgr = env.expression_manager
		tm = env.type_manager
		type_person = tm.UserType("person")
		type_boat = tm.UserType("boat")
		fluent_saved = up.model.Fluent("saved", tm.BoolType(), _signature=OrderedDict([("t", type_person)]))
		fluent_x = up.model.Fluent("x", tm.RealType(None, None), _signature=OrderedDict([("b", type_boat)]))
		fluent_y = up.model.Fluent("y", tm.RealType(None, None), _signature=OrderedDict([("b", type_boat)]))
		fluent_d = up.model.Fluent("d", tm.RealType(None, None), _signature=OrderedDict([("t", type_person)]))
		object_b0 = up.model.Object("b0", type_boat)
		object_p0 = up.model.Object("p0", type_person)
		object_p1 = up.model.Object("p1", type_person)
		object_p2 = up.model.Object("p2", type_person)
		problem_initial_defaults = {}
		problem_initial_defaults[tm.BoolType()] = emgr.FALSE()
		problem = up.model.Problem("instance_1_3_1229", env, initial_defaults=problem_initial_defaults)
		problem.add_object(object_b0)
		problem.add_object(object_p0)
		problem.add_object(object_p1)
		problem.add_object(object_p2)
		problem.add_fluent(fluent_saved, default_initial_value=emgr.FALSE())
		problem.add_fluent(fluent_x)
		problem.add_fluent(fluent_y)
		problem.add_fluent(fluent_d)
		act_go_north_east = up.model.InstantaneousAction("go_north_east", _parameters=OrderedDict([("b", type_boat)]))
		act_go_north_east.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		act_go_north_east.add_increase_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		problem.add_action(act_go_north_east)
		act_go_north_west = up.model.InstantaneousAction("go_north_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_north_west.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		act_go_north_west.add_increase_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		problem.add_action(act_go_north_west)
		act_go_est = up.model.InstantaneousAction("go_est", _parameters=OrderedDict([("b", type_boat)]))
		act_go_est.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(3), condition=emgr.TRUE())
		problem.add_action(act_go_est)
		act_go_west = up.model.InstantaneousAction("go_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_west.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(3), condition=emgr.TRUE())
		problem.add_action(act_go_west)
		act_go_south_west = up.model.InstantaneousAction("go_south_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south_west.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		act_go_south_west.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south_west)
		act_go_south_east = up.model.InstantaneousAction("go_south_east", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south_east.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		act_go_south_east.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south_east)
		act_go_south = up.model.InstantaneousAction("go_south", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south)
		act_save_person = up.model.InstantaneousAction("save_person", _parameters=OrderedDict([("b", type_boat), ("t", type_person)]))
		act_save_person.add_precondition(emgr.And(emgr.LE(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Plus(fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))))), emgr.LE(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Minus(fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))))), emgr.LE(emgr.Plus(fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat)))), emgr.Plus(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Int(25))), emgr.LE(emgr.Minus(fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat)))), emgr.Plus(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Int(25)))))
		act_save_person.add_effect(fluent=fluent_saved(emgr.ParameterExp(up.model.Parameter("t", type_person))), value=emgr.TRUE(), condition=emgr.TRUE())
		problem.add_action(act_save_person)
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_b0)), emgr.Int(-7))
		problem.set_initial_value(fluent_y(emgr.ObjectExp(object_b0)), emgr.Int(0))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p0)), emgr.Int(-370))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p1)), emgr.Int(-58))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p2)), emgr.Int(63))
		problem.add_goal(goal=emgr.And(fluent_saved(emgr.ObjectExp(object_p0)), fluent_saved(emgr.ObjectExp(object_p1)), fluent_saved(emgr.ObjectExp(object_p2))))

		return problem

	def get_description(self):
		return 'sailing'

	def version(self):
		return 1


class sailing_3_3_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		env = up.environment.get_environment()
		emgr = env.expression_manager
		tm = env.type_manager
		type_person = tm.UserType("person")
		type_boat = tm.UserType("boat")
		fluent_saved = up.model.Fluent("saved", tm.BoolType(), _signature=OrderedDict([("t", type_person)]))
		fluent_x = up.model.Fluent("x", tm.RealType(None, None), _signature=OrderedDict([("b", type_boat)]))
		fluent_y = up.model.Fluent("y", tm.RealType(None, None), _signature=OrderedDict([("b", type_boat)]))
		fluent_d = up.model.Fluent("d", tm.RealType(None, None), _signature=OrderedDict([("t", type_person)]))
		object_b0 = up.model.Object("b0", type_boat)
		object_b1 = up.model.Object("b1", type_boat)
		object_b2 = up.model.Object("b2", type_boat)
		object_p0 = up.model.Object("p0", type_person)
		object_p1 = up.model.Object("p1", type_person)
		object_p2 = up.model.Object("p2", type_person)
		problem_initial_defaults = {}
		problem_initial_defaults[tm.BoolType()] = emgr.FALSE()
		problem = up.model.Problem("instance_3_3_1229", env, initial_defaults=problem_initial_defaults)
		problem.add_object(object_b0)
		problem.add_object(object_b1)
		problem.add_object(object_b2)
		problem.add_object(object_p0)
		problem.add_object(object_p1)
		problem.add_object(object_p2)
		problem.add_fluent(fluent_saved, default_initial_value=emgr.FALSE())
		problem.add_fluent(fluent_x)
		problem.add_fluent(fluent_y)
		problem.add_fluent(fluent_d)
		act_go_north_east = up.model.InstantaneousAction("go_north_east", _parameters=OrderedDict([("b", type_boat)]))
		act_go_north_east.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		act_go_north_east.add_increase_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		problem.add_action(act_go_north_east)
		act_go_north_west = up.model.InstantaneousAction("go_north_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_north_west.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		act_go_north_west.add_increase_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		problem.add_action(act_go_north_west)
		act_go_est = up.model.InstantaneousAction("go_est", _parameters=OrderedDict([("b", type_boat)]))
		act_go_est.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(3), condition=emgr.TRUE())
		problem.add_action(act_go_est)
		act_go_west = up.model.InstantaneousAction("go_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_west.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(3), condition=emgr.TRUE())
		problem.add_action(act_go_west)
		act_go_south_west = up.model.InstantaneousAction("go_south_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south_west.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		act_go_south_west.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south_west)
		act_go_south_east = up.model.InstantaneousAction("go_south_east", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south_east.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		act_go_south_east.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south_east)
		act_go_south = up.model.InstantaneousAction("go_south", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south)
		act_save_person = up.model.InstantaneousAction("save_person", _parameters=OrderedDict([("b", type_boat), ("t", type_person)]))
		act_save_person.add_precondition(emgr.And(emgr.LE(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Plus(fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))))), emgr.LE(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Minus(fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))))), emgr.LE(emgr.Plus(fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat)))), emgr.Plus(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Int(25))), emgr.LE(emgr.Minus(fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat)))), emgr.Plus(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Int(25)))))
		act_save_person.add_effect(fluent=fluent_saved(emgr.ParameterExp(up.model.Parameter("t", type_person))), value=emgr.TRUE(), condition=emgr.TRUE())
		problem.add_action(act_save_person)
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_b0)), emgr.Int(-7))
		problem.set_initial_value(fluent_y(emgr.ObjectExp(object_b0)), emgr.Int(0))
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_b1)), emgr.Int(-2))
		problem.set_initial_value(fluent_y(emgr.ObjectExp(object_b1)), emgr.Int(0))
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_b2)), emgr.Int(0))
		problem.set_initial_value(fluent_y(emgr.ObjectExp(object_b2)), emgr.Int(0))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p0)), emgr.Int(-370))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p1)), emgr.Int(-58))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p2)), emgr.Int(63))
		problem.add_goal(goal=emgr.And(fluent_saved(emgr.ObjectExp(object_p0)), fluent_saved(emgr.ObjectExp(object_p1)), fluent_saved(emgr.ObjectExp(object_p2))))

		return problem

	def get_description(self):
		return 'sailing'

	def version(self):
		return 1


class sailing_4_10_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		env = up.environment.get_environment()
		emgr = env.expression_manager
		tm = env.type_manager
		type_person = tm.UserType("person")
		type_boat = tm.UserType("boat")
		fluent_saved = up.model.Fluent("saved", tm.BoolType(), _signature=OrderedDict([("t", type_person)]))
		fluent_x = up.model.Fluent("x", tm.RealType(None, None), _signature=OrderedDict([("b", type_boat)]))
		fluent_y = up.model.Fluent("y", tm.RealType(None, None), _signature=OrderedDict([("b", type_boat)]))
		fluent_d = up.model.Fluent("d", tm.RealType(None, None), _signature=OrderedDict([("t", type_person)]))
		object_b0 = up.model.Object("b0", type_boat)
		object_b1 = up.model.Object("b1", type_boat)
		object_b2 = up.model.Object("b2", type_boat)
		object_b3 = up.model.Object("b3", type_boat)
		object_p0 = up.model.Object("p0", type_person)
		object_p1 = up.model.Object("p1", type_person)
		object_p2 = up.model.Object("p2", type_person)
		object_p3 = up.model.Object("p3", type_person)
		object_p4 = up.model.Object("p4", type_person)
		object_p5 = up.model.Object("p5", type_person)
		object_p6 = up.model.Object("p6", type_person)
		object_p7 = up.model.Object("p7", type_person)
		object_p8 = up.model.Object("p8", type_person)
		object_p9 = up.model.Object("p9", type_person)
		problem_initial_defaults = {}
		problem_initial_defaults[tm.BoolType()] = emgr.FALSE()
		problem = up.model.Problem("instance_4_10_1229", env, initial_defaults=problem_initial_defaults)
		problem.add_object(object_b0)
		problem.add_object(object_b1)
		problem.add_object(object_b2)
		problem.add_object(object_b3)
		problem.add_object(object_p0)
		problem.add_object(object_p1)
		problem.add_object(object_p2)
		problem.add_object(object_p3)
		problem.add_object(object_p4)
		problem.add_object(object_p5)
		problem.add_object(object_p6)
		problem.add_object(object_p7)
		problem.add_object(object_p8)
		problem.add_object(object_p9)
		problem.add_fluent(fluent_saved, default_initial_value=emgr.FALSE())
		problem.add_fluent(fluent_x)
		problem.add_fluent(fluent_y)
		problem.add_fluent(fluent_d)
		act_go_north_east = up.model.InstantaneousAction("go_north_east", _parameters=OrderedDict([("b", type_boat)]))
		act_go_north_east.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		act_go_north_east.add_increase_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		problem.add_action(act_go_north_east)
		act_go_north_west = up.model.InstantaneousAction("go_north_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_north_west.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		act_go_north_west.add_increase_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Real(Fraction(3, 2)), condition=emgr.TRUE())
		problem.add_action(act_go_north_west)
		act_go_est = up.model.InstantaneousAction("go_est", _parameters=OrderedDict([("b", type_boat)]))
		act_go_est.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(3), condition=emgr.TRUE())
		problem.add_action(act_go_est)
		act_go_west = up.model.InstantaneousAction("go_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_west.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(3), condition=emgr.TRUE())
		problem.add_action(act_go_west)
		act_go_south_west = up.model.InstantaneousAction("go_south_west", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south_west.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		act_go_south_west.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south_west)
		act_go_south_east = up.model.InstantaneousAction("go_south_east", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south_east.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		act_go_south_east.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south_east)
		act_go_south = up.model.InstantaneousAction("go_south", _parameters=OrderedDict([("b", type_boat)]))
		act_go_south.add_decrease_effect(fluent=fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), value=emgr.Int(2), condition=emgr.TRUE())
		problem.add_action(act_go_south)
		act_save_person = up.model.InstantaneousAction("save_person", _parameters=OrderedDict([("b", type_boat), ("t", type_person)]))
		act_save_person.add_precondition(emgr.And(emgr.LE(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Plus(fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))))), emgr.LE(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Minus(fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))))), emgr.LE(emgr.Plus(fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat)))), emgr.Plus(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Int(25))), emgr.LE(emgr.Minus(fluent_y(emgr.ParameterExp(up.model.Parameter("b", type_boat))), fluent_x(emgr.ParameterExp(up.model.Parameter("b", type_boat)))), emgr.Plus(fluent_d(emgr.ParameterExp(up.model.Parameter("t", type_person))), emgr.Int(25)))))
		act_save_person.add_effect(fluent=fluent_saved(emgr.ParameterExp(up.model.Parameter("t", type_person))), value=emgr.TRUE(), condition=emgr.TRUE())
		problem.add_action(act_save_person)
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_b0)), emgr.Int(-5))
		problem.set_initial_value(fluent_y(emgr.ObjectExp(object_b0)), emgr.Int(0))
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_b1)), emgr.Int(1))
		problem.set_initial_value(fluent_y(emgr.ObjectExp(object_b1)), emgr.Int(0))
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_b2)), emgr.Int(-7))
		problem.set_initial_value(fluent_y(emgr.ObjectExp(object_b2)), emgr.Int(0))
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_b3)), emgr.Int(1))
		problem.set_initial_value(fluent_y(emgr.ObjectExp(object_b3)), emgr.Int(0))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p0)), emgr.Int(-370))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p1)), emgr.Int(-58))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p2)), emgr.Int(63))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p3)), emgr.Int(483))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p4)), emgr.Int(223))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p5)), emgr.Int(316))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p6)), emgr.Int(-394))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p7)), emgr.Int(-242))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p8)), emgr.Int(-160))
		problem.set_initial_value(fluent_d(emgr.ObjectExp(object_p9)), emgr.Int(-338))
		problem.add_goal(goal=emgr.And(fluent_saved(emgr.ObjectExp(object_p0)), fluent_saved(emgr.ObjectExp(object_p1)), fluent_saved(emgr.ObjectExp(object_p2)), fluent_saved(emgr.ObjectExp(object_p3)), fluent_saved(emgr.ObjectExp(object_p4)), fluent_saved(emgr.ObjectExp(object_p5)), fluent_saved(emgr.ObjectExp(object_p6)), fluent_saved(emgr.ObjectExp(object_p7)), fluent_saved(emgr.ObjectExp(object_p8)), fluent_saved(emgr.ObjectExp(object_p9))))

		return problem

	def get_description(self):
		return 'sailing'

	def version(self):
		return 1