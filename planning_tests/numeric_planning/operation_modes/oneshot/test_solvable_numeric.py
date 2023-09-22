# TODO test somewhere that presumably optimal planners declare themeselves such
import pytest

from planning_tests.numeric_planning import (
        UPBasic,
        UPDisjunctiveConditions,
        UPExistentialConditions,
        UPUniversalConditions,
        UPComplexUniversalExistentialConditions,
        UPNonLinearDisjunctiveConditions,
        UPNonLinearExistentialConditions,
        UPNonLinearUniversalConditions,
        UPConstantIncreaseEffects,
        UPConstantDecreaseEffects,
        UPConditionalEffects,
        UPNonLinearIncreaseEffects,
        UPNonLinearAssignEffects,
        UPNonLinearConditionalEffects,
        UPEqualityConditions,
        UPNegativeConditions,
        UPGreaterLowerConditions,
        UPGreaterThanConditions,
        UPLowerThanConditions,
        UPGreaterThanEqualityNonLinearConditions,
        UPLowerEqualNegativeNonLinearConditions,
        depots_pfile1,
        depots_pfile2,
        depots_pfile3,
        depots_pfile10,
        depots_pfile11,
        rovers_pfile2,
        rovers_pfile3,
        rovers_pfile4,
        rovers_pfile5,
        block_grouping_5_5_2_1,
        block_grouping_5_5_2_2,
        block_grouping_5_5_2_3,
        block_grouping_11_10_2_2,
        block_grouping_20_25_6_2,
        block_grouping_20_25_6_3,
        farmland_2_100_1229,
        farmland_2_200_1229,
        farmland_2_300_1229,
        farmland_8_400_1229,
        farmland_10_400_1229,
        farmland_10_1000_1229,
        fn_counters_2,
        fn_counters_4,
        fn_counters_8,
        plant_watering_4_1,
        plant_watering_4_2,
        plant_watering_4_3,
        sailing_1_1_1229,
        sailing_1_2_1229,
        sailing_1_3_1229,
        sailing_3_3_1229,
        sailing_4_10_1229,
        )
from unified_planning.engines import (OptimalityGuarantee,
        PlanGenerationResultStatus, ValidationResultStatus)

from unified_planning.shortcuts import *

unified_planning.shortcuts.get_environment().credits_stream = None # silence credits


@pytest.fixture()
def is_simple(request):
    return "simple" in  (m.name for m in request.node.own_markers)

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


basic = UPBasic(expected_version=1)
disjunctive_conditions = UPDisjunctiveConditions(expected_version=1)
existential_conditions = UPExistentialConditions(expected_version=1)
universal_conditions = UPUniversalConditions(expected_version=1)
universal_existential_conditions = UPComplexUniversalExistentialConditions(expected_version=1)
nonlinear_disjunctive_conditions = UPNonLinearDisjunctiveConditions(expected_version=1)
nonlinear_existential_conditions = UPNonLinearExistentialConditions(expected_version=1)
nonlinear_universal_conditions = UPNonLinearUniversalConditions(expected_version=1)
increase_effects = UPConstantIncreaseEffects(expected_version=1)
decrease_effects = UPConstantDecreaseEffects(expected_version=1)
conditional_effects = UPConditionalEffects(expected_version=1)
nonlinear_increase_effects = UPNonLinearIncreaseEffects(expected_version=1)
nonlinear_assign_continuous_effects = UPNonLinearAssignEffects(expected_version=1)
nonlinear_assign_conditional_effects = UPNonLinearConditionalEffects(expected_version=1)
equality_conditions = UPEqualityConditions(expected_version=1)
negative_conditions = UPNegativeConditions(expected_version=1)
greater_lower_conditions = UPGreaterLowerConditions(expected_version=1)
lower_than_conditions = UPGreaterThanConditions(expected_version=1)
greater_than_conditions = UPLowerThanConditions(expected_version=1)
gt_equality_nonlinear_conditions = UPGreaterThanEqualityNonLinearConditions(expected_version=1)
le_negative_nonlinear_conditions = UPLowerEqualNegativeNonLinearConditions(expected_version=1)
depots_pfile1 = depots_pfile1(expected_version=1)
depots_pfile2 = depots_pfile2(expected_version=1)
depots_pfile3 = depots_pfile3(expected_version=1)
depots_pfile10 = depots_pfile10(expected_version=1)
depots_pfile11 = depots_pfile11(expected_version=1)
rovers_pfile2 = rovers_pfile2(expected_version=1)
rovers_pfile3 = rovers_pfile3(expected_version=1)
rovers_pfile4 = rovers_pfile4(expected_version=1)
rovers_pfile5 = rovers_pfile5(expected_version=1)
block_grouping_5_5_2_1 = block_grouping_5_5_2_1(expected_version=1)
block_grouping_5_5_2_2 = block_grouping_5_5_2_2(expected_version=1)
block_grouping_5_5_2_3 = block_grouping_5_5_2_3(expected_version=1)
block_grouping_11_10_2_2 = block_grouping_11_10_2_2(expected_version=1)
block_grouping_20_25_6_2 = block_grouping_20_25_6_2(expected_version=1)
block_grouping_20_25_6_3 = block_grouping_20_25_6_3(expected_version=1)
farmland_2_100_1229 = farmland_2_100_1229(expected_version=1)
farmland_2_200_1229 = farmland_2_200_1229(expected_version=1)
farmland_2_300_1229 = farmland_2_300_1229(expected_version=1)
farmland_8_400_1229 = farmland_8_400_1229(expected_version=1)
farmland_10_400_1229 = farmland_10_400_1229(expected_version=1)
farmland_10_1000_1229 = farmland_10_1000_1229(expected_version=1)
fn_counters_2 = fn_counters_2(expected_version=1)
fn_counters_4 = fn_counters_4(expected_version=1)
fn_counters_8 = fn_counters_8(expected_version=1)
plant_watering_4_1 = plant_watering_4_1(expected_version=1)
plant_watering_4_2 = plant_watering_4_2(expected_version=1)
plant_watering_4_3 = plant_watering_4_3(expected_version=1)
sailing_1_1_1229 = sailing_1_1_1229(expected_version=1)
sailing_1_2_1229 = sailing_1_2_1229(expected_version=1)
sailing_1_3_1229 = sailing_1_3_1229(expected_version=1)
sailing_3_3_1229 = sailing_3_3_1229(expected_version=1)
sailing_4_10_1229 = sailing_4_10_1229(expected_version=1)


