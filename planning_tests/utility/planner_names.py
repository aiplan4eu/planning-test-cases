
from unified_planning.environment import get_env
from unified_planning.shortcuts import*


def get_planner_names(problem_kind):
    return [n for n, s in get_env().factory._engines.items() if s.is_oneshot_planner() and 
    s.supports(problem_kind) and n in ["lpg","enhsp","pyperplan","tamer","fast-downward"]]
    #["lpg","enhsp","pyperplan","tamer"]

def anytime_names(problem_kind):
    return [n for n, s in get_env().factory.engines if s.is_oneshot_planner() and
    s.supports(problem_kind) and n in ["lpg-anytime"]]


