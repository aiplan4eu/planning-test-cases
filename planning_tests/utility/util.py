import os
import sys
from unified_planning.shortcuts import OneshotPlanner, PlanValidator


plans = []

@staticmethod
def my_callback(intermediate_result):
    plans.append(intermediate_result.plan)
    if len(intermediate_result.plan.actions) <= 1:
        return False
    else:
        return True	

def saveArray(result):
    fout = open('output',"w")
    for line in result:
        fout.write(line)
    fout.close()

class TestUtil:

    @staticmethod
    def execute_one_shot_planning_test(problem,planner_name,problem_name = "",expected_plan_length=None ):
            
        with OneshotPlanner(name=planner_name) as planner:
            #this if might be deleted
            if planner.supports(problem.kind):
                result = planner.solve(problem)
                plan = result.plan
                print(plan)
                with PlanValidator(problem_kind=problem.kind,plan_kind=plan.kind) as validator:
                    check = validator.validate(problem, plan)
                    if expected_plan_length is not None:
                        check = check and len(plan.actions) == expected_plan_length
                    
                    assert check



    @staticmethod
    def execute_anytime_planning_test(problem,planner_name,problem_name = "",expected_plan_length=None ):
                    
        with OneshotPlanner(name=planner_name) as planner:
            #this if might be deleted
            if planner.supports(problem.kind):
                result = planner.solve(problem,callback = my_callback, timeout = 30)
                plan = result.plan
                with PlanValidator(problem_kind=problem.kind,plan_kind=plan.kind) as validator:
                    check = validator.validate(problem, plan)
                    if expected_plan_length is not None:
                        check = check and len(plan.actions) == expected_plan_length
                    saveArray(plans)
                    assert check




            