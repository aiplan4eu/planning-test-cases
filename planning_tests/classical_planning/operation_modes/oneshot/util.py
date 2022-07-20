import unified_planning
from unified_planning.shortcuts import *
from unified_planning.engines import OptimalityGuarantee, PlanGenerationResultStatus
from unified_planning.engines import ValidationResultStatus

from unittest import TestCase, main


def run_all_oneshot_planners_on_solvable_problem(up_problem, optimal_cost=None):
    unified_planning.shortcuts.get_env().credits_stream = None # silence credits

    optimal = OptimalityGuarantee.SOLVED_OPTIMALLY
    factory = get_env().factory
    planner_names_with_guarantee = [(n, factory.engine(n).satisfies(optimal))
                                    for n in get_env().factory.engines
                                    if factory.engine(n).is_oneshot_planner()]

    for p, guarantees_optimality in planner_names_with_guarantee:
        with OneshotPlanner(name=p) as planner:
            if planner.supports(up_problem.kind):
                print(p)

                # verify that an optimal planner gives this optimality
                # guarantee
                if guarantees_optimality:
                    assert planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY)
                result = planner.solve(up_problem)
                if result.plan:
                    # verify that the plan is valid
                    # The plan validator does not support metrics, so we remove
                    # this part from the instance
                    # TODO remove workaraound once resolved in UP
                    metrics = up_problem.quality_metrics
                    validation_problem = up_problem
                    if metrics:
                        validation_problem = validation_problem.clone()
                        validation_problem.clear_quality_metrics()
                    
                    with PlanValidator(problem_kind=validation_problem.kind) as validator:
                        check = validator.validate(validation_problem, result.plan)
                        assert check.status is ValidationResultStatus.VALID

                    # if the planner guarantees optimality, this should be
                    # reflected in the result status
                    if planner.satisfies(OptimalityGuarantee.SOLVED_OPTIMALLY):
                        assert result.status is PlanGenerationResultStatus.SOLVED_OPTIMALLY

                    # if the plan is marked as optimal, we compare the solution
                    # quality with the known solution cost
                    if result.status is PlanGenerationResultStatus.SOLVED_OPTIMALLY:
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
                else:
                    assert result.status != PlanGenerationResultStatus.INTERNAL_ERROR
                    # result status must reflect that there is no plan
                    assert result.status in (PlanGenerationResultStatus.UNSOLVABLE_PROVEN,
                                             PlanGenerationResultStatus.UNSOLVABLE_INCOMPLETELY)
                    # There cannot be proven unsolvability for a solvable instance
                    # (scope of this test)
                    assert result.status != PlanGenerationResultStatus.UNSOLVABLE_PROVEN


def run_all_oneshot_planners_on_unsolvable_problem(up_problem):
    unified_planning.shortcuts.get_env().credits_stream = None # silence credits
    factory = get_env().factory
    planner_names = [n for n in get_env().factory.engines
                       if factory.engine(n).is_oneshot_planner()]
    for p in planner_names:
        print(p)
        with OneshotPlanner(name=p) as planner:
            if planner.supports(up_problem.kind):

                result = planner.solve(up_problem)
                assert result.status != PlanGenerationResultStatus.INTERNAL_ERROR
                # result status must reflect that there is no plan
                assert result.status in (PlanGenerationResultStatus.UNSOLVABLE_PROVEN,
                                         PlanGenerationResultStatus.UNSOLVABLE_INCOMPLETELY)
                assert not result.plan
