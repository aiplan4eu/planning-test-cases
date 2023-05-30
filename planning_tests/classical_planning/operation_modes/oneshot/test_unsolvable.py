import pytest

from planning_tests.classical_planning import UPBasicUnsolvable
from unified_planning.engines import PlanGenerationResultStatus
import unified_planning
from unified_planning.shortcuts import *

class TestUnsolvable:
    
    @pytest.mark.all
    @pytest.mark.simple 
    @pytest.mark.unsolvable
    def test_unsolvable_problem(self, oneshot_planner_name):
        problem = UPBasicUnsolvable(expected_version=1)
        up_problem = problem.get_problem()
        unified_planning.shortcuts.get_environment().credits_stream = None # silence credits
        with OneshotPlanner(name=oneshot_planner_name) as planner:
            if not planner.supports(up_problem.kind):
                pytest.skip("{} does not support problem kind".format(oneshot_planner_name))
            result = planner.solve(up_problem)
            assert result.status != PlanGenerationResultStatus.INTERNAL_ERROR
            # result status must reflect that there has no plan been found.
            assert result.status in (PlanGenerationResultStatus.TIMEOUT,
                                     PlanGenerationResultStatus.MEMOUT,
                                     PlanGenerationResultStatus.UNSUPPORTED_PROBLEM,
                                     PlanGenerationResultStatus.UNSOLVABLE_PROVEN,
                                     PlanGenerationResultStatus.UNSOLVABLE_INCOMPLETELY)
            assert not result.plan
