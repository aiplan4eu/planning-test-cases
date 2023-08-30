from pathlib import Path

from unified_planning.shortcuts import LE
from unified_planning.model.metrics import MinimizeMakespan
from unified_planning.model.scheduling import SchedulingProblem


def _parse_line(line: str) -> list[int]:
    """
    Parse a line of integers.

    # Example

    ``` python
    assert _parse_line("2 3 1 4") == [2, 3, 1, 4]
    ```
    """
    return list(map(int, line.rstrip().split()))


def _parse_problem(filepath: Path) -> SchedulingProblem:
    """
    Parses the JobShop instance stored in the given file.

    # Content example

    ```
    nb_jobs nb_machines
    6 6 0 0 0 0
    Times
    1 3 6 7 3 6
    8 5 10 10 10 4
    5 4 8 9 1 7
    5 5 5 3 8 9
    9 3 5 4 3 1
    3 3 9 10 4 1
    Machines
    3 1 2 4 6 5
    2 3 5 6 1 4
    3 4 6 1 2 5
    2 1 3 4 5 6
    3 2 5 6 1 4
    2 4 6 1 5 3
    ```
    """

    # Read the file
    with open(filepath, mode="r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    # Get header data
    lines.pop(0)  # Remove the header
    num_jobs, num_machines = _parse_line(lines.pop(0))[0:2]

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

    # Create the problem
    problem = SchedulingProblem(f"sched:jobshop:{filepath.name}")
    machine_objects = [
        problem.add_resource(f"M{i}", capacity=1) for i in range(1, num_machines + 1)
    ]

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
    problem.add_quality_metric(MinimizeMakespan())
    print(problem)
    return problem
