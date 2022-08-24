import unified_planning
from unified_planning.shortcuts import*
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import anytime_names
from planning_tests.numeric_planning.pddl_problems.rovers.rovers import  rovers_pfile2,rovers_pfile3,rovers_pfile4,rovers_pfile5
import pytest
import sys




    
plans = []
  
@staticmethod
def my_callback(intermediate_result):
    plans.append(intermediate_result.plan)
    if len(intermediate_result.plan.actions) <= 1:
        return False
    else:
        return True	
    
 
if __name__ == "__main__":
    tmp = get_env()
    rovers_pfile2 = rovers_pfile2(expected_version=1)
    problem = rovers_pfile2.get_problem()
    with OneshotPlanner(name="lpg") as planner:
            #this if might be deleted
           
            result = planner.solve(problem,callback = my_callback, timeout = 10)
            plan = result.plan
              