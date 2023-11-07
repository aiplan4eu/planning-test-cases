from unified_planning.io.pddl_reader import PDDLReader
from .rovers import (
	rovers_pfile2, rovers_pfile3, rovers_pfile4, rovers_pfile5)


class rovers_pfile2_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """(NAVIGATE ROVER0 WAYPOINT2 WAYPOINT3) 
   (NAVIGATE ROVER0 WAYPOINT3 WAYPOINT0) 
   (CALIBRATE ROVER0 CAMERA1 OBJECTIVE0 WAYPOINT0) 
   (TAKE_IMAGE ROVER0 WAYPOINT0 OBJECTIVE0 CAMERA1 COLOUR) 
   (SAMPLE_ROCK ROVER0 ROVER0STORE WAYPOINT0) 
   (NAVIGATE ROVER0 WAYPOINT0 WAYPOINT3) 
   (COMMUNICATE_IMAGE_DATA ROVER0 GENERAL OBJECTIVE0 COLOUR WAYPOINT3 WAYPOINT0) 
   (COMMUNICATE_ROCK_DATA ROVER0 GENERAL WAYPOINT0 WAYPOINT3 WAYPOINT0) """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(rovers_pfile2(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan


class rovers_pfile3_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """
        (navigate rover1 waypoint3 waypoint0)
        (calibrate rover1 camera1 objective0 waypoint0)
        (sample_rock rover0 rover0store waypoint0)
        (navigate rover1 waypoint0 waypoint3)
        (communicate_rock_data rover0 general waypoint0 waypoint1 waypoint0)
        (communicate_soil_data rover1 general waypoint2 waypoint2 waypoint0)
        (navigate rover1 waypoint2 waypoint3)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(rovers_pfile3(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan


class rovers_pfile4_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """(sample_soil rover0 rover0store waypoint3)
        (sample_rock rover1 rover1store waypoint1)
        (communicate_rock_data rover1 general waypoint1 waypoint1 waypoint2)
        (calibrate rover1 camera0 objective0 waypoint1)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(rovers_pfile4(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan
    

class rovers_pfile5_bad_plan1(object):
    
    def __init__(self, expected_version=1):
        self._pddl_plan = """ (sample_rock rover0 rover0store waypoint0)
        (calibrate rover1 camera1 objective1 waypoint0)
        (take_image rover1 waypoint0 objective0 camera1 high_res)
        (communicate_image_data rover1 general objective0 high_res waypoint0 waypoint3)
        (take_image rover0 waypoint0 objective0 camera2 colour)
        (communicate_soil_data rover1 general waypoint1 waypoint1 waypoint3)
        (communicate_image_data rover0 general objective2 high_res waypoint0 waypoint3)
        (navigate rover1 waypoint1 waypoint2)
        (navigate rover1 waypoint2 waypoint1)
        (communicate_soil_data rover1 general waypoint2 waypoint1 waypoint3)
        (navigate rover0 waypoint1 waypoint0)
        """
        
    def get_plan(self):
        reader = PDDLReader()
        plan = reader.parse_plan_string(rovers_pfile5(expected_version=1).get_problem(), self._pddl_plan)
        
        return plan