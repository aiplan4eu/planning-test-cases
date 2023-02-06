import os
import sys
from unified_planning.shortcuts import OneshotPlanner, PlanValidator, AnytimePlanner



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
                print(len(plan.actions))
                with PlanValidator(problem_kind=problem.kind,plan_kind=plan.kind) as validator:
                    check = validator.validate(problem, plan)
                    if expected_plan_length is not None:
                        check = check and len(plan.actions) == expected_plan_length
                    
                    assert check

    @staticmethod
    def execute_one_shot_planning_test_minimize_value(problem,planner_name,problem_name = "",expected_plan_length=None ):
            
        with OneshotPlanner(name=planner_name) as planner:
            #this if might be deleted
            if planner.supports(problem.kind):
                result = planner.solve(problem)
                plan = result.plan
                print(plan)
                print(len(plan.actions))
                with PlanValidator(problem_kind=problem.kind,plan_kind=plan.kind) as validator:
                    check = validator.validate(problem, plan)
                    if expected_plan_length is not None:
                        check = check and len(plan.actions) == expected_plan_length
                    
                    assert check



    @staticmethod
    def execute_anytime_planning_test(problem,planner_name,problem_name = "",timeout=None):
                    
       #with AnytimePlanner(name=planner_name, anytime_guarantee="INCREASING_QUALITY") as planner:
       with AnytimePlanner(name=planner_name) as planner:
            #this if might be deleted
           if planner.supports(problem.kind) and planner.is_anytime_planner():
                solutions = []
                for p in planner.get_solutions(problem,2):
                    if p.plan is not None:
                        solutions.append(p.plan)
                        print(p.plan)
                        print("\n")

                with PlanValidator(problem_kind=problem.kind,plan_kind=solutions[0].kind) as validator:
                   check = validator.validate(problem, solutions[0])
                   assert check 

                total_solutions = len(solutions)
                if total_solutions > 1:
                    total_solutions = total_solutions - 1
                    for i in range(1,total_solutions):
                        plan = solutions[i]
                        with PlanValidator(problem_kind=problem.kind,plan_kind=plan.kind) as validator:
                            check = validator.validate(problem, plan)
                            assert check
                        assert len(plan.actions) <= len(solutions[i-1].actions)
                        




            