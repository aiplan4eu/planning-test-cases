import pkg_resources
import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io.pddl_writer import PDDLWriter
from unified_planning.io.pddl_reader import PDDLReader

from planning_tests.commons.problem import TestCaseProblem
path = pkg_resources.resource_filename(__name__,'/')

class sailing_1_1_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'sailing_domain.pddl'),(path + 'sailing_1_1_1229.pddl'))
									

		return problem

	def get_description(self):
		return 'sailing'

	def version(self):
		return 1

class sailing_1_2_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'sailing_domain.pddl'),(path + 'sailing_1_2_1229.pddl'))

		return problem

	def get_description(self):
		return 'sailing'

	def version(self):
		return 1

class sailing_1_3_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'sailing_domain.pddl'),(path + 'sailing_1_3_1229.pddl'))

		return problem

	def get_description(self):
		return 'sailing'

	def version(self):
		return 1


class sailing_3_3_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'sailing_domain.pddl'),(path + 'sailing_3_3_1229.pddl'))

		return problem

	def get_description(self):
		return 'sailing'

	def version(self):
		return 1


class sailing_4_10_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'sailing_domain.pddl'),(path + 'sailing_4_10_1229.pddl'))

		return problem

	def get_description(self):
		return 'sailing'

	def version(self):
		return 1