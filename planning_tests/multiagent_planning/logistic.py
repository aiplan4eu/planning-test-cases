import unified_planning
from unified_planning.shortcuts import *
from unified_planning.model.multi_agent import *
from planning_tests.commons.problem import TestCaseProblem


class TestCaseProblem(object):
    def __init__(self, expected_version):
        if expected_version != self.version():
            raise ValueError("Wrong version")
        pass

    def get_problem(self):
        raise NotImplementedError

    def get_description(self):
        raise NotImplementedError

    def version(self):
        raise NotImplementedError


class UPLogistic(TestCaseProblem):
    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        problem = MultiAgentProblem("ma-logistic")
        truck1 = Agent("truck1", problem)
        truck2 = Agent("truck2", problem)
        airplane = Agent("airplane", problem)
        object = UserType("object")
        location = UserType("location", object)
        vehicle = UserType("vehicle", object)
        package = UserType("package", object)
        city = UserType("city", object)
        airport = UserType("airport", location)

        pos = Fluent("pos", location=location)
        at = Fluent("at", BoolType(), object=object, location=location)
        In = Fluent("in", BoolType(), package=package, vehicle=vehicle)
        on = Fluent("on", BoolType(), object=object)
        in_city = Fluent("in_city", BoolType(), location=location, city=city)

        truck1.add_public_fluent(pos, default_initial_value=False)
        truck1.add_private_fluent(in_city, default_initial_value=False)
        truck1.add_public_fluent(on, default_initial_value=False)
        truck2.add_public_fluent(pos, default_initial_value=False)
        truck2.add_private_fluent(in_city, default_initial_value=False)
        truck2.add_public_fluent(on, default_initial_value=False)
        airplane.add_public_fluent(pos, default_initial_value=False)
        airplane.add_public_fluent(on, default_initial_value=False)
        problem.ma_environment.add_fluent(at, default_initial_value=False)
        problem.ma_environment.add_fluent(In, default_initial_value=False)

        load_truck = InstantaneousAction("load_truck", loc=location, obj=package)
        obj = load_truck.parameter("obj")
        loc = load_truck.parameter("loc")
        load_truck.add_precondition(at(obj, loc))
        load_truck.add_precondition(pos(loc))
        load_truck.add_effect(at(obj, loc), False)
        load_truck.add_effect(on(obj), True)

        unload_truck = InstantaneousAction("unload_truck", obj=package, loc=location)
        obj = unload_truck.parameter("obj")
        loc = unload_truck.parameter("loc")
        unload_truck.add_precondition(pos(loc))
        unload_truck.add_precondition(on(obj))
        unload_truck.add_effect(on(obj), False)
        unload_truck.add_effect(at(obj, loc), True)

        drive_truck = InstantaneousAction(
            "drive_truck", loc_from=location, loc_to=location, city_=city
        )
        loc_from = drive_truck.parameter("loc_from")
        loc_to = drive_truck.parameter("loc_to")
        city_ = drive_truck.parameter("city_")
        drive_truck.add_precondition(pos(loc_from))
        drive_truck.add_precondition(in_city(loc_from, city_))
        drive_truck.add_precondition(in_city(loc_to, city_))
        drive_truck.add_effect(pos(loc_from), False)
        drive_truck.add_effect(pos(loc_to), True)

        load_airplane = InstantaneousAction("load_airplane", loc=airport, obj=package)
        loc = load_airplane.parameter("loc")
        obj = load_airplane.parameter("obj")
        load_airplane.add_precondition(at(obj, loc))
        load_airplane.add_precondition(pos(loc))
        load_airplane.add_effect(at(obj, loc), False)
        load_airplane.add_effect(on(obj), True)

        unload_airplane = InstantaneousAction(
            "unload_airplane", loc=airport, obj=package
        )
        loc = load_airplane.parameter("loc")
        obj = load_airplane.parameter("obj")
        unload_airplane.add_precondition(on(obj))
        unload_airplane.add_precondition(pos(loc))
        unload_airplane.add_effect(on(obj), False)
        unload_airplane.add_effect(at(obj, loc), True)

        fly_airplane = InstantaneousAction(
            "fly_airplane", loc_from=airport, loc_to=airport
        )
        loc_from = fly_airplane.parameter("loc_from")
        loc_to = fly_airplane.parameter("loc_to")
        fly_airplane.add_precondition(pos(loc_from))
        fly_airplane.add_effect(pos(loc_from), False)
        fly_airplane.add_effect(pos(loc_to), True)

        truck1.add_action(drive_truck)
        truck1.add_action(unload_truck)
        truck1.add_action(load_truck)
        truck2.add_action(drive_truck)
        truck2.add_action(unload_truck)
        truck2.add_action(load_truck)
        airplane.add_action(load_airplane)
        airplane.add_action(unload_airplane)
        airplane.add_action(fly_airplane)
        problem.add_agent(truck1)
        problem.add_agent(truck2)
        problem.add_agent(airplane)

        obj21 = Object("obj21", package)
        obj22 = Object("obj22", package)
        obj23 = Object("obj23", package)
        obj11 = Object("obj11", package)
        obj13 = Object("obj13", package)
        obj12 = Object("obj12", package)
        apt2 = Object("apt2", airport)
        apt1 = Object("apt1", airport)
        pos1 = Object("pos1", location)
        cit1 = Object("cit1", city)
        pos2 = Object("pos2", location)
        cit2 = Object("cit2", city)

        problem.add_object(obj21)
        problem.add_object(obj22)
        problem.add_object(obj23)
        problem.add_object(obj11)
        problem.add_object(obj13)
        problem.add_object(obj12)
        problem.add_object(apt2)
        problem.add_object(apt1)
        problem.add_object(pos1)
        problem.add_object(cit1)
        problem.add_object(pos2)
        problem.add_object(cit2)

        problem.set_initial_value(Dot(truck1, pos(pos1)), True)
        problem.set_initial_value(at(obj11, pos1), True)
        problem.set_initial_value(at(obj12, pos1), True)
        problem.set_initial_value(at(obj13, pos1), True)
        problem.set_initial_value(Dot(truck1, in_city(pos1, cit1)), True)
        problem.set_initial_value(Dot(truck1, in_city(apt1, cit1)), True)
        problem.set_initial_value(Dot(truck1, pos(pos1)), True)
        problem.set_initial_value(Dot(truck2, pos(pos2)), True)
        problem.set_initial_value(at(obj21, pos2), True)
        problem.set_initial_value(at(obj22, pos2), True)
        problem.set_initial_value(at(obj23, pos2), True)
        problem.set_initial_value(Dot(truck2, in_city(pos2, cit2)), True)
        problem.set_initial_value(Dot(truck2, in_city(apt2, cit2)), True)
        problem.set_initial_value(Dot(truck2, pos(pos2)), True)
        problem.set_initial_value(Dot(airplane, pos(apt2)), True)
        problem.set_initial_value(at(obj11, pos1), True)
        problem.set_initial_value(at(obj12, pos1), True)
        problem.set_initial_value(at(obj13, pos1), True)
        problem.set_initial_value(Dot(airplane, pos(apt2)), True)

        problem.add_goal(at(obj11, apt1))
        problem.add_goal(at(obj23, pos1))
        problem.add_goal(at(obj13, apt1))
        problem.add_goal(at(obj21, pos1))
        return problem

    def get_description(self):
        return "logistic"

    def version(self):
        return 1