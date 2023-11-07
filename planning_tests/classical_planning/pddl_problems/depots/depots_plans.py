from unified_planning.io.pddl_reader import PDDLReader
from .depots import (
	depots_pfile1, depots_pfile2, depots_pfile3)


class depots_pfile1_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (lift hoist1 crate0 pallet1 distributor0)
        (load hoist0 crate1 truck1 depot0)
        (drive truck1 depot0 distributor1)
        (unload hoist2 crate0 truck0 distributor1)
        (unload hoist1 crate1 truck1 distributor0)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile1(expected_version=1).get_problem(), self._pddl_plan)

        return plan


class depots_pfile2_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (lift hoist0 crate0 pallet0 depot0)
        (load hoist2 crate2 truck1 distributor1)
        (load hoist0 crate0 truck1 depot0)
        (unload hoist0 crate2 truck1 depot0)
        (drop hoist0 crate2 pallet0 depot0)
        (load hoist2 crate1 truck1 distributor1)
        (unload hoist2 crate0 truck1 distributor1)
        (drop hoist2 crate0 pallet2 distributor1)
        (unload hoist1 crate1 truck1 distributor0)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile2(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    

class depots_pfile3_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (lift hoist0 crate0 pallet0 depot0)
        (load hoist2 crate2 truck1 distributor1)
        (load hoist0 crate0 truck1 depot0)
        (unload hoist0 crate2 truck1 depot0)
        (drop hoist0 crate2 pallet0 depot0)
        (load hoist2 crate1 truck1 distributor1)
        (unload hoist2 crate0 truck1 distributor1)
        (drop hoist2 crate0 pallet2 distributor1)
        (unload hoist1 crate1 truck1 distributor0)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(depots_pfile3(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    
