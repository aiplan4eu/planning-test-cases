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
    pbs: list[TestCase] = []

    problems_dir = Path(__file__).parent.resolve() / "valid_problems"
    for file in problems_dir.iterdir():
        if file.is_file() and file.suffix == ".jsp":
            problem, plan, optimal = _parse(file)
            test_case = TestCase(
                problem,
                solvable=True,
                optimum=optimal,
                valid_plans=[plan],
                invalid_plans=[],  # TODO - Add invalid plans
            )
            pbs.append(test_case)

    return pbs


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
def _parse(filepath: Path) -> tuple[SchedulingProblem, SchedulingPlan, int]:
    """
    Parses the JobShop problem instance stored in the given file.

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
    Starts
    0 6 20 28
    3 15 25 30
    5 14 28 33
    0 3 6 15
    ```
    """

    # Read the file
    with open(filepath, mode="r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    # Get header data
    lines.pop(0)  # Remove the header
    num_jobs, num_machines, optimal = _parse_line(lines.pop(0))[0:3]

    # Get times
    lines.pop(0)  # Remove the header
    times = []
    for _ in range(num_jobs):
        times.append(_parse_line(lines.pop(0))[0:num_machines])

    # Get machines
    lines.pop(0)  # Remove the header
    machines = []
    for _ in range(num_jobs):
        machines.append(_parse_line(lines.pop(0))[0:num_machines])

    # Get starts
    lines.pop(0)  # Remove the header
    starts = []
    for _ in range(num_jobs):
        starts.append(_parse_line(lines.pop(0))[0:num_machines])

    # Create the problem and the plan data
    problem = SchedulingProblem(f"sched:jobshop:{filepath.name}")
    machine_objects = [
        problem.add_resource(f"M{i}", capacity=1) for i in range(1, num_machines + 1)
    ]

    timepoints = {}
    for job in range(num_jobs):
        previous_activity = None
        for task in range(num_machines):
            activity = problem.add_activity(
                f"T_{job+1}_{task+1}", duration=times[job][task]
            )
            machine = machine_objects[machines[job][task] - 1]
            activity.uses(machine)
            if previous_activity is not None:
                problem.add_constraint(LE(previous_activity.end, activity.start))
            previous_activity = activity
            timepoints[activity.start] = starts[job][task]
            timepoints[activity.end] = starts[job][task] + times[job][task]
    problem.add_quality_metric(MinimizeMakespan())

    # Create the plan
    plan = SchedulingPlan(problem.activities, timepoints)

    return problem, plan, optimal
