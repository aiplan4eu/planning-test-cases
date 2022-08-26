from unified_planning.environment import get_env

import pytest

def pytest_addoption(parser):
    parser.addoption("--planner_name", action="append", default=[], 
    help="add tests for this planner. Available values: a planner name or 'all'")


def pytest_generate_tests(metafunc):
    if "oneshot_planner_name" in metafunc.fixturenames:
        tags = set(metafunc.config.option.planner_name)
        if not tags or 'all' in tags:
            tags = [n for n in get_env().factory.engines]
        tags = [t for t in tags if get_env().factory.engine(t).is_oneshot_planner()]
        metafunc.parametrize("oneshot_planner_name", tags, scope='session')
