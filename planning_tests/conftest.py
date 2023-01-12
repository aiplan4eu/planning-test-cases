from unified_planning.environment import get_env
from unified_planning.engines.mixins.compiler import CompilationKind

import pytest

# TODO remove once in UPF
env = get_env()
env.factory.add_engine('fast-downward-grounder', "up_fast_downward", 'FastDownwardGrounder')

def pytest_addoption(parser):
    parser.addoption("--planner_name", action="append", default=[], 
    help="add tests for this planner. Available values: a planner name or 'all'")

    parser.addoption("--grounder_name", action="append", default=[], 
    help="add tests for this grounder. Available values: a grounder name or 'all'")

def pytest_generate_tests(metafunc):
    if "oneshot_planner_name" in metafunc.fixturenames:
        tags = set(metafunc.config.option.planner_name)
        if not tags or 'all' in tags:
            tags = [n for n in get_env().factory.engines]
        tags = [t for t in tags if get_env().factory.engine(t).is_oneshot_planner()]
        metafunc.parametrize("oneshot_planner_name", tags, scope='session')
    if "grounder_name" in metafunc.fixturenames:
        tags = set(metafunc.config.option.grounder_name)
        if not tags or 'all' in tags:
            tags = [n for n in get_env().factory.engines]
        tags = [t for t in tags if
                get_env().factory.engine(t).is_compiler() and
                get_env().factory.engine(t).supports_compilation(CompilationKind.GROUNDING)]
        metafunc.parametrize("grounder_name", tags, scope='session')