@pytest.mark.all
@pytest.mark.solvable
@pytest.mark.numeric
@pytest.mark.parametrize("problem_name, problem, optimal_cost",
    [
        pytest.param('prob_basic', basic, 1, marks=pytest.mark.simple),
        pytest.param('prob_cond_effects', conditional_effects, 2, marks=pytest.mark.simple),
        pytest.param('prob_disj_conditions', disjunctive_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.complex_conditions]),
        pytest.param('prob_exis_conditions', existential_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.complex_conditions]),
        pytest.param('prob_univ_conditions', universal_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.complex_conditions]),
        pytest.param('prob_univ_exis_conditions', universal_existential_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.complex_conditions]),
        pytest.param('prob_nonlinear_disj_conditions', nonlinear_disjunctive_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.complex_nonlinear_conditions]),
        pytest.param('prob_nonlinear_exis_conditions', nonlinear_existential_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.complex_nonlinear_conditions]),
        pytest.param('prob_nonlinear_univ_conditions', nonlinear_universal_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.complex_nonlinear_conditions]),
        pytest.param('prob_increase_effects', increase_effects, 1,
            marks=[pytest.mark.simple,pytest.mark.constant_additive_effects]),
        pytest.param('prob_decrease_effects', decrease_effects, 2,
            marks=[pytest.mark.simple,pytest.mark.constant_additive_effects]),
        pytest.param('prob_nonlinear_increase_effects', nonlinear_increase_effects, None,
            marks=[pytest.mark.simple,pytest.mark.nonlinear_effects]),
        pytest.param('prob_nonlinear_assign_cont_effects', nonlinear_assign_continuous_effects, None,
            marks=[pytest.mark.simple,pytest.mark.nonlinear_effects]),         
        pytest.param('prob_nonlinear_assign_conditional_effects', nonlinear_assign_conditional_effects, None,
            marks=[pytest.mark.simple,pytest.mark.nonlinear_effects]),
        pytest.param('prob_eq_conditions', equality_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.simple_linear_conditions]),
        pytest.param('prob_neg_conditions', negative_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.simple_linear_conditions]), 
        pytest.param('prob_gt_lw_conditions', greater_lower_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.simple_linear_conditions]), 
        pytest.param('prob_lw_conditions', lower_than_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.simple_linear_conditions]), 
        pytest.param('prob_gt_conditions', greater_than_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.simple_linear_conditions]),
        pytest.param('prob_gt_eq_nonlinear_conditions', gt_equality_nonlinear_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.simple_nonlinear_conditions]),   
        pytest.param('prob_le_negative_nonlinear_conditions', le_negative_nonlinear_conditions, None,
            marks=[pytest.mark.simple,pytest.mark.simple_nonlinear_conditions]),      
        pytest.param("depots_pfile1", depots_pfile1, 10,
            marks=[pytest.mark.simple, pytest.mark.depots]),
        pytest.param("depots_pfile2", depots_pfile2, 15,
            marks=[pytest.mark.simple, pytest.mark.depots]),
        pytest.param("depots_pfile3", depots_pfile3, 27,
            marks=[pytest.mark.simple, pytest.mark.depots]),
        pytest.param("depots_pfile10", depots_pfile10, None,
            marks=[pytest.mark.medium, pytest.mark.depots]),
        pytest.param("depots_pfile11", depots_pfile11, None,
            marks=[pytest.mark.medium, pytest.mark.depots]),
        pytest.param("rovers_pfile2", rovers_pfile2, 8,
            marks=[pytest.mark.simple, pytest.mark.rovers]),
        pytest.param("rovers_pfile3", rovers_pfile3, 11,
            marks=[pytest.mark.simple, pytest.mark.rovers]),
        pytest.param("rovers_pfile4", rovers_pfile4, 8,
            marks=[pytest.mark.simple, pytest.mark.rovers]),
        pytest.param("rovers_pfile5", rovers_pfile2, None,
            marks=[pytest.mark.medium, pytest.mark.rovers]),
        pytest.param("block_grouping_5_5_2_1", block_grouping_5_5_2_1, None,
            marks=[pytest.mark.simple, pytest.mark.block_grouping]),
        pytest.param("block_grouping_5_5_2_2", block_grouping_5_5_2_2, None,
            marks=[pytest.mark.simple, pytest.mark.block_grouping]),
        pytest.param("block_grouping_5_5_2_3", block_grouping_5_5_2_3, None,
            marks=[pytest.mark.simple, pytest.mark.block_grouping]),
        pytest.param("block_grouping_11_10_2_2", block_grouping_11_10_2_2, None,
            marks=[pytest.mark.simple, pytest.mark.block_grouping]),
        pytest.param("block_grouping_20_25_6_2", block_grouping_20_25_6_2, None,
            marks=[pytest.mark.medium, pytest.mark.block_grouping]),
        pytest.param("block_grouping_20_25_6_3", block_grouping_20_25_6_3, None,
            marks=[pytest.mark.medium, pytest.mark.block_grouping]),
        pytest.param("farmland_2_100_1229", farmland_2_100_1229, None,
            marks=[pytest.mark.simple, pytest.mark.farmland]),
        pytest.param("farmland_2_200_1229", farmland_2_200_1229, None,
            marks=[pytest.mark.simple, pytest.mark.farmland]),
        pytest.param("farmland_2_300_1229", farmland_2_300_1229, None,
            marks=[pytest.mark.simple, pytest.mark.farmland]),
        pytest.param("farmland_8_400_1229", farmland_8_400_1229, None,
            marks=[pytest.mark.simple, pytest.mark.farmland]),
        pytest.param("farmland_10_400_1229", farmland_10_400_1229, None,
            marks=[pytest.mark.simple, pytest.mark.farmland]),
        pytest.param("farmland_10_1000_1229", farmland_10_1000_1229, None,
            marks=[pytest.mark.simple, pytest.mark.farmland]),
        pytest.param("fn_counters_2", fn_counters_2, None,
            marks=[pytest.mark.simple, pytest.mark.fn_counters]),
        pytest.param("fn_counters_4", fn_counters_4, None,
            marks=[pytest.mark.simple, pytest.mark.fn_counters]),
        pytest.param("fn_counters_8", fn_counters_8, None,
            marks=[pytest.mark.simple, pytest.mark.fn_counters]),
        pytest.param("plant_watering_4_1", plant_watering_4_1, None,
            marks=[pytest.mark.simple, pytest.mark.plant_watering]),
        pytest.param("plant_watering_4_2", plant_watering_4_2, None,
            marks=[pytest.mark.simple, pytest.mark.plant_watering]),
        pytest.param("plant_watering_4_3", plant_watering_4_3, None,
            marks=[pytest.mark.simple, pytest.mark.plant_watering]),
        pytest.param("sailing_1_1_1229", sailing_1_1_1229, None,
            marks=[pytest.mark.simple, pytest.mark.sailing]),
        pytest.param("sailing_1_2_1229", sailing_1_2_1229, None,
            marks=[pytest.mark.simple, pytest.mark.sailing]),
        pytest.param("sailing_1_3_1229", sailing_1_3_1229, None,
            marks=[pytest.mark.simple, pytest.mark.sailing]),
        pytest.param("sailing_3_3_1229", sailing_3_3_1229, None,
            marks=[pytest.mark.simple, pytest.mark.sailing]),
        pytest.param("sailing_4_10_1229", sailing_4_10_1229, None,
            marks=[pytest.mark.medium, pytest.mark.sailing]),


    ])
