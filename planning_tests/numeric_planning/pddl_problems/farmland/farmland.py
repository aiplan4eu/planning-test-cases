from fractions import Fraction
from collections import OrderedDict
import unified_planning as up
from unified_planning.shortcuts import *

from planning_tests.commons.problem import TestCaseProblem


class farmland_2_100_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)
		
	def get_problem(self):
		env = up.environment.get_env()
		emgr = env.expression_manager
		tm = env.type_manager
		type_farm = tm.UserType("farm")
		fluent_adj = up.model.Fluent("adj", tm.BoolType(), _signature=OrderedDict([("f1", type_farm), ("f2", type_farm)]))
		fluent_x = up.model.Fluent("x", tm.RealType(None, None), _signature=OrderedDict([("b", type_farm)]))
		fluent_cost = up.model.Fluent("cost", tm.RealType(None, None), _signature=OrderedDict([]))
		object_farm0 = up.model.Object("farm0", type_farm)
		object_farm1 = up.model.Object("farm1", type_farm)
		problem_initial_defaults = {}
		problem_initial_defaults[tm.BoolType()] = emgr.FALSE()
		problem = up.model.Problem("instance_2_100_1229_ladder", env, initial_defaults=problem_initial_defaults)
		problem.add_object(object_farm0)
		problem.add_object(object_farm1)
		problem.add_fluent(fluent_adj, default_initial_value=emgr.FALSE())
		problem.add_fluent(fluent_x)
		problem.add_fluent(fluent_cost)
		act_move_fast = up.model.InstantaneousAction("move-fast", _parameters=OrderedDict([("f1", type_farm), ("f2", type_farm)]))
		act_move_fast.add_precondition(emgr.And(emgr.Not(emgr.Equals(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))), emgr.LE(emgr.Int(4), fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm)))), fluent_adj(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))))
		act_move_fast.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm))), value=emgr.Int(4), condition=emgr.TRUE())
		act_move_fast.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f2", type_farm))), value=emgr.Int(2), condition=emgr.TRUE())
		act_move_fast.add_increase_effect(fluent=emgr.FluentExp(fluent_cost), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_move_fast)
		act_move_slow = up.model.InstantaneousAction("move-slow", _parameters=OrderedDict([("f1", type_farm), ("f2", type_farm)]))
		act_move_slow.add_precondition(emgr.And(emgr.Not(emgr.Equals(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))), emgr.LE(emgr.Int(1), fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm)))), fluent_adj(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))))
		act_move_slow.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm))), value=emgr.Int(1), condition=emgr.TRUE())
		act_move_slow.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f2", type_farm))), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_move_slow)
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_farm0)), emgr.Int(100))
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_farm1)), emgr.Int(1))
		problem.set_initial_value(fluent_adj(emgr.ObjectExp(object_farm0), emgr.ObjectExp(object_farm1)), emgr.TRUE())
		problem.set_initial_value(fluent_adj(emgr.ObjectExp(object_farm1), emgr.ObjectExp(object_farm0)), emgr.TRUE())
		problem.set_initial_value(emgr.FluentExp(fluent_cost), emgr.Int(0))
		problem.add_goal(goal=emgr.And(emgr.LE(emgr.Int(1), fluent_x(emgr.ObjectExp(object_farm0))), emgr.LE(emgr.Int(1), fluent_x(emgr.ObjectExp(object_farm1))), emgr.LE(emgr.Int(140), emgr.Plus(emgr.Times(emgr.Int(1), fluent_x(emgr.ObjectExp(object_farm0))), emgr.Plus(emgr.Times(emgr.Real(Fraction(17, 10)), fluent_x(emgr.ObjectExp(object_farm1))), emgr.Int(0))))))


		return problem
	
	def get_description(self):
		return 'farming is important and it will ever be'

	def version(self):
		return 1

class farmland_2_200_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)
		
	def get_problem(self):
		env = up.environment.get_env()
		emgr = env.expression_manager
		tm = env.type_manager
		type_farm = tm.UserType("farm")
		fluent_adj = up.model.Fluent("adj", tm.BoolType(), _signature=OrderedDict([("f1", type_farm), ("f2", type_farm)]))
		fluent_x = up.model.Fluent("x", tm.RealType(None, None), _signature=OrderedDict([("b", type_farm)]))
		fluent_cost = up.model.Fluent("cost", tm.RealType(None, None), _signature=OrderedDict([]))
		object_farm0 = up.model.Object("farm0", type_farm)
		object_farm1 = up.model.Object("farm1", type_farm)
		problem_initial_defaults = {}
		problem_initial_defaults[tm.BoolType()] = emgr.FALSE()
		problem = up.model.Problem("instance_2_200_1229_ladder", env, initial_defaults=problem_initial_defaults)
		problem.add_object(object_farm0)
		problem.add_object(object_farm1)
		problem.add_fluent(fluent_adj, default_initial_value=emgr.FALSE())
		problem.add_fluent(fluent_x)
		problem.add_fluent(fluent_cost)
		act_move_fast = up.model.InstantaneousAction("move-fast", _parameters=OrderedDict([("f1", type_farm), ("f2", type_farm)]))
		act_move_fast.add_precondition(emgr.And(emgr.Not(emgr.Equals(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))), emgr.LE(emgr.Int(4), fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm)))), fluent_adj(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))))
		act_move_fast.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm))), value=emgr.Int(4), condition=emgr.TRUE())
		act_move_fast.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f2", type_farm))), value=emgr.Int(2), condition=emgr.TRUE())
		act_move_fast.add_increase_effect(fluent=emgr.FluentExp(fluent_cost), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_move_fast)
		act_move_slow = up.model.InstantaneousAction("move-slow", _parameters=OrderedDict([("f1", type_farm), ("f2", type_farm)]))
		act_move_slow.add_precondition(emgr.And(emgr.Not(emgr.Equals(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))), emgr.LE(emgr.Int(1), fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm)))), fluent_adj(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))))
		act_move_slow.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm))), value=emgr.Int(1), condition=emgr.TRUE())
		act_move_slow.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f2", type_farm))), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_move_slow)
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_farm0)), emgr.Int(200))
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_farm1)), emgr.Int(1))
		problem.set_initial_value(fluent_adj(emgr.ObjectExp(object_farm0), emgr.ObjectExp(object_farm1)), emgr.TRUE())
		problem.set_initial_value(fluent_adj(emgr.ObjectExp(object_farm1), emgr.ObjectExp(object_farm0)), emgr.TRUE())
		problem.set_initial_value(emgr.FluentExp(fluent_cost), emgr.Int(0))
		problem.add_goal(goal=emgr.And(emgr.LE(emgr.Int(1), fluent_x(emgr.ObjectExp(object_farm0))), emgr.LE(emgr.Int(1), fluent_x(emgr.ObjectExp(object_farm1))), emgr.LE(emgr.Int(280), emgr.Plus(emgr.Times(emgr.Int(1), fluent_x(emgr.ObjectExp(object_farm0))), emgr.Plus(emgr.Times(emgr.Real(Fraction(17, 10)), fluent_x(emgr.ObjectExp(object_farm1))), emgr.Int(0))))))
	

		return problem
	
	def get_description(self):
		return 'farming is important and it will ever be'

	def version(self):
		return 1
		

