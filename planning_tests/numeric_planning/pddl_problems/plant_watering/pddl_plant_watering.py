import pkg_resources
import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io.pddl_writer import PDDLWriter
from unified_planning.io.pddl_reader import PDDLReader

from planning_tests.commons.problem import TestCaseProblem
path = pkg_resources.resource_filename(__name__,'/')

class plant_watering_4_1(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'plant_watering_domain.pddl'),(path + 'plant_watering_4_1.pddl'))
									

		return problem

	def get_description(self):
		return 'time to water those plants'

	def version(self):
		return 1

class plant_watering_4_2(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'plant_watering_domain.pddl'),(path + 'plant_watering_4_2.pddl'))
		return problem

	def get_description(self):
		return 'time to water those plants'

	def version(self):
		return 1

class plant_watering_4_3(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'plant_watering_domain.pddl'),(path + 'plant_watering_4_3.pddl'))
		return problem

	def get_description(self):
		return 'time to water those plants'

	def version(self):
		return 1

class plant_watering_18_2(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'plant_watering_domain.pddl'),(path + 'plant_watering_18_2.pddl'))
		return problem

	def get_description(self):
		return 'time to water those plants'

	def version(self):
		return 1

class plant_watering_20_3(TestCaseProblem):

	def __init__(self, expected_version):
		TestCaseProblem.__init__(self, expected_version)

	def get_problem(self):

		reader = PDDLReader()
		problem = reader.parse_problem((path + 'plant_watering_domain.pddl'),(path + 'plant_watering_20_3.pddl'))
		return problem

	def get_description(self):
		return 'time to water those plants'

	def version(self):
		return 1