
from unified_planning.environment import get_env
from unified_planning.shortcuts import*


def get_planner_names(problem_kind):
    return [n for n, s in get_env().factory._engines.items() if s.is_oneshot_planner() and 
    s.supports(problem_kind) and n in ["lpg","enhsp"]]
    #["lpg","enhsp","pyperplan","tamer"]

def get_planner_names_opt(problem_kind):
        return [n for n, s in get_env().factory._engines.items() if s.is_oneshot_planner() and 
        s.supports(problem_kind) and n in ["enhsp-opt"]]

def get_anytime_names(problem_kind):
    return [n for n, s in get_env().factory._engines.items() if s.is_oneshot_planner() and 
    s.supports(problem_kind) and n in ["lpg-anytime"]]


