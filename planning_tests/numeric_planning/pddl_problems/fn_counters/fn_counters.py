from fractions import Fraction
from collections import OrderedDict
import unified_planning as up
from unified_planning.shortcuts import *
from unified_planning.io.pddl_writer import PDDLWriter
from unified_planning.io.pddl_reader import PDDLReader

from planning_tests.commons.problem import TestCaseProblem


class fn_counters_2(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):
		env = up.environment.get_environment()
		emgr = env.expression_manager
		tm = env.type_manager
		type_counter = tm.UserType("counter")
		fluent_value = up.model.Fluent("value", tm.RealType(None, None), _signature=OrderedDict([("c", type_counter)]))
		fluent_max_int = up.model.Fluent("max_int", tm.RealType(None, None), _signature=OrderedDict([]))
		object_c0 = up.model.Object("c0", type_counter)
		object_c1 = up.model.Object("c1", type_counter)
		problem_initial_defaults = {}
		problem_initial_defaults[tm.BoolType()] = emgr.FALSE()
		problem = up.model.Problem("instance_2", env, initial_defaults=problem_initial_defaults)
		problem.add_object(object_c0)
		problem.add_object(object_c1)
		problem.add_fluent(fluent_value)
		problem.add_fluent(fluent_max_int)
		act_increment = up.model.InstantaneousAction("increment", _parameters=OrderedDict([("c", type_counter)]))
		act_increment.add_precondition(emgr.LE(emgr.Plus(fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter))), emgr.Int(1)), emgr.FluentExp(fluent_max_int)))
		act_increment.add_increase_effect(fluent=fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter))), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_increment)
		act_decrement = up.model.InstantaneousAction("decrement", _parameters=OrderedDict([("c", type_counter)]))
		act_decrement.add_precondition(emgr.LE(emgr.Int(1), fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter)))))
		act_decrement.add_decrease_effect(fluent=fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter))), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_decrement)
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c0)), emgr.Int(0))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c1)), emgr.Int(0))
		problem.set_initial_value(emgr.FluentExp(fluent_max_int), emgr.Int(4))
		problem.add_goal(goal=emgr.LE(emgr.Plus(fluent_value(emgr.ObjectExp(object_c0)), emgr.Int(1)), fluent_value(emgr.ObjectExp(object_c1))))
		
		return problem

	def get_description(self):
		return 'fn-counters'

	def version(self):
		return 1

class fn_counters_4(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):
		env = up.environment.get_environment()
		emgr = env.expression_manager
		tm = env.type_manager
		type_counter = tm.UserType("counter")
		fluent_value = up.model.Fluent("value", tm.RealType(None, None), _signature=OrderedDict([("c", type_counter)]))
		fluent_max_int = up.model.Fluent("max_int", tm.RealType(None, None), _signature=OrderedDict([]))
		object_c0 = up.model.Object("c0", type_counter)
		object_c1 = up.model.Object("c1", type_counter)
		object_c2 = up.model.Object("c2", type_counter)
		object_c3 = up.model.Object("c3", type_counter)
		problem_initial_defaults = {}
		problem_initial_defaults[tm.BoolType()] = emgr.FALSE()
		problem = up.model.Problem("instance_4", env, initial_defaults=problem_initial_defaults)
		problem.add_object(object_c0)
		problem.add_object(object_c1)
		problem.add_object(object_c2)
		problem.add_object(object_c3)
		problem.add_fluent(fluent_value)
		problem.add_fluent(fluent_max_int)
		act_increment = up.model.InstantaneousAction("increment", _parameters=OrderedDict([("c", type_counter)]))
		act_increment.add_precondition(emgr.LE(emgr.Plus(fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter))), emgr.Int(1)), emgr.FluentExp(fluent_max_int)))
		act_increment.add_increase_effect(fluent=fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter))), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_increment)
		act_decrement = up.model.InstantaneousAction("decrement", _parameters=OrderedDict([("c", type_counter)]))
		act_decrement.add_precondition(emgr.LE(emgr.Int(1), fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter)))))
		act_decrement.add_decrease_effect(fluent=fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter))), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_decrement)
		problem.set_initial_value(emgr.FluentExp(fluent_max_int), emgr.Int(8))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c0)), emgr.Int(0))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c1)), emgr.Int(0))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c2)), emgr.Int(0))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c3)), emgr.Int(0))
		problem.add_goal(goal=emgr.And(emgr.LE(emgr.Plus(fluent_value(emgr.ObjectExp(object_c0)), emgr.Int(1)), fluent_value(emgr.ObjectExp(object_c1))), emgr.LE(emgr.Plus(fluent_value(emgr.ObjectExp(object_c1)), emgr.Int(1)), fluent_value(emgr.ObjectExp(object_c2))), emgr.LE(emgr.Plus(fluent_value(emgr.ObjectExp(object_c2)), emgr.Int(1)), fluent_value(emgr.ObjectExp(object_c3)))))
				
		return problem

	def get_description(self):
		return 'fn-counters'

	def version(self):
		return 1

