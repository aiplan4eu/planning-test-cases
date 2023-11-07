from .pddl_problems.depots.depots import (
	depots_pfile1, depots_pfile2, depots_pfile3, depots_pfile10, depots_pfile11)

from .pddl_problems.depots.depots_plans import (
        depots_pfile1_bad_plan1,
        depots_pfile2_bad_plan1,
        depots_pfile3_bad_plan1,
        depots_pfile10_bad_plan1,
        depots_pfile11_bad_plan1)


def problems():
    problems = {}
    problems['depots_pfile1'] = depots_pfile1(expected_version=1).get_problem()
    problems['depots_pfile2'] = depots_pfile2(expected_version=1).get_problem()
    problems['depots_pfile3'] = depots_pfile3(expected_version=1).get_problem()
    problems['depots_pfile10'] = depots_pfile10(expected_version=1).get_problem()
    problems['depots_pfile11'] = depots_pfile11(expected_version=1).get_problem()
    return problems


def plans():
    plans = {}
    plans['depots_pfile1_bad_plan1'] = depots_pfile1_bad_plan1(expected_version=1).get_plan()
    plans['depots_pfile2_bad_plan1'] = depots_pfile2_bad_plan1(expected_version=1).get_plan()
    plans['depots_pfile3_bad_plan1'] = depots_pfile3_bad_plan1(expected_version=1).get_plan()
    plans['depots_pfile10_bad_plan1'] = depots_pfile10_bad_plan1(expected_version=1).get_plan()
    plans['depots_pfile11_bad_plan1'] = depots_pfile11_bad_plan1(expected_version=1).get_plan()
    return plans