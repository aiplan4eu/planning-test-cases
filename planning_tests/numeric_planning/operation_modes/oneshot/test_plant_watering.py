import unified_planning
from unified_planning.shortcuts import *
from planning_tests.numeric_planning.pddl_problems.plant_watering.plant_watering import plant_watering_4_1, plant_watering_4_2, plant_watering_4_3
import pytest
from planning_tests.utility.util import TestUtil
from planning_tests.utility.planner_names import get_planner_names


class TestPlantWatering:

 
	plant_watering_4_1 = plant_watering_4_1(expected_version=1)
	plant_watering_4_2 = plant_watering_4_2(expected_version=1)
	plant_watering_4_3 = plant_watering_4_3(expected_version=1)
	

	#we check only the first problem, since the domain is the same for all the problems
	planner_names = get_planner_names(plant_watering_4_1.get_problem().kind)
	
	@pytest.mark.parametrize("planner_name",planner_names)
	@pytest.mark.parametrize("problem_name,problem",[("plant_watering_4_1",plant_watering_4_1),
	("plant_watering_4_2",plant_watering_4_2),
	("plant_watering_4_3",plant_watering_4_3)])
	def test_plant_watering(self,planner_name,problem_name,problem):
		TestUtil.execute_one_shot_planning_test(problem.get_problem(),[problem_name +'.pddl'],planner_name)

	