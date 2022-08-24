import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io.pddl_reader import PDDLReader
import pkg_resources
from planning_tests.commons.problem import TestCaseProblem

path = pkg_resources.resource_filename(__name__,'/')

class TPP_p01(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'TPP_domain.pddl'),(path + 'TPP_p01.pddl'))
		return problem

	def get_description(self):
		return 'TPP'

	def version(self):
		return 1

class TPP_p02(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'TPP_domain.pddl'),(path + 'TPP_p02.pddl'))
		return problem

	def get_description(self):
		return 'TPP'

	def version(self):
		return 1