class fn_counters_8(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):
		env = up.environment.get_environment()
		emgr = env.expression_manager
		tm = env.type_manager
		type_counter = tm.UserType("counter")
		fluent_value = up.model.Fluent("value", tm.RealType(None, None), _signature=OrderedDict([("c", type_counter)]))
		fluent_max_int = up.model.Fluent("max_int", tm.RealType(None, None), _signature=OrderedDict([]))
		object_c0 = up.model.Object("c0", type_counter)
		object_c1 = up.model.Object("c1", type_counter)
		object_c2 = up.model.Object("c2", type_counter)
		object_c3 = up.model.Object("c3", type_counter)
		object_c4 = up.model.Object("c4", type_counter)
		object_c5 = up.model.Object("c5", type_counter)
		object_c6 = up.model.Object("c6", type_counter)
		object_c7 = up.model.Object("c7", type_counter)
		problem_initial_defaults = {}
		problem_initial_defaults[tm.BoolType()] = emgr.FALSE()
		problem = up.model.Problem("instance_8", env, initial_defaults=problem_initial_defaults)
		problem.add_object(object_c0)
		problem.add_object(object_c1)
		problem.add_object(object_c2)
		problem.add_object(object_c3)
		problem.add_object(object_c4)
		problem.add_object(object_c5)
		problem.add_object(object_c6)
		problem.add_object(object_c7)
		problem.add_fluent(fluent_value)
		problem.add_fluent(fluent_max_int)
		act_increment = up.model.InstantaneousAction("increment", _parameters=OrderedDict([("c", type_counter)]))
		act_increment.add_precondition(emgr.LE(emgr.Plus(fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter))), emgr.Int(1)), emgr.FluentExp(fluent_max_int)))
		act_increment.add_increase_effect(fluent=fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter))), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_increment)
		act_decrement = up.model.InstantaneousAction("decrement", _parameters=OrderedDict([("c", type_counter)]))
		act_decrement.add_precondition(emgr.LE(emgr.Int(1), fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter)))))
		act_decrement.add_decrease_effect(fluent=fluent_value(emgr.ParameterExp(up.model.Parameter("c", type_counter))), value=emgr.Int(1), condition=emgr.TRUE())
		problem.add_action(act_decrement)
		problem.set_initial_value(emgr.FluentExp(fluent_max_int), emgr.Int(16))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c0)), emgr.Int(0))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c1)), emgr.Int(0))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c2)), emgr.Int(0))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c3)), emgr.Int(0))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c4)), emgr.Int(0))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c5)), emgr.Int(0))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c6)), emgr.Int(0))
		problem.set_initial_value(fluent_value(emgr.ObjectExp(object_c7)), emgr.Int(0))
		problem.add_goal(goal=emgr.And(emgr.LE(emgr.Plus(fluent_value(emgr.ObjectExp(object_c0)), emgr.Int(1)), fluent_value(emgr.ObjectExp(object_c1))), emgr.LE(emgr.Plus(fluent_value(emgr.ObjectExp(object_c1)), emgr.Int(1)), fluent_value(emgr.ObjectExp(object_c2))), emgr.LE(emgr.Plus(fluent_value(emgr.ObjectExp(object_c2)), emgr.Int(1)), fluent_value(emgr.ObjectExp(object_c3))), emgr.LE(emgr.Plus(fluent_value(emgr.ObjectExp(object_c3)), emgr.Int(1)), fluent_value(emgr.ObjectExp(object_c4))), emgr.LE(emgr.Plus(fluent_value(emgr.ObjectExp(object_c4)), emgr.Int(1)), fluent_value(emgr.ObjectExp(object_c5))), emgr.LE(emgr.Plus(fluent_value(emgr.ObjectExp(object_c5)), emgr.Int(1)), fluent_value(emgr.ObjectExp(object_c6))), emgr.LE(emgr.Plus(fluent_value(emgr.ObjectExp(object_c6)), emgr.Int(1)), fluent_value(emgr.ObjectExp(object_c7)))))
	

		return problem

	def get_description(self):
		return 'fn-counters'

	def version(self):
		return 1