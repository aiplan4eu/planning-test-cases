
from unified_planning.environment import get_env
from unified_planning.shortcuts import OneshotPlanner


def get_planner_names(problem_kind):
    planner_names = [n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner()]

    executable_planners = []
    for p in planner_names:
        with OneshotPlanner(name=p) as planner:
            if planner.supports(problem_kind):
                executable_planners.append(p)

    return executable_planners