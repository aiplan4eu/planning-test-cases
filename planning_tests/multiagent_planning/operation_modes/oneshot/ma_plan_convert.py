from unified_planning.shortcuts import *
import planning_tests.multiagent_planning.operation_modes.oneshot.convert_mapddl_to_pddl as mapddl_to_pddl
from unified_planning.io.ma_pddl_writer import MAPDDLWriter
from unified_planning.io.pddl_reader import PDDLReader
from unified_planning.plans.plan import ActionInstance
from unified_planning.plans.sequential_plan import SequentialPlan


class PlanConverter:
    def __init__(self, pddl_problem):
        self.pddl_problem = pddl_problem

    def convert_sequential_plan(self, sequential_plan):
        new_plan = []
        for act in sequential_plan.actions:
            action_name = f"{act.action.name}_{act.agent.name}"
            matched = False
            for act_prob in self.pddl_problem.actions:
                if action_name == act_prob.name:

                    agent_param = self.pddl_problem.object(act_prob.parameters[0].name)
                    assert agent_param.type == act_prob.parameters[0].type

                    new_params = [agent_param]
                    new_params.extend(act.actual_parameters)

                    new_act_instance = ActionInstance(
                        action=act_prob, params=new_params
                    )
                    new_plan.append(new_act_instance)
                    matched = True
                    break
            if not matched:
                raise ValueError(f"No matching action found for {action_name}")
        return SequentialPlan(actions=new_plan, environment=self.pddl_problem._env)

    def _custom_replace_function(self, action_instance):
        action_name = f"{action_instance.action.name}_{action_instance.agent.name}"
        for act_prob in self.pddl_problem.actions:
            if action_name == act_prob.name:
                agent_param = self.pddl_problem.object(act_prob.parameters[0].name)
                assert agent_param.type == act_prob.parameters[0].type

                new_params = [agent_param]
                new_params.extend(action_instance.actual_parameters)

                new_action_instance = ActionInstance(action=act_prob, params=new_params)
                return new_action_instance

            # raise ValueError(f"No matching action found for {action_name}")
        return action_instance

    def convert_pop_plan(self, pop_plan):
        new_pop = pop_plan.replace_action_instances(self._custom_replace_function)
        return new_pop
