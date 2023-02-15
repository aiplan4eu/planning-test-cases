import os
import time

from unified_planning.engines import PlanGenerationResultStatus




# pip install https://github.com/plaans/aries/releases/download/latest/up_aries.tar.gz

from unified_planning.shortcuts import *
from unified_planning.model.htn import *
import unified_planning as up
from unified_planning.environment import get_environment

import planning_tests.refinement_planning.hddl
from planning_tests.commons.problem import TestCase

get_environment().factory.add_engine('aries', 'up_aries', 'AriesDev')
#get_environment().factory.add_engine('aries', 'up_aries', 'Aries')
get_environment().credits_stream = None # silence credits


def oneshot_planners():
    """All available oneshot planners."""
    # return ["aries"]
    tags = [n for n in get_environment().factory.engines]
    tags = [t for t in tags
            if get_environment().factory.engine(t).is_oneshot_planner()]
    return tags


def up_tests():
    """"All test cases defined in the `unified_planning` module. All are assumed to be solvable."""
    from unified_planning.test.examples import get_example_problems

    cases = []
    for name, problem in get_example_problems().items():
        pb = problem.problem.clone()
        pb.name = f"up:{name}"
        cases.append(TestCase(pb, solvable=True))
    return cases


def run(planners: List[str], problems: List[TestCase]):
    for test_case in problems:
        print()
        print(test_case.name.ljust(40), end='\n')
        pb = test_case.problem()

        for planner_id in planners:
            planner = OneshotPlanner(name=planner_id)
            if planner.supports(pb.kind):

                print("  ", planner_id.ljust(80), end='')
                start = time.time()
                try:
                    result = planner.solve(pb, timeout=1) #, output_stream=sys.stdout)
                    end = time.time()
                    status = str(result.status).replace("PlanGenerationResultStatus.", "").ljust(20)
                    print("\t  ", status, "\t    ", end - start)
                    if result.status == PlanGenerationResultStatus.INTERNAL_ERROR and result.log_messages is not None:
                        print('\n'.join(map(str, result.log_messages)))

                except Exception as e:
                    print("\t CRASH !!!!", e)


def report(*planners: str,
           problem_prefix: str = ""):

    if len(planners) == 0:
        planners = oneshot_planners()

    problems = up_tests() + planning_tests.refinement_planning.hddl.problems()
    problems = [p for p in problems if p.name.startswith(problem_prefix)]
    run(planners, problems)


if __name__ == "__main__":
    # report(planner="fast-downward", problem_prefix="up:")
    report("aries", "fast-downward",
           problem_prefix="up:basic")
    report("aries")

    report()

