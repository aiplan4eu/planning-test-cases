from unified_planning.io.pddl_reader import PDDLReader
from .fn_counters import (
	fn_counters_2, fn_counters_4, fn_counters_8)


class fn_counters_2_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (increment c0)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(fn_counters_2(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    

class fn_counters_4_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (increment c2)
        (increment c3)
        (increment c2)
        (increment c1)
        (decrement c2)
        (increment c2)
        (increment c2)
        (decrement c2)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(fn_counters_4(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    

class fn_counters_8_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
            (increment c6)
            (increment c5)
            (decrement c3)
            (decrement c5)
            (decrement c4)
            (increment c7)
            (increment c2)
            (increment c1)
            (increment c6)
            (increment c7)
            (increment c7)
            (decrement c6)
            (decrement c1)
            (decrement c2)
            (decrement c6)
            (increment c4)
            (increment c5)
            (increment c3)
            (increment c1)
            (increment c2)
            (decrement c6)
            (decrement c4)
            (decrement c2)
            (increment c6)
            (decrement c4)
            (increment c3)
            (increment c5)
            (increment c2)
            (decrement c1)
            (increment c2)
            (increment c4)
            (decrement c5)
            (increment c6)
            (increment c3)
            (decrement c4)
            (increment c5)
            (increment c6)
            (decrement c3)
            (increment c4)
            (decrement c5)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(fn_counters_8(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan