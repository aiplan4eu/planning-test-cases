import unified_planning
from unified_planning.shortcuts import *
from unified_planning.model.multi_agent import *
from planning_tests.commons.problem import TestCaseProblem


class UPProcterAndGamble(TestCaseProblem):
    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        problem = MultiAgentProblem("p_g")
        # AGENTs
        robot_a = Agent("robot_a", problem)
        scale1_a = Agent("scale1_a", problem)
        marks1_a = Agent("marks1_a", problem)
        markt1_a = Agent("markt1_a", problem)

        # TYPES
        location_g = UserType("location_g")
        location_p = UserType("location_p")
        state_g = UserType("state_g")
        pouch_obj = UserType("pouch_obj")
        pos = Fluent("pos", place=location_p)

        # DEFINE FLUENTS
        at = Fluent("at", BoolType(), loc=location_g)
        in_stat_g = Fluent("in_stat_g", BoolType(), state=state_g)
        relative_loc = Fluent(
            "relative_loc", BoolType(), locP=location_p, locG=location_g
        )
        adj = Fluent("adj", BoolType(), from_l=location_g, to=location_g)
        opened = Fluent("opened", BoolType(), device=location_p)
        is_draw = Fluent("is_draw", BoolType(), loc=location_p)
        is_bin = Fluent("is_bin", BoolType(), loc=location_p)
        is_bin_loc = Fluent("is_bin_loc", BoolType(), loc=location_g)
        is_mark_strength = Fluent("is_mark_strength", BoolType(), loc=location_p)
        is_mark_sloc = Fluent("is_mark_sloc", BoolType(), loc=location_g)
        is_scale = Fluent("is_scale", BoolType(), loc=location_p)
        reset = Fluent("reset", BoolType(), device=location_p)
        free = Fluent("free", BoolType(), device=location_p)
        pouch_at = Fluent("pouch_at", BoolType(), pouch=pouch_obj, loc=location_p)
        detected = Fluent("detected", BoolType(), pouch=pouch_obj)
        grasped = Fluent("grasped", BoolType(), pouch=pouch_obj)
        measured_at = Fluent(
            "measured_at", BoolType(), pouch=pouch_obj, device=location_p
        )
        is_p1 = Fluent("is_p1", BoolType(), pouch=pouch_obj)
        is_p2 = Fluent("is_p2", BoolType(), pouch=pouch_obj)
        isP3 = Fluent("isP3", BoolType(), pouch=pouch_obj)

        # ADD FLUENTS
        robot_a.add_public_fluent(at, default_initial_value=False)
        robot_a.add_public_fluent(in_stat_g, default_initial_value=False)

        scale1_a.add_private_fluent(pos, default_initial_value=False)
        scale1_a.add_public_fluent(reset, default_initial_value=False)

        marks1_a.add_private_fluent(pos, default_initial_value=False)
        marks1_a.add_public_fluent(reset, default_initial_value=False)

        markt1_a.add_private_fluent(pos, default_initial_value=False)
        markt1_a.add_public_fluent(reset, default_initial_value=False)

        problem.ma_environment.add_fluent(free, default_initial_value=False)
        problem.ma_environment.add_fluent(pouch_at, default_initial_value=False)
        problem.ma_environment.add_fluent(detected, default_initial_value=False)
        problem.ma_environment.add_fluent(grasped, default_initial_value=False)
        problem.ma_environment.add_fluent(measured_at, default_initial_value=False)
        problem.ma_environment.add_fluent(is_p1, default_initial_value=False)
        problem.ma_environment.add_fluent(is_p2, default_initial_value=False)
        problem.ma_environment.add_fluent(isP3, default_initial_value=False)

        problem.ma_environment.add_fluent(adj, default_initial_value=False)
        problem.ma_environment.add_fluent(relative_loc, default_initial_value=False)
        problem.ma_environment.add_fluent(is_draw, default_initial_value=False)
        problem.ma_environment.add_fluent(opened, default_initial_value=False)
        problem.ma_environment.add_fluent(is_bin, default_initial_value=False)
        problem.ma_environment.add_fluent(is_mark_strength, default_initial_value=False)
        problem.ma_environment.add_fluent(is_scale, default_initial_value=False)
        problem.ma_environment.add_fluent(is_mark_sloc, default_initial_value=False)
        problem.ma_environment.add_fluent(is_bin_loc, default_initial_value=False)

        # OBJECTS
        vision2 = Object("vision2", location_g)
        drawers_loc = Object("drawers_loc", location_g)
        scale_loc = Object("scale_loc", location_g)
        mark10_s_loc = Object("mark10_s_loc", location_g)
        mark10_t_loc = Object("mark10_t_loc", location_g)
        bin_loc = Object("bin_loc", location_g)

        drawer = Object("drawer", location_p)
        scale1 = Object("scale1", location_p)
        mark_s1 = Object("mark_s1", location_p)
        mark_t1 = Object("mark_t1", location_p)
        bin = Object("bin", location_p)

        available = Object("available", state_g)

        pouch1 = Object("pouch1", pouch_obj)
        pouch2 = Object("pouch2", pouch_obj)
        pouch3 = Object("pouch3", pouch_obj)
        d4_r2_c5 = Object("d4_r2_c5", pouch_obj)
        d4_r5_c5 = Object("d4_r5_c5", pouch_obj)

        # ADD OBJECTS
        problem.add_object(vision2)
        problem.add_object(drawers_loc)
        problem.add_object(scale_loc)
        problem.add_object(mark10_s_loc)
        problem.add_object(mark10_t_loc)
        problem.add_object(bin_loc)

        problem.add_object(drawer)
        problem.add_object(scale1)
        problem.add_object(mark_s1)
        problem.add_object(mark_t1)
        problem.add_object(bin)

        problem.add_object(available)

        problem.add_object(d4_r2_c5)
        problem.add_object(d4_r5_c5)

        problem.add_object(pouch1)
        problem.add_object(pouch2)
        problem.add_object(pouch3)

        # ACTIONS
        goto = InstantaneousAction("goto", from_l=location_g, to=location_g)
        from_l = goto.parameter("from_l")
        to = goto.parameter("to")
        goto.add_precondition(at(from_l))
        goto.add_precondition(adj(from_l, to))
        goto.add_effect(at(to), True)
        goto.add_effect(at(from_l), False)

        sense_imaging = InstantaneousAction("sense_imaging", pouch=pouch_obj)
        pouch = sense_imaging.parameter("pouch")
        sense_imaging.add_precondition(at(vision2))
        sense_imaging.add_precondition(opened(drawer))
        sense_imaging.add_precondition(Not(detected(pouch)))
        sense_imaging.add_precondition(in_stat_g(available))
        sense_imaging.add_precondition(
            Or(
                is_p1(pouch),
                Or(Not(detected(d4_r2_c5)), Not(pouch_at(d4_r2_c5, drawer))),
            )
        )
        sense_imaging.add_precondition(
            Or(
                is_p2(pouch),
                Or(Not(detected(d4_r5_c5)), Not(pouch_at(d4_r5_c5, drawer))),
            )
        )
        sense_imaging.add_effect(detected(pouch), True)
        sense_imaging.add_effect(pouch_at(pouch, drawer), True)

        pick_pouch = InstantaneousAction(
            "pick_pouch", pouch=pouch_obj, where_p=location_p, grip_pos=location_g
        )
        pouch = pick_pouch.parameter("pouch")
        where_p = pick_pouch.parameter("where_p")
        grip_pos = pick_pouch.parameter("grip_pos")
        pick_pouch.add_precondition(in_stat_g(available))
        pick_pouch.add_precondition(detected(pouch))
        pick_pouch.add_precondition(pouch_at(pouch, where_p))
        pick_pouch.add_precondition(Not(free(where_p)))
        pick_pouch.add_precondition(at(grip_pos))
        pick_pouch.add_precondition(relative_loc(where_p, grip_pos))
        pick_pouch.add_precondition(Not(is_bin(where_p)))
        pick_pouch.add_precondition(Not(is_mark_strength(where_p)))
        pick_pouch.add_precondition(Or(Not(is_draw(where_p)), opened(where_p)))
        pick_pouch.add_effect(grasped(pouch), True)
        pick_pouch.add_effect(in_stat_g(available), False)
        pick_pouch.add_effect(pouch_at(pouch, where_p), False)
        pick_pouch.add_effect(free(where_p), True, Not(is_draw(where_p)))

        put_pouch_on = InstantaneousAction(
            "put_pouch_on", pouch=pouch_obj, where_p=location_p, grip_pos=location_g
        )
        pouch = put_pouch_on.parameter("pouch")
        where_p = put_pouch_on.parameter("where_p")
        grip_pos = put_pouch_on.parameter("grip_pos")
        put_pouch_on.add_precondition(grasped(pouch))
        put_pouch_on.add_precondition(Not(in_stat_g(available)))
        put_pouch_on.add_precondition(Not(is_draw(where_p)))
        put_pouch_on.add_precondition(Not(is_bin(where_p)))
        put_pouch_on.add_precondition(relative_loc(where_p, grip_pos))
        put_pouch_on.add_precondition(at(grip_pos))
        put_pouch_on.add_precondition(free(where_p))
        put_pouch_on.add_effect(pouch_at(pouch, where_p), True)
        put_pouch_on.add_effect(grasped(pouch), False)
        put_pouch_on.add_effect(in_stat_g(available), True)
        put_pouch_on.add_effect(free(where_p), False)

        drop_pouch = InstantaneousAction(
            "drop_pouch", pouch=pouch_obj, grip_pos=location_g
        )
        pouch = drop_pouch.parameter("pouch")
        grip_pos = drop_pouch.parameter("grip_pos")
        drop_pouch.add_precondition(at(grip_pos))
        drop_pouch.add_precondition(
            Or(
                And(grasped(pouch), Not(in_stat_g(available)), is_bin_loc(grip_pos)),
                And(
                    measured_at(pouch, mark_s1),
                    pouch_at(pouch, mark_s1),
                    is_mark_sloc(grip_pos),
                ),
            )
        )  # Equals(grip_pos, bin_loc) #Equals(grip_pos, mark10_s_loc)
        drop_pouch.add_effect(pouch_at(pouch, bin), True)
        drop_pouch.add_effect(in_stat_g(available), True)
        drop_pouch.add_effect(grasped(pouch), False)
        drop_pouch.add_effect(free(mark_s1), True, is_mark_sloc(grip_pos))
        drop_pouch.add_effect(pouch_at(pouch, mark_s1), False, is_mark_sloc(grip_pos))

        # resetDev
        device_reset = InstantaneousAction("device_reset", dev=location_p)
        dev = device_reset.parameter("dev")
        device_reset.add_precondition(pos(dev))
        device_reset.add_precondition(Not(reset(dev)))
        device_reset.add_precondition(Not(is_draw(dev)))
        device_reset.add_precondition(Not(is_bin(dev)))
        device_reset.add_precondition(free(dev))
        device_reset.add_effect(reset(dev), True)

        measure = InstantaneousAction("measure", pouch=pouch_obj, dev=location_p)  #
        pouch = measure.parameter("pouch")
        dev = measure.parameter("dev")
        measure.add_precondition(pos(dev))
        measure.add_precondition(reset(dev))
        measure.add_precondition(pouch_at(pouch, dev))
        measure.add_precondition(Not(is_draw(dev)))
        measure.add_precondition(Not(is_bin(dev)))
        measure.add_effect(measured_at(pouch, dev), True)
        measure.add_effect(reset(dev), False)

        # ADD ACTIONS
        robot_a.add_action(goto)
        robot_a.add_action(sense_imaging)
        robot_a.add_action(pick_pouch)
        robot_a.add_action(put_pouch_on)
        robot_a.add_action(drop_pouch)

        scale1_a.add_action(measure)
        scale1_a.add_action(device_reset)

        marks1_a.add_action(measure)
        marks1_a.add_action(device_reset)

        markt1_a.add_action(measure)
        markt1_a.add_action(device_reset)

        # ADD AGENTS
        problem.add_agent(robot_a)
        problem.add_agent(scale1_a)
        problem.add_agent(marks1_a)
        problem.add_agent(markt1_a)

        print(problem.agent("robot_a"))
        print(problem.agent("scale1_a"))
        print(problem.agent("marks1_a"))
        print(problem.agent("markt1_a"))

        # INITIAL VALUES
        problem.set_initial_value(Dot(robot_a, in_stat_g(available)), True)
        problem.set_initial_value(Dot(robot_a, at(drawers_loc)), True)

        problem.set_initial_value(Dot(scale1_a, pos(scale1)), True)
        problem.set_initial_value(Dot(marks1_a, pos(mark_s1)), True)
        problem.set_initial_value(Dot(markt1_a, pos(mark_t1)), True)

        problem.set_initial_value(is_p1(d4_r2_c5), True)
        problem.set_initial_value(is_p2(d4_r5_c5), True)

        problem.set_initial_value(free(scale1), True)
        problem.set_initial_value(free(mark_s1), True)
        problem.set_initial_value(free(mark_t1), True)

        problem.set_initial_value(is_draw(drawer), True)
        problem.set_initial_value(opened(drawer), True)
        problem.set_initial_value(is_bin(bin), True)

        problem.set_initial_value(is_mark_strength(mark_s1), True)
        problem.set_initial_value(is_scale(scale1), True)
        problem.set_initial_value(is_mark_sloc(mark10_s_loc), True)
        problem.set_initial_value(is_bin_loc(bin_loc), True)

        problem.set_initial_value(adj(bin_loc, mark10_s_loc), True)
        problem.set_initial_value(adj(mark10_s_loc, bin_loc), True)
        problem.set_initial_value(adj(mark10_s_loc, scale_loc), True)
        problem.set_initial_value(adj(scale_loc, mark10_s_loc), True)
        problem.set_initial_value(adj(mark10_s_loc, drawers_loc), True)
        problem.set_initial_value(adj(drawers_loc, mark10_s_loc), True)
        problem.set_initial_value(adj(mark10_t_loc, drawers_loc), True)
        problem.set_initial_value(adj(drawers_loc, mark10_t_loc), True)
        problem.set_initial_value(adj(scale_loc, drawers_loc), True)
        problem.set_initial_value(adj(drawers_loc, scale_loc), True)
        problem.set_initial_value(adj(drawers_loc, vision2), True)
        problem.set_initial_value(adj(vision2, drawers_loc), True)
        problem.set_initial_value(adj(mark10_t_loc, vision2), True)
        problem.set_initial_value(adj(vision2, mark10_t_loc), True)

        problem.set_initial_value(relative_loc(drawer, vision2), True)
        problem.set_initial_value(relative_loc(scale1, scale_loc), True)
        problem.set_initial_value(relative_loc(mark_s1, mark10_s_loc), True)
        problem.set_initial_value(relative_loc(mark_t1, mark10_t_loc), True)
        problem.set_initial_value(relative_loc(bin, bin_loc), True)

        # GOALS
        # problem.add_goal(measured_at(pouch1, scale1))
        # problem.add_goal(measured_at(pouch1, mark_s1))
        # problem.add_goal(measured_at(pouch1, mark_t1))
        # problem.add_goal(pouch_at(pouch1, bin))
        # problem.add_goal(measured_at(pouch2, scale1))
        # problem.add_goal(measured_at(pouch2, mark_s1))
        # problem.add_goal(measured_at(pouch2, mark_t1))
        # problem.add_goal(pouch_at(pouch2, bin))
        problem.add_goal(measured_at(d4_r2_c5, scale1))
        problem.add_goal(measured_at(d4_r2_c5, mark_t1))
        problem.add_goal(pouch_at(d4_r2_c5, bin))
        problem.add_goal(measured_at(d4_r5_c5, scale1))
        problem.add_goal(measured_at(d4_r5_c5, mark_s1))
        problem.add_goal(measured_at(d4_r5_c5, mark_t1))
        problem.add_goal(pouch_at(d4_r5_c5, bin))

        with Compiler(
            problem_kind=problem.kind,
            compilation_kind=CompilationKind.DISJUNCTIVE_CONDITIONS_REMOVING,
        ) as disjunctive_conditions_remover:
            # After we have the compiler, we get the compilation result
            dcr_result = disjunctive_conditions_remover.compile(
                problem, CompilationKind.DISJUNCTIVE_CONDITIONS_REMOVING
            )
            dcr_problem = dcr_result.problem
            dcr_kind = dcr_problem.kind

            assert not dcr_kind.has_disjunctive_conditions()

        with Compiler(
            problem_kind=dcr_problem.kind,
            compilation_kind=CompilationKind.CONDITIONAL_EFFECTS_REMOVING,
        ) as conditional_effects_remover:
            # After we have the compiler, we get the compilation result
            cer_result = conditional_effects_remover.compile(
                dcr_problem, CompilationKind.CONDITIONAL_EFFECTS_REMOVING
            )
            cer_problem = cer_result.problem
            cer_kind = cer_problem.kind

            assert not cer_kind.has_conditional_effects()
        return cer_problem

    def get_description(self):
        return "procter_gamble"

    def version(self):
        return 1
