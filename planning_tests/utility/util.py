import os
import sys
from unified_planning.shortcuts import OneshotPlanner, PlanValidator


class TestUtil:

	@staticmethod
	def execute_one_shot_planning_test(problem,planner_name,problem_name = "",expected_plan_length=None ):
			
		with OneshotPlanner(name=planner_name) as planner:
			#this if might be deleted
			if planner.supports(problem.kind):
				result = planner.solve(problem)
				plan = result.plan
				with PlanValidator(problem_kind=problem.kind,plan_kind=plan.kind) as validator:
					check = validator.validate(problem, plan)
					if expected_plan_length is not None:
						check = check and len(plan.actions) == expected_plan_length

					assert check
				

			