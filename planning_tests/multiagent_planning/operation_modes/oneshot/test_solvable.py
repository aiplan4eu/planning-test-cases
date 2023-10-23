# TODO test somewhere that presumably optimal planners declare themeselves such
import pytest

from planning_tests.multiagent_planning import (
    UPDepot,
    UPLogistic,
    UPMABasic,
    UPTaxi,
    UPProcterAndGamble,
)
from unified_planning.engines import (
    OptimalityGuarantee,
    PlanGenerationResultStatus,
    ValidationResultStatus,
)

from unified_planning.shortcuts import *
import planning_tests.multiagent_planning.operation_modes.oneshot.convert_mapddl_to_pddl as mapddl_to_pddl
from unified_planning.io.ma_pddl_writer import MAPDDLWriter
from unified_planning.io.pddl_reader import PDDLReader
from unified_planning.plans.plan import ActionInstance
from unified_planning.plans.sequential_plan import SequentialPlan
from planning_tests.multiagent_planning.operation_modes.oneshot.ma_plan_convert import (
    PlanConverter,
)
import os

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
                    if up_problem.name == "prob_basic":
                        res = planner.solve(up_problem, None, "1")
                    else:
                        res = planner.solve(up_problem)
                    self._results[(oneshot_planner_name, problem)] = res
            return self._results[(oneshot_planner_name, problem)]

    return ResultCache()


basic = UPMABasic(expected_version=1)
depot = UPDepot(expected_version=1)
logistic = UPLogistic(expected_version=1)
taxi = UPTaxi(expected_version=1)
procter_gamble = UPProcterAndGamble(expected_version=1)


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
        pytest.param(
            "prob_procter_gamble",
            procter_gamble,
            5,
            marks=[pytest.mark.medium, pytest.mark.procter_gamble],
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
        if problem_name == "prob_basic":
            result = planner.solve(up_problem, None, "1")
        else:
            result = result_cache.result(oneshot_planner_name, problem)
        if not result.plan:
            pytest.skip("{} did not find a plan".format(oneshot_planner_name))

        w = MAPDDLWriter(up_problem, unfactored=True)
        w.write_ma_domain(f"unfactored_{up_problem.name}")
        w.write_ma_problem(f"unfactored_{up_problem.name}")

        domain_dir = f"ma_pddl_unfactored_{up_problem.name}"
        domain_file = f"{up_problem.name}_domain.pddl"
        problem_file = f"{up_problem.name}_problem.pddl"

        domain_path = os.path.join(domain_dir, domain_file)
        problem_path = os.path.join(domain_dir, problem_file)

        pp = mapddl_to_pddl.PlanningProblem(domain_path, problem_path)

        # Creating routes for new centralized PDDL archives
        centralized_dir = "centralized"
        new_domain_file = f"{up_problem.name}_domain.pddl"
        new_problem_file = f"{up_problem.name}_problem.pddl"

        new_domain_path = os.path.join(centralized_dir, new_domain_file)
        new_problem_path = os.path.join(centralized_dir, new_problem_file)

        # Make sure the directory exists, if it doesn't, create it
        if not os.path.exists(centralized_dir):
            os.makedirs(centralized_dir)

        pp.write_pddl_domain(new_domain_path)
        pp.write_pddl_problem(new_problem_path)

        reader = PDDLReader()
        pddl_problem = reader.parse_problem(
            os.path.abspath(new_domain_path), os.path.abspath(new_problem_path)
        )

        converter = PlanConverter(pddl_problem)

        for seq_plan in result.plan.all_sequential_plans():
            new_seq_plan = converter.convert_sequential_plan(seq_plan)
            with PlanValidator(problem_kind=pddl_problem.kind) as validator:
                check = validator.validate(pddl_problem, new_seq_plan)
                assert check.status is ValidationResultStatus.VALID

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
