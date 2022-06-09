import this
import unified_planning
from unified_planning.model import problem
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.up_problems.simple_linear_conditions import UPEqualityConditions, UPGreaterLowerConditions, UPNegativeConditions, UPGreaterThanConditions, UPLowerThanConditions
from unified_planning.environment import get_env
from unittest import TestCase, main



class TestSimpleLinearConditions(TestCase):

	def setUp(self):
		self.problem_equality = UPEqualityConditions(expected_version=1)
		self.problem_negative_conditions = UPNegativeConditions(expected_version=1)
		self.problem_grater_lower_conditions = UPGreaterLowerConditions(expected_version=1)
		self.problem_lower_than_conditions = UPGreaterThanConditions(expected_version=1)
		self.problem_grater_than_conditions = UPLowerThanConditions(expected_version=1)



	@staticmethod
	def execute_one_shot_planning_test(problem,planner_name):
		results = {}
		with OneshotPlanner(name=planner_name) as planner:
			if planner.supports(problem.kind):
					plan = planner.solve(problem)
					with PlanValidator(problem_kind=problem.kind) as validator:
						check = validator.validate(problem, plan.plan)
						results[planner_name] = check
						assert check

		print(f'Planners executed: {" ".join(results.keys())}')



	

	def test_equality(self,planner_name):
		self.execute_one_shot_planning_test(self.problem_equality.get_problem(),planner_name)

	
	def test_negative_conditions(self,planner_name):
		self.execute_one_shot_planning_test(self.problem_negative_conditions.get_problem(),planner_name)

	
	def test_greater_than_conditions(self,planner_name):
		self.execute_one_shot_planning_test(self.problem_grater_than_conditions.get_problem(),planner_name)

	
	def test_lower_than_conditions(self,planner_name):
		self.execute_one_shot_planning_test(self.problem_lower_than_conditions.get_problem(),planner_name)

	
	def test_greater_lower_conditions(self,planner_name):
		self.execute_one_shot_planning_test(self.problem_lower_than_conditions.get_problem(),planner_name)


if __name__ == '__main__':
   main()


