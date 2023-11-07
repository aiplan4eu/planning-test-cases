from unified_planning.io.pddl_reader import PDDLReader
from .depots import (
	depots_pfile1, depots_pfile2, depots_pfile3, depots_pfile10, depots_pfile11)


class depots_pfile1_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        0.1: (lift hoist1 crate0 pallet1 distributor0) [1.1]
        43.0013: (drive truck1 depot0 distributor1) [0.875]
        """

    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile1(expected_version=1).get_problem(), self._pddl_plan)

        return plan


class depots_pfile2_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        0.0002: (lift hoist2 crate2 crate1 distributor1) [1.0]
        33.0008: (lift hoist2 crate1 pallet2 distributor1) [1.0]
        33.001: (drive truck0 distributor1 depot0) [3.3333]
        49.7798: (drive truck0 depot0 distributor1) [3.3333]
        54.4469: (unload hoist2 crate0 truck0 distributor1) [10.6667]
        54.4472: (drop hoist2 crate0 pallet2 distributor1) [1.0]
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile2(expected_version=1).get_problem(), self._pddl_plan)

        return plan
    

class depots_pfile3_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        0.0002: (lift hoist0 crate1 pallet0 depot0) [1.0]
        0.0002: (lift hoist2 crate5 crate2 distributor1) [1.0]
        1.1255: (load hoist0 crate1 truck1 depot0) [22.25]
        100.5295: (drive truck1 depot0 distributor1) [0.75]
        101.2798: (unload hoist2 crate0 truck1 distributor1) [16.5]
        41.552: (drive truck0 distributor0 distributor1) [0.375]
        41.552: (load hoist1 crate4 truck1 distributor0) [0.8]
        42.3525: (load hoist1 crate3 truck1 distributor0) [16.2]
        76.3871: (unload hoist0 crate2 truck0 depot0) [16.75]
        78.3535: (drop hoist1 crate4 pallet1 distributor0) [1.0]
        80.279: (unload hoist0 crate3 truck1 depot0) [20.25]
        80.2793: (drop hoist0 crate3 crate2 depot0) [1.0]
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile3(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    

class depots_pfile10_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """ 
        0.0002: (lift hoist5 crate3 crate2 distributor2) [1.0]
        0.0002: (lift hoist3 crate5 pallet3 distributor0) [1.0]
        0.0002: (lift hoist2 crate4 pallet2 depot2) [1.0]
        141.5032: (drive truck0 distributor0 depot0) [1.3333]
        29.2525: (drive truck1 distributor2 depot1) [3.0]
        3.8345: (drive truck1 depot2 distributor0) [3.5]
        32.2528: (load hoist1 crate0 truck1 depot1) [16.0]
        48.2533: (drive truck1 depot1 distributor2) [1.5]
        67.503: (drop hoist3 crate2 pallet3 distributor0) [1.0]
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile10(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    

class depots_pfile11_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        0.0002: (drive truck1 distributor0 depot0) [0.6667]
        0.0002: (lift hoist0 crate1 pallet0 depot0) [1.0]
        177.0015: (lift hoist2 crate4 crate2 depot2) [1.0]
        177.0017: (load hoist2 crate4 truck0 depot2) [61.0]
        312.0027: (drop hoist2 crate5 pallet2 depot2) [1.0]
        391.003: (drive truck0 depot2 distributor0) [0.8889]
        391.8921: (drive truck0 distributor0 distributor2) [0.7778]
        431.7283: (drop hoist0 crate4 pallet0 depot0) [1.0]
        446.9786: (drive truck0 depot0 distributor0) [0.8889]
        483.3557: (drive truck0 distributor2 distributor0) [0.5556]
        483.9116: (drive truck0 distributor0 depot2) [1.1111]
        485.0232: (drop hoist2 crate6 crate5 depot2) [1.0]
        486.0221: (drive truck1 depot1 distributor1) [1.1111]
        514.0234: (drive truck0 depot2 distributor1) [0.5556]
        98.001: (lift hoist2 crate5 crate4 depot2) [1.0]
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile11(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan


