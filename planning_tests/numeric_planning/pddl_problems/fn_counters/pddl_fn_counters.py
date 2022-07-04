import pkg_resources
import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io.pddl_writer import PDDLWriter
from unified_planning.io.pddl_reader import PDDLReader

from planning_tests.commons.problem import TestCaseProblem
path = pkg_resources.resource_filename(__name__,'/')

class fn_counters_2(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'fn_counters_domain.pddl'),(path + 'fn_counters_2.pddl'))
									

		return problem

	def get_description(self):
		return 'fn_counters'

	def version(self):
		return 1

class fn_counters_4(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'fn_counters_domain.pddl'),(path + 'fn_counters_4.pddl'))

		return problem

	def get_description(self):
		return 'fn_counters'

	def version(self):
		return 1

class fn_counters_8(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'fn_counters_domain.pddl'),(path + 'fn_counters_8.pddl'))

		return problem

	def get_description(self):
		return 'fn_counters'

	def version(self):
		return 1

class fn_counters_20(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'fn_counters_domain.pddl'),(path + 'fn_counters_20.pddl'))

		return problem

	def get_description(self):
		return 'fn_counters'

	def version(self):
		return 1


