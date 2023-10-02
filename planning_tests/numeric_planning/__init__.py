from .problems.problem_basic import UPBasic
from .problems.linear_effects import UPConditionalEffects
from .problems.complex_linear_conditions import (UPDisjunctiveConditions,UPExistentialConditions,UPUniversalConditions,UPComplexUniversalExistentialConditions)
from .problems.complex_nonlinear_conditions import (UPNonLinearDisjunctiveConditions,UPNonLinearExistentialConditions,UPNonLinearUniversalConditions)
from .problems.constant_additive_effects import (UPConstantIncreaseEffects,UPConstantDecreaseEffects)
from .problems.nonlinear_effects import (UPNonLinearIncreaseEffects,UPNonLinearAssignEffects,UPNonLinearConditionalEffects)
from .problems.simple_linear_conditions import (UPEqualityConditions,UPNegativeConditions,UPGreaterLowerConditions,UPGreaterThanConditions,UPLowerThanConditions)
from .problems.simple_nonlinear_conditions import (UPGreaterThanEqualityNonLinearConditions,UPLowerEqualNegativeNonLinearConditions)
from .pddl_problems.depots.depots import (
        depots_pfile1, depots_pfile2, depots_pfile3, depots_pfile10, depots_pfile11)
from .pddl_problems.rovers.rovers import (
	rovers_pfile2, rovers_pfile3, rovers_pfile4, rovers_pfile5)
from .pddl_problems.block_grouping.block_grouping import (
        block_grouping_5_5_2_1,
        block_grouping_5_5_2_2,
        block_grouping_5_5_2_3,
        block_grouping_11_10_2_2,
        block_grouping_20_25_6_2,
        block_grouping_20_25_6_3)
from .pddl_problems.farmland.farmland import (
       	farmland_2_100_1229,
        farmland_2_200_1229,
        farmland_2_300_1229,
        farmland_8_400_1229,
        farmland_10_400_1229,
        farmland_10_1000_1229)
from .pddl_problems.fn_counters.fn_counters import (
        fn_counters_2,
        fn_counters_4,
        fn_counters_8)
from .pddl_problems.plant_watering.plant_watering import (
       plant_watering_4_1,
        plant_watering_4_2,
        plant_watering_4_3)
from .pddl_problems.sailing.sailing import (
        sailing_1_1_1229,
        sailing_1_2_1229,
        sailing_1_3_1229,
        sailing_3_3_1229,
        sailing_4_10_1229)

def problems():
    problems = {}
    problems['depots_pfile1'] = depots_pfile1(expected_version=1).get_problem()
    problems['depots_pfile2'] = depots_pfile2(expected_version=1).get_problem()
    problems['depots_pfile3'] = depots_pfile3(expected_version=1).get_problem()
    problems['depots_pfile10'] = depots_pfile10(expected_version=1).get_problem()
    problems['depots_pfile11'] = depots_pfile11(expected_version=1).get_problem()
    problems['rovers_pfile2'] = rovers_pfile2(expected_version=1).get_problem()
    problems['rovers_pfile3'] = rovers_pfile3(expected_version=1).get_problem()
    problems['rovers_pfile4'] = rovers_pfile4(expected_version=1).get_problem()
    problems['rovers_pfile5'] = rovers_pfile5(expected_version=1).get_problem()
    problems['block_grouping_5_5_2_1'] = block_grouping_5_5_2_1(expected_version=1).get_problem()
    problems['block_grouping_5_5_2_2'] = block_grouping_5_5_2_2(expected_version=1).get_problem()
    problems['block_grouping_5_5_2_3'] = block_grouping_5_5_2_3(expected_version=1).get_problem()
    problems['block_grouping_11_10_2_2'] = block_grouping_11_10_2_2(expected_version=1).get_problem()
    problems['block_grouping_20_25_6_2'] = block_grouping_20_25_6_2(expected_version=1).get_problem()
    problems['block_grouping_20_25_6_3'] = block_grouping_20_25_6_3(expected_version=1).get_problem()
    problems['farmland_2_100_1229'] = farmland_2_100_1229(expected_version=1).get_problem()
    problems['farmland_2_200_1229'] = farmland_2_200_1229(expected_version=1).get_problem()
    problems['farmland_2_300_1229'] = farmland_2_300_1229(expected_version=1).get_problem()
    problems['farmland_8_400_1229'] = farmland_8_400_1229(expected_version=1).get_problem()
    problems['farmland_10_400_1229'] = farmland_10_400_1229(expected_version=1).get_problem()
    problems['farmland_10_1000_1229'] = farmland_10_1000_1229(expected_version=1).get_problem()
    problems['fn_counters_2'] = fn_counters_2(expected_version=1).get_problem()
    problems['fn_counters_4'] = fn_counters_4(expected_version=1).get_problem()
    problems['fn_counters_8'] = fn_counters_8(expected_version=1).get_problem()
    problems['plant_watering_4_1'] = plant_watering_4_1(expected_version=1).get_problem()
    problems['plant_watering_4_2'] = plant_watering_4_2(expected_version=1).get_problem()
    problems['plant_watering_4_3'] = plant_watering_4_3(expected_version=1).get_problem()
    problems['sailing_1_1_1229'] = sailing_1_1_1229(expected_version=1).get_problem()
    problems['sailing_1_2_1229'] = sailing_1_2_1229(expected_version=1).get_problem()
    problems['sailing_1_3_1229'] = sailing_1_3_1229(expected_version=1).get_problem()
    problems['sailing_3_3_1229'] = sailing_3_3_1229(expected_version=1).get_problem()
    problems['sailing_4_10_1229'] = sailing_4_10_1229(expected_version=1).get_problem()
    return problems

