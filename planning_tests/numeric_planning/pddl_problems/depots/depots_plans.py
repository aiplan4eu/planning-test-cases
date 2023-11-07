from unified_planning.io.pddl_reader import PDDLReader
from .depots import (
	depots_pfile1, depots_pfile2, depots_pfile3, depots_pfile10, depots_pfile11)


class depots_pfile1_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (load hoist1 crate0 truck0 distributor0)
        (load hoist0 crate1 truck1 depot0)
        (drive truck1 depot0 distributor0)
        (unload hoist2 crate0 truck0 distributor1)
        (drop hoist2 crate0 pallet2 distributor1)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile1(expected_version=1).get_problem(), self._pddl_plan)

        return plan


class depots_pfile2_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (lift hoist2 crate2 crate1 distributor1)
        (drive truck1 depot0 distributor1)
        (load hoist0 crate0 truck0 depot0)
        (lift hoist2 crate1 pallet2 distributor1)
        (load hoist2 crate1 truck1 distributor1)
        (unload hoist2 crate0 truck0 distributor1)
        (unload hoist2 crate2 truck1 distributor1)
        (load hoist2 crate2 truck0 distributor1)
        (drive truck1 distributor1 depot0)
        (unload hoist1 crate1 truck1 distributor0)
        (drop hoist1 crate1 crate3 distributor0)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile2(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    

class depots_pfile3_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (lift hoist1 crate4 crate3 distributor0)
        (lift hoist2 crate5 crate2 distributor1)
        (drive truck0 depot0 distributor1)
        (load hoist1 crate4 truck1 distributor0)
        (load hoist2 crate5 truck0 distributor1)
        (lift hoist1 crate3 crate0 distributor0)
        (drive truck0 distributor1 depot0)
        (drop hoist1 crate3 crate0 distributor0)
        (lift hoist1 crate3 crate0 distributor0)
        (drop hoist1 crate3 crate0 distributor0)
        (drop hoist1 crate3 crate0 distributor0)
        (lift hoist1 crate3 crate0 distributor0)
        (drop hoist1 crate3 crate0 distributor0)
        (lift hoist1 crate3 crate0 distributor0)
        (drop hoist1 crate3 crate0 distributor0)
        (lift hoist1 crate0 pallet1 distributor0)
        (drive truck1 distributor0 distributor1)
        (unload hoist2 crate3 truck1 distributor1)
        (load hoist2 crate3 truck1 distributor1)
        (drive truck1 distributor1 depot0)
        (load hoist0 crate1 truck1 depot0)
        (unload hoist0 crate2 truck0 depot0)
        (drop hoist0 crate2 pallet0 depot0)
        (drive truck0 depot0 distributor1)
        (unload hoist0 crate1 truck1 depot0)
        (drive truck0 distributor1 depot0)
        (unload hoist1 crate1 truck1 distributor0)
        (drop hoist1 crate1 pallet1 distributor0)
        (lift hoist1 crate1 pallet1 distributor0)
        (load hoist1 crate1 truck1 distributor0)
        (unload hoist1 crate4 truck1 distributor0)
        (drop hoist1 crate4 pallet1 distributor0)
        (unload hoist1 crate1 truck1 distributor0)
        (drop hoist1 crate1 crate4 distributor0)
        (unload hoist0 crate1 truck1 depot0)
        (load hoist0 crate1 truck0 depot0)
        (drive truck1 depot0 distributor1)
        (drop hoist2 crate0 crate1 distributor1)
        (unload hoist2 crate5 truck1 distributor1)
        (drop hoist2 crate5 crate0 distributor1)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile3(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    

class depots_pfile10_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """ 
        (lift hoist5 crate3 crate2 distributor2)
        (lift hoist2 crate4 pallet2 depot2)
        (lift hoist0 crate1 pallet0 depot0)
        (load hoist2 crate4 truck1 depot2)
        (drive truck1 depot2 depot1)
        (load hoist1 crate4 truck0 depot1)
        (drive truck1 depot1 distributor2)
        (load hoist5 crate2 truck0 distributor2)
        (drop hoist5 crate4 pallet5 distributor2)
        (drive truck0 distributor2 distributor0)
        (unload hoist5 crate0 truck1 distributor2)
        (unload hoist3 crate2 truck0 distributor0)
        (drop hoist5 crate0 crate4 distributor2)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile10(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    

class depots_pfile11_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (lift hoist2 crate9 crate5 depot2)
        (drive truck1 distributor0 depot2)
        (lift hoist1 crate3 crate0 depot1)
        (lift hoist5 crate8 crate7 distributor2)
        (drop hoist2 crate5 crate4 depot2)
        (lift hoist2 crate5 crate4 depot2)
        (lift hoist2 crate5 crate4 depot2)
        (drop hoist2 crate5 crate4 depot2)
        (drop hoist1 crate3 crate0 depot1)
        (lift hoist1 crate3 crate0 depot1)
        (load hoist1 crate3 truck0 depot1)
        (lift hoist1 crate0 pallet1 depot1)
        (load hoist1 crate0 truck0 depot1)
        (drive truck0 depot1 distributor0)
        (drive truck0 distributor0 depot2)
        (load hoist2 crate0 truck1 depot2)
        (drive truck0 depot2 distributor2)
        (load hoist5 crate8 truck1 distributor2)
        (lift hoist5 crate7 crate6 distributor2)
        (load hoist5 crate7 truck1 distributor2)
        (load hoist5 crate6 truck1 distributor2)
        (unload hoist5 crate2 truck1 distributor2)
        (drop hoist5 crate2 pallet5 distributor2)
        (unload hoist5 crate5 truck1 distributor2)
        (lift hoist5 crate5 crate2 distributor2)
        (load hoist5 crate5 truck1 distributor2)
        (unload hoist5 crate9 truck0 distributor2)
        (drop hoist5 crate9 crate2 distributor2)
        (drive truck0 distributor2 depot0)
        (drop hoist0 crate7 crate1 depot0)
        (drive truck1 depot0 distributor0)
        (unload hoist3 crate8 truck1 distributor0)
        (lift hoist0 crate7 crate1 depot0)
        (drop hoist3 crate8 pallet3 distributor0)
        (drop hoist0 crate7 crate1 depot0)
        (drive truck1 distributor0 depot0)
        (load hoist0 crate7 truck1 depot0)
        (lift hoist0 crate1 pallet0 depot0)
        (unload hoist5 crate1 truck0 distributor2)
        (load hoist5 crate1 truck0 distributor2)
        (unload hoist5 crate1 truck0 distributor2)
        (load hoist5 crate1 truck0 distributor2)
        (unload hoist5 crate1 truck0 distributor2)
        (load hoist5 crate1 truck0 distributor2)
        (unload hoist5 crate1 truck0 distributor2)
        (load hoist5 crate1 truck0 distributor2)
        (unload hoist5 crate1 truck0 distributor2)
        (load hoist5 crate1 truck0 distributor2)
        (drive truck0 distributor2 distributor1)
        (lift hoist5 crate6 crate5 distributor2)
        (drive truck0 distributor2 distributor1)
        (unload hoist4 crate7 truck0 distributor1)
        (drive truck0 distributor1 depot2)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile11(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan


