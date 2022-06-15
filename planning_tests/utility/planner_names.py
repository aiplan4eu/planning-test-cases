
from unified_planning.environment import get_env
from unified_planning.shortcuts import OneshotPlanner


def get_planner_names(problem_kind):

    return [n for n, s in get_env().factory.solvers.items() if s.is_oneshot_planner() and
    s.supports(problem_kind)]