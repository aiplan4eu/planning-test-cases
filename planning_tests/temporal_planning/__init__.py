from .pddl_problems.depots.depots import (
	depots_pfile1, depots_pfile2, depots_pfile3, depots_pfile10, depots_pfile11)


def problems():
    problems = {}
    problems['depots_pfile1'] = depots_pfile1(expected_version=1).get_problem()
    problems['depots_pfile2'] = depots_pfile2(expected_version=1).get_problem()
    problems['depots_pfile3'] = depots_pfile3(expected_version=1).get_problem()
    problems['depots_pfile10'] = depots_pfile10(expected_version=1).get_problem()
    problems['depots_pfile11'] = depots_pfile11(expected_version=1).get_problem()
    return problems