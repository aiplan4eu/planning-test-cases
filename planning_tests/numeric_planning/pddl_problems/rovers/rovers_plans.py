from unified_planning.io.pddl_reader import PDDLReader



class rovers_pfile3_bad_plan1(object):
    
    def __init__(self):
        self._pddl_plan = """(NAVIGATE ROVER1 WAYPOINT2 WAYPOINT3) 
   (NAVIGATE ROVER1 WAYPOINT3 WAYPOINT0) 
   (CALIBRATE ROVER1 CAMERA1 OBJECTIVE0 WAYPOINT0) 
   (TAKE_IMAGE ROVER1 WAYPOINT0 OBJECTIVE0 CAMERA1 COLOUR) 
   (SAMPLE_ROCK ROVER1 ROVER1STORE WAYPOINT0) 
   (NAVIGATE ROVER1 WAYPOINT0 WAYPOINT3) 
   (COMMUNICATE_IMAGE_DATA ROVER1 GENERAL OBJECTIVE0 COLOUR WAYPOINT3 WAYPOINT0) 
   (COMMUNICATE_ROCK_DATA ROVER1 GENERAL WAYPOINT0 WAYPOINT3 WAYPOINT0) """
        
    
    def get_plan(self,problem):
        reader = PDDLReader()
        plan = reader.parse_plan_string(problem, self._pddl_plan)
        
        return plan
