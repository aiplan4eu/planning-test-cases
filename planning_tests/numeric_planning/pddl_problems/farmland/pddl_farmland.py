import pkg_resources
import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io.pddl_writer import PDDLWriter
from unified_planning.io.pddl_reader import PDDLReader

from planning_tests.commons.problem import TestCaseProblem


path = pkg_resources.resource_filename(__name__,'/')

class farmland_2_100_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + '/farmland_domain.pddl'),(path + 'farmland_2_100_1229.pddl'))
							

		return problem

	def get_description(self):
		return 'farming is important'

	def version(self):
		return 1

class farmland_2_200_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + '/farmland_domain.pddl'),(path + 'farmland_2_200_1229.pddl'))

		return problem

	def get_description(self):
		return 'farming is important'

	def version(self):
		return 1

class farmland_2_300_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + '/farmland_domain.pddl'),(path + 'farmland_2_300_1229.pddl'))

		return problem

	def get_description(self):
		return 'farming is important'

	def version(self):
		return 1

class farmland_8_400_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + '/farmland_domain.pddl'),(path + 'farmland_8_400_1229.pddl'))

		return problem

	def get_description(self):
		return 'farming is important'

	def version(self):
		return 1

class farmland_10_400_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + '/farmland_domain.pddl'),(path + 'farmland_10_400_1229.pddl'))

		return problem

	def get_description(self):
		return 'farming is important'

	def version(self):
		return 1

class farmland_10_1000_1229(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + '/farmland_domain.pddl'),(path + 'farmland_10_1000_1229.pddl'))

		return problem

	def get_description(self):
		return 'farming is important'

	def version(self):
		return 1