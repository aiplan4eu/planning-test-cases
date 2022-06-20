import os
import sys
from unified_planning.shortcuts import OneshotPlanner, PlanValidator
#from planning_tests.utility.correct_output import correct, correct_validation

class TestUtil:

	@staticmethod
	def execute_one_shot_planning_test(problem,planner_name,problem_name = "",expected_plan_length=None ):
			
		with OneshotPlanner(name=planner_name) as planner:
			if planner.supports(problem.kind):
				result = planner.solve(problem)
				plan = result.plan
				#if len(sys.argv) > 2 :
						#if sys.argv[2] == '-v' or sys.argv[2] == '-verbose':
							#open(f"output","w").write('\n'.join([str(act) for act in plan.plan.actions]))
							#correct("output")
							#os.system("./validate  "+ path +"block_grouping_domain.pddl "+ path + name +" output")
							#print(correct_validation(str(plan)))
				with PlanValidator(problem_kind=problem.kind,plan_kind=plan.kind) as validator:
					check = validator.validate(problem, plan)
					if expected_plan_length is not None:
						check = check and len(plan.actions) == expected_plan_length

					assert check
				

			