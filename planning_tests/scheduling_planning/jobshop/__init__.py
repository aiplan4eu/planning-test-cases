from pathlib import Path

from unified_planning.model.metrics import MinimizeMakespan
from unified_planning.model.scheduling import SchedulingProblem
from unified_planning.plans import Schedule as SchedulingPlan
from unified_planning.shortcuts import LE

from planning_tests.commons.problem import TestCase


# ============================================================================ #
#                                   Problems                                   #
# ============================================================================ #


def problems() -> list[TestCase]:
    """
    Generates deterministically a set of JobShop problems with valid/invalid solutions and optimal.
    """
    folder = Path(__file__).parent.resolve() / "problems"
    return [_parse(file) for file in folder.iterdir()]


# ============================================================================ #
#                               JSP Files Parsing                              #
# ============================================================================ #


def _parse_line(line: str) -> list[int]:
    """
    Parse a line of integers.

    # Example

    ``` python
    assert _parse_line("2 3 1 4") == [2, 3, 1, 4]
    ```
    """
    return list(map(int, line.rstrip().split()))


# pylint: disable = too-many-locals
def _parse(filepath: Path) -> TestCase:
    """
    Parses the JobShop test case instance stored in the given file.

    # Content example

    ```
    nb_jobs nb_machines optimal
    4 4 37 0
    Times
    5 4 8 9
    5 5 5 3
    9 3 5 4
    3 3 9 10
    Machines
    3 4 1 2
    2 1 3 4
    3 2 1 4
    2 4 1 3
    Valid Plan
    0 6 20 28
    3 15 25 30
    5 14 28 33
    0 3 6 15
    Invalid Plan
    0 1 11 17
    3 11 16 26
    0 3 6 16
    1 17 26 36
    ```
    """

    # Read the file
    with open(filepath, mode="r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    # Get header data
    lines.pop(0)  # Remove the header
    nb_jobs, nb_machines, optimal = _parse_line(lines.pop(0))[0:3]

    # Get times
    lines.pop(0)  # Remove the header
    times = [_parse_line(lines.pop(0))[0:nb_machines] for _ in range(nb_jobs)]

    # Get machines
    lines.pop(0)  # Remove the header
    machines = [_parse_line(lines.pop(0))[0:nb_machines] for _ in range(nb_jobs)]

    # Get starts
    valid_starts, invalid_starts = [], []
    while len(lines) > 0 and "plan" in (header := lines.pop(0).lower()):
        starts = [_parse_line(lines.pop(0))[0:nb_machines] for _ in range(nb_jobs)]
        if "invalid" in header:
            invalid_starts.append(starts)
        elif "valid" in header:
            valid_starts.append(starts)
        else:
            raise ValueError(f"Cannot parse section with header '{header}'")

    # Create the problem
    problem = SchedulingProblem(f"sched:jobshop:{filepath.stem}")
    activities = []
    machine_objects = [
        problem.add_resource(f"M{i+1}", capacity=1) for i in range(nb_machines)
    ]

    for job in range(nb_jobs):
        previous_activity = None
        for task in range(nb_machines):
            activity = problem.add_activity(
                f"T_{job+1}_{task+1}",
                duration=times[job][task],
            )
            machine = machine_objects[machines[job][task] - 1]
            activity.uses(machine)
            if previous_activity is not None:
                problem.add_constraint(LE(previous_activity.end, activity.start))
            previous_activity = activity
            activities.append(activity)
    problem.add_quality_metric(MinimizeMakespan())

    # Create the plans
    valid_plans, invalid_plans = [], []
    for starts in valid_starts + invalid_starts:
        timepoints = {}
        k = 0
        for job in range(nb_jobs):
            for task in range(nb_machines):
                start = starts[job][task]
                end = start + times[job][task]
                activity = activities[k]
                timepoints[activity.start] = start
                timepoints[activity.end] = end
                k += 1
        plan = SchedulingPlan(activities, timepoints)
        if starts in valid_starts:
            valid_plans.append(plan)
        else:
            invalid_plans.append(plan)

    return TestCase(problem, True, optimal, valid_plans, invalid_plans)
