import os
import sys
import time
from typing import Tuple

from unified_planning.engines import PlanGenerationResultStatus, ValidationResultStatus, PlanGenerationResult
from unified_planning.plans import Plan

from unified_planning.shortcuts import *
from unified_planning.environment import get_environment

import planning_tests.refinement_planning.hddl
from planning_tests.commons.problem import TestCase
from planning_tests.commons.results import *

get_environment().credits_stream = None  # silence credits


def all_test_cases():
    """Returns all test cases of this repository"""
    return up_tests() + planning_tests.refinement_planning.problems()


def oneshot_planners():
    """All available oneshot planners."""
    tags = [n for n in get_environment().factory.engines]
    tags = [t for t in tags
            if get_environment().factory.engine(t).is_oneshot_planner()]
    return tags


def up_tests():
    """All test cases defined in the `unified_planning.test` module. All are assumed to be solvable."""
    from unified_planning.test.examples import get_example_problems

    cases = []
    for name, problem in get_example_problems().items():
        pb = problem.problem.clone()
        pb.name = f"up:{name}"
        plans = [problem.plan] if problem.plan is not None else []
        cases.append(TestCase(pb, solvable=True, valid_plans=plans))
    return cases


def validate_plan(plan: Plan, problem: Problem) -> ResultSet:
    try:
        with PlanValidator(problem_kind=problem.kind) as validator:
            if not validator.supports_plan(plan.kind):
                return Warn(f"Validator {validator.name} does not support plan")
            check = validator.validate(problem, plan)
            if check.status is ValidationResultStatus.VALID:
                return Ok("Valid")
            else:
                return Err("INVALID")
    except unified_planning.exceptions.UPNoSuitableEngineAvailableException:
        return Warn("No validator for problem")
    except Exception as e:
        return Warn(f"Validator crash ({e})")


def verify(cond: bool, error_tag: str, ok_tag: str = "") -> ResultSet:
    """Returns an Error if the condition passed in parameter does not hold."""
    if cond:
        return Ok(ok_tag)
    else:
        return Err(error_tag)


def check_result(test: TestCase, result: PlanGenerationResult, planner) -> ResultSet:
    output = Void()
    output += verify(result.status != PlanGenerationResultStatus.INTERNAL_ERROR, "forbidden internal error")

    if result.plan:
        if not test.solvable:
            output += Err("Unsolvable problem")
        # if the planner guarantees optimality, this should be reflected in
        # the result status
        metrics = test.problem.quality_metrics
        if not metrics:
            output += verify(result.status is PlanGenerationResultStatus.SOLVED_SATISFICING, "expected SAT ")
        else:
            if planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
                output += verify(result.status is PlanGenerationResultStatus.SOLVED_OPTIMALLY, "expected OPT")
            else:
                output += verify(result.status in (PlanGenerationResultStatus.SOLVED_OPTIMALLY,
                                         PlanGenerationResultStatus.SOLVED_SATISFICING), "expected SAT/OPT")
        output += validate_plan(result.plan, test.problem)
    elif test.solvable:
        output += verify(result.status != PlanGenerationResultStatus.UNSOLVABLE_PROVEN, "UNSOLVABLE on solvable problem")
        # We are only running the test on solvable instances
        output += verify(result.status in (PlanGenerationResultStatus.TIMEOUT,
                                           PlanGenerationResultStatus.MEMOUT,
                                           PlanGenerationResultStatus.UNSUPPORTED_PROBLEM,
                                           PlanGenerationResultStatus.UNSOLVABLE_INCOMPLETELY), "invalid status")
        output += Warn(f"Unsolved ({result.status.name})")
    else:
        output += verify(result.status in (PlanGenerationResultStatus.UNSOLVABLE_PROVEN,
                                           PlanGenerationResultStatus.TIMEOUT,
                                           PlanGenerationResultStatus.MEMOUT,
                                           PlanGenerationResultStatus.UNSUPPORTED_PROBLEM,
                                           PlanGenerationResultStatus.UNSOLVABLE_INCOMPLETELY), "invalid status")

    return output


def run(planners: List[str], problems: List[TestCase], timeout=1) -> List[Tuple[str, str]]:
    errors = []
    for test_case in problems:
        print()
        print(test_case.name.ljust(40), end='\n')
        pb = test_case.problem

        for planner_id in planners:
            planner = OneshotPlanner(name=planner_id)
            if planner.supports(pb.kind):

                print("|  ", planner_id.ljust(40), end='')
                start = time.time()
                try:
                    result = planner.solve(pb, timeout=timeout)
                    end = time.time()
                    status = str(result.status.name).ljust(25)
                    outcome = check_result(test_case, result, planner)
                    if not outcome.ok():
                        errors.append((planner_id, test_case.name))
                    runtime = "{:.3f}s".format(end - start).ljust(10)
                    print(status, "    ", runtime, outcome)

                except Exception as e:
                    print(f"{bcolors.ERR}CRASH{bcolors.ENDC}", e)
                    errors.append((planner_id, test_case.name))
    return errors


def report(*planners: str, problem_prefix: str = ""):
    """Run all planners on all problems that start with the given prefix"""

    if len(planners) == 0:
        planners = oneshot_planners()

    problems = all_test_cases()
    problems = [p for p in problems if p.name.startswith(problem_prefix)]
    errors = run(planners, problems)
    if len(errors) > 0:
        print("Errors:\n ", "\n  ".join(map(str, errors)))
    return errors


if __name__ == "__main__":
    print("""Validate the results of solvers on a set of planning problems.
Usage
 - python report.py                          # will run all solvers on all all problems
 - python report.py aries tamer              # will run aries an tamer on all problems they support 
 - python report.py aries --prefix up:basic  # will run aries on all problems whose name starts with "up:basic" """)
    planners = sys.argv[1:]
    try:
        prefix_opt = planners.index("--prefix")
        planners.pop(prefix_opt)
        prefix = planners.pop(prefix_opt)
    except ValueError:
        prefix = ""

    errors = report(*planners, problem_prefix=prefix)
    if len(errors) > 0:
        sys.exit(1)


