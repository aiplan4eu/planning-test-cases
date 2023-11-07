from unified_planning.io.pddl_reader import PDDLReader
from .tpp import (
	tpp_pfile1, tpp_pfile2, tpp_pfile3, tpp_pfile6)


class tpp_pfile1_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (buy truck1 goods1 market1 level0 level1 level0 level1)
        (load goods1 truck1 market1 level0 level1 level0 level1)
        (drive truck1 market1 depot1)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(tpp_pfile1(expected_version=1).get_problem(), self._pddl_plan)

        return plan


class tpp_pfile2_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (buy truck1 goods2 market1 level0 level1 level0 level1)
        (load goods1 truck1 market1 level0 level1 level0 level1)
        (drive truck1 market1 depot1)
        (drive truck1 depot1 market1)
        (drive truck1 market1 depot1)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(tpp_pfile2(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    

class tpp_pfile3_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (buy truck1 goods1 market1 level0 level1 level0 level1)
        (buy truck1 goods3 market1 level0 level1 level0 level1)
        (load goods1 truck1 market1 level0 level1 level0 level1)
        (drive truck1 market1 depot1)
        (unload goods2 truck1 depot1 level0 level1 level0 level1)
        (drive truck1 depot1 market1)
        (drive truck1 market1 depot1)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(tpp_pfile3(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    

class tpp_pfile6_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (drive truck1 depot1 market2)
        (drive truck1 market2 market1)
        (buy truck2 goods1 market1 level0 level1 level0 level1)
        (buy truck2 goods5 market1 level1 level2 level0 level1)
        (load goods1 truck2 market1 level0 level1 level0 level1)
        (buy truck2 goods2 market1 level0 level1 level1 level2)
        (load goods6 truck2 market1 level0 level1 level0 level1)
        (load goods2 truck1 market1 level1 level2 level0 level1)
        (drive truck2 market1 market2)
        (unload goods2 truck1 depot1 level0 level1 level0 level1)
        (unload goods4 truck2 depot1 level0 level1 level0 level1)
        (drive truck2 market2 market1)
        (drive truck2 market1 market2)
        (drive truck2 market2 depot1)
        (unload goods3 truck2 depot1 level0 level1 level0 level1)
        (drive truck2 market2 depot1)
        (unload goods1 truck2 depot1 level0 level1 level0 level1)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(tpp_pfile6(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    