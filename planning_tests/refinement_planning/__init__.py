from planning_tests.refinement_planning import hddl, optimal


def problems():
    return optimal.problems() + hddl.problems()