class farmland_2_300_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)
		
	def get_problem(self):
		env = up.environment.get_env()
		emgr = env.expression_manager
		tm = env.type_manager
		type_farm = tm.UserType("farm")
		fluent_adj = up.model.Fluent("adj", tm.BoolType(), _signature=OrderedDict([("f1", type_farm), ("f2", type_farm)]))
		fluent_x = up.model.Fluent("x", tm.RealType(None, None), _signature=OrderedDict([("b", type_farm)]))
		fluent_cost = up.model.Fluent("cost", tm.RealType(None, None), _signature=OrderedDict([]))
		object_farm0 = up.model.Object("farm0", type_farm)
		object_farm1 = up.model.Object("farm1", type_farm)
		problem_initial_defaults = {}
		problem_initial_defaults[tm.BoolType()] = emgr.FALSE()
		problem = up.model.Problem("instance_2_300_1229_ladder", env, initial_defaults=problem_initial_defaults)
		problem.add_object(object_farm0)
		problem.add_object(object_farm1)
		problem.add_fluent(fluent_adj, default_initial_value=emgr.FALSE())
		problem.add_fluent(fluent_x)
		problem.add_fluent(fluent_cost)
		act_move_fast = up.model.InstantaneousAction("move-fast", _parameters=OrderedDict([("f1", type_farm), ("f2", type_farm)]))
		act_move_fast.add_precondition(emgr.And(emgr.Not(emgr.Equals(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))), emgr.LE(emgr.Int(4), fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm)))), fluent_adj(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))))
		act_move_fast.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm))), value=emgr.Int(4), condition=emgr.TRUE())
		act_move_fast.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f2", type_farm))), value=emgr.Int(2), condition=emgr.TRUE())
		act_move_fast.add_increase_effect(fluent=emgr.FluentExp(fluent_cost), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_move_fast)
		act_move_slow = up.model.InstantaneousAction("move-slow", _parameters=OrderedDict([("f1", type_farm), ("f2", type_farm)]))
		act_move_slow.add_precondition(emgr.And(emgr.Not(emgr.Equals(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))), emgr.LE(emgr.Int(1), fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm)))), fluent_adj(emgr.ParameterExp(up.model.Parameter("f1", type_farm)), emgr.ParameterExp(up.model.Parameter("f2", type_farm)))))
		act_move_slow.add_decrease_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f1", type_farm))), value=emgr.Int(1), condition=emgr.TRUE())
		act_move_slow.add_increase_effect(fluent=fluent_x(emgr.ParameterExp(up.model.Parameter("f2", type_farm))), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_move_slow)
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_farm0)), emgr.Int(300))
		problem.set_initial_value(fluent_x(emgr.ObjectExp(object_farm1)), emgr.Int(1))
		problem.set_initial_value(fluent_adj(emgr.ObjectExp(object_farm0), emgr.ObjectExp(object_farm1)), emgr.TRUE())
		problem.set_initial_value(fluent_adj(emgr.ObjectExp(object_farm1), emgr.ObjectExp(object_farm0)), emgr.TRUE())
		problem.set_initial_value(emgr.FluentExp(fluent_cost), emgr.Int(0))
		problem.add_goal(goal=emgr.And(emgr.LE(emgr.Int(1), fluent_x(emgr.ObjectExp(object_farm0))), emgr.LE(emgr.Int(1), fluent_x(emgr.ObjectExp(object_farm1))), emgr.LE(emgr.Int(420), emgr.Plus(emgr.Times(emgr.Int(1), fluent_x(emgr.ObjectExp(object_farm0))), emgr.Plus(emgr.Times(emgr.Real(Fraction(17, 10)), fluent_x(emgr.ObjectExp(object_farm1))), emgr.Int(0))))))
	

		return problem
	
	def get_description(self):
		return 'farming is important and it will ever be'

	def version(self):
		return 1