class TestSolvable:

    def test_plan_validates(self, oneshot_planner_name, problem_name, problem,
            optimal_cost, result_cache, is_simple):
        up_problem = problem.get_problem()
        planner = OneshotPlanner(name=oneshot_planner_name)
        if not planner.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(oneshot_planner_name))
        if not is_simple and planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
            pytest.skip("skip optimal planner on non-simple task")
        result = result_cache.result(oneshot_planner_name, problem)
        if not result.plan:
            pytest.skip("{} did not find a plan".format(oneshot_planner_name))
        # The plan validator does not support metrics, so we remove this part
        # from the instance
        # TODO remove workaraound once resolved in UP
        metrics = up_problem.quality_metrics
        validation_problem = up_problem
        if metrics:
            validation_problem = validation_problem.clone()
            validation_problem.clear_quality_metrics()
       
        with PlanValidator(problem_kind=validation_problem.kind) as validator:
            check = validator.validate(validation_problem, result.plan)
            assert check.status is ValidationResultStatus.VALID

    def test_optimal_quality(self, oneshot_planner_name, problem_name, problem,
                             optimal_cost, result_cache, is_simple):
        up_problem = problem.get_problem()
        planner = OneshotPlanner(name=oneshot_planner_name)
        if not planner.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(oneshot_planner_name))
        if not is_simple and planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
            pytest.skip("skip optimal planner on non-simple task")
        result = result_cache.result(oneshot_planner_name, problem)
        if result.status is not PlanGenerationResultStatus.SOLVED_OPTIMALLY:
            pytest.skip("{} does not claim solution to be optimal".format(oneshot_planner_name))
        if optimal_cost is not None:
            metrics = up_problem.quality_metrics
            if metrics:
                assert len(metrics) == 1 # this is not a test assertion
                # but asserts the scope of this test function

                # another assertion for the scope of this util
                # function; not testing the planner
                assert (isinstance(metrics[0], up.model.metrics.MinimizeActionCosts)  or
                        isinstance(metrics[0], up.model.metrics.MinimizeSequentialPlanLength))

                if isinstance(metrics[0], up.model.metrics.MinimizeActionCosts):
                    cost_function = metrics[0].costs
                    default = metrics[0].default
                    cost = sum(cost_function.get(a.action, default).constant_value()
                               for a in result.plan.actions)
                    assert cost == optimal_cost
            else:
                assert optimal_cost == len(result.plan.actions)

    def test_valid_result_status(self, oneshot_planner_name, problem_name,
            problem, optimal_cost, result_cache, is_simple):
        up_problem = problem.get_problem()
        planner = OneshotPlanner(name=oneshot_planner_name)
        if not planner.supports(up_problem.kind):
            pytest.skip("{} does not support problem kind".format(oneshot_planner_name))
        if not is_simple and planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
            pytest.skip("skip optimal planner on non-simple task")
        result = result_cache.result(oneshot_planner_name, problem)
        if result.plan:
            # if the planner guarantees optimality, this should be reflected in
            # the result status
            metrics = up_problem.quality_metrics
            if not metrics:
                assert result.status is PlanGenerationResultStatus.SOLVED_SATISFICING
            else:
                if planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
                    assert result.status is PlanGenerationResultStatus.SOLVED_OPTIMALLY
                else:
                    assert result.status in (PlanGenerationResultStatus.SOLVED_OPTIMALLY,
                                             PlanGenerationResultStatus.SOLVED_SATISFICING)
        else:
            assert result.status != PlanGenerationResultStatus.INTERNAL_ERROR
            # We are only running the test on solvable instances
            assert result.status != PlanGenerationResultStatus.UNSOLVABLE_PROVEN
            assert result.status in (PlanGenerationResultStatus.TIMEOUT,
                                     PlanGenerationResultStatus.MEMOUT,
                                     PlanGenerationResultStatus.UNSUPPORTED_PROBLEM,
                                     PlanGenerationResultStatus.UNSOLVABLE_INCOMPLETELY)
