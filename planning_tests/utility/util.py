import os
import sys
from unified_planning.shortcuts import OneshotPlanner, PlanValidator
#from planning_tests.utility.correct_output import correct, correct_validation

class TestUtil:

	@staticmethod
	def execute_one_shot_planning_test(problem,name,planner_name):
			
		with OneshotPlanner(name=planner_name) as planner:
			if planner.supports(problem.kind):
				plan = planner.solve(problem)
				#if len(sys.argv) > 2 :
						#if sys.argv[2] == '-v' or sys.argv[2] == '-verbose':
							#open(f"output","w").write('\n'.join([str(act) for act in plan.plan.actions]))
							#correct("output")
							#os.system("./validate  "+ path +"block_grouping_domain.pddl "+ path + name +" output")
							#print(correct_validation(str(plan)))
				with PlanValidator(problem_kind=problem.kind) as validator:
					check = validator.validate(problem, plan.plan)
					assert check
				

			