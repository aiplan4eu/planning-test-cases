# TODO test somewhere that presumably optimal planners declare themeselves such
import pytest

from planning_tests.multiagent_planning import UPDepot, UPLogistic, UPMABasic, UPTaxi
from unified_planning.engines import (
    OptimalityGuarantee,
    PlanGenerationResultStatus,
    ValidationResultStatus,
)

from unified_planning.shortcuts import *

unified_planning.shortcuts.get_environment().credits_stream = None  # silence credits


@pytest.fixture()
def is_simple(request):
    return "simple" in (m.name for m in request.node.own_markers)


@pytest.fixture(scope="class")
def result_cache():
    class ResultCache:
        def __init__(self):
            self._results = dict()

        def result(self, oneshot_planner_name, problem):
            if (oneshot_planner_name, problem) not in self._results:
                up_problem = problem.get_problem()
                with OneshotPlanner(name=oneshot_planner_name) as planner:
                    res = planner.solve(up_problem)
                    self._results[(oneshot_planner_name, problem)] = res
            return self._results[(oneshot_planner_name, problem)]

    return ResultCache()


basic = UPMABasic(expected_version=1)
depot = UPDepot(expected_version=1)
logistic = UPLogistic(expected_version=1)
taxi = UPTaxi(expected_version=1)


@pytest.mark.all
@pytest.mark.solvable
@pytest.mark.parametrize(
    "problem_name, problem, optimal_cost",
    [
        pytest.param("prob_basic", basic, 1, marks=pytest.mark.simple),
        pytest.param(
            "prob_depot", depot, 2, marks=[pytest.mark.medium, pytest.mark.depots]
        ),
        pytest.param(
            "prob_logistic",
            logistic,
            3,
            marks=[pytest.mark.medium, pytest.mark.logistic],
        ),
        pytest.param(
            "prob_taxi", taxi, 4, marks=[pytest.mark.medium, pytest.mark.taxi]
        ),
    ],
)
class TestSolvable:
    def test_plan_validates(
        self,
        oneshot_planner_name,
        problem_name,
        problem,
        optimal_cost,
        result_cache,
        is_simple,
    ):
        up_problem = problem.get_problem()
        planner = OneshotPlanner(name=oneshot_planner_name)
        if not planner.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(oneshot_planner_name))
        if not is_simple and planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
            pytest.skip("skip optimal planner on non-simple task")
        result = result_cache.result(oneshot_planner_name, problem)
        if not result.plan:
            pytest.skip("{} did not find a plan".format(oneshot_planner_name))

    def test_valid_result_status(
        self,
        oneshot_planner_name,
        problem_name,
        problem,
        optimal_cost,
        result_cache,
        is_simple,
    ):
        up_problem = problem.get_problem()
        planner = OneshotPlanner(name=oneshot_planner_name)
        if not planner.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(oneshot_planner_name))
        if not is_simple and planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
            pytest.skip("skip optimal planner on non-simple task")
        if problem_name == "prob_basic":
            result = planner.solve(up_problem, None, "1")
        else:
            result = result_cache.result(oneshot_planner_name, problem)
        if result.plan:
            assert result.status is PlanGenerationResultStatus.SOLVED_SATISFICING
        else:
            assert result.status != PlanGenerationResultStatus.INTERNAL_ERROR
            # We are only running the test on solvable instances
            assert result.status != PlanGenerationResultStatus.UNSOLVABLE_PROVEN
            assert result.status in (
                PlanGenerationResultStatus.TIMEOUT,
                PlanGenerationResultStatus.MEMOUT,
                PlanGenerationResultStatus.UNSUPPORTED_PROBLEM,
                PlanGenerationResultStatus.UNSOLVABLE_INCOMPLETELY,
            )
