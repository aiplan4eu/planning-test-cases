import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io.pddl_writer import PDDLWriter
from unified_planning.io.pddl_reader import PDDLReader
import pkg_resources
from planning_tests.commons.problem import TestCaseProblem
#path = '/home/valerik/Desktop/programmazione/planning/planning-test-cases/planning_tests/numeric_planning/pddl_problems/block_grouping/'
path = pkg_resources.resource_filename(__name__,'/')
class block_grouping_5_5_2_1(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'block_grouping_domain.pddl'),(path + 'block_grouping_5_5_2_1.pddl'))
		return problem

	def get_description(self):
		return 'block grouping'

	def version(self):
		return 1

class block_grouping_5_5_2_2(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'block_grouping_domain.pddl'),(path + 'block_grouping_5_5_2_2.pddl'))

		return problem

	def get_description(self):
		return 'block grouping'

	def version(self):
		return 1

class block_grouping_5_5_2_3(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'block_grouping_domain.pddl'),(path + 'block_grouping_5_5_2_3.pddl'))

		return problem

	def get_description(self):
		return 'block grouping'

	def version(self):
		return 1


class block_grouping_11_10_2_2(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'block_grouping_domain.pddl'),(path + 'block_grouping_11_10_2_2.pddl'))

		return problem

	def get_description(self):
		return 'block grouping'

	def version(self):
		return 1

#medium difficulty problems
class block_grouping_20_25_6_2(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'block_grouping_domain.pddl'),(path + 'block_grouping_20_25_6_2.pddl'))

		return problem

	def get_description(self):
		return 'block grouping'

	def version(self):
		return 1


class block_grouping_20_25_6_3(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'block_grouping_domain.pddl'),(path + 'block_grouping_20_25_6_3.pddl'))

		return problem

	def get_description(self):
		return 'block grouping'

	def version(self):
		return 1
