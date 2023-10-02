from .problems.problem_basic import UPBasic
from .problems.problem_basic_unsolvable import UPBasicUnsolvable
from .problems.problem_conditional_effects import UPConditionalEffects
from .problems.problem_metric import UPCostMetricWithConstantCosts
from .problems.problem_metric import UPLengthMetric
from .pddl_problems.depots.depots import (
        depots_pfile1, depots_pfile2, depots_pfile3)
from .pddl_problems.tpp.tpp import (
        tpp_pfile1, tpp_pfile2, tpp_pfile3, tpp_pfile6)


def problems():
    problems = {}
    problems['depots_pfile1'] = depots_pfile1(expected_version=1).get_problem()
    problems['depots_pfile2'] = depots_pfile2(expected_version=1).get_problem()
    problems['depots_pfile3'] = depots_pfile3(expected_version=1).get_problem()
    problems['tpp_pfile1'] = tpp_pfile1(expected_version=1).get_problem()
    problems['tpp_pfile2'] = tpp_pfile2(expected_version=1).get_problem()
    problems['tpp_pfile3'] = tpp_pfile3(expected_version=1).get_problem()
    problems['tpp_pfile6'] = tpp_pfile6(expected_version=1).get_problem()
    return problems