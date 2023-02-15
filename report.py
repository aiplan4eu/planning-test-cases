import os
import time

from unified_planning.engines import PlanGenerationResultStatus




# pip install https://github.com/plaans/aries/releases/download/latest/up_aries.tar.gz

from unified_planning.shortcuts import *
from unified_planning.model.htn import *
import unified_planning as up
from unified_planning.environment import get_environment
get_environment().factory.add_engine('aries', 'up_aries', 'AriesDev')
get_environment().credits_stream = None # silence credits

def oneshot_planners():
    # return ["aries"]
    tags = [n for n in get_environment().factory.engines]
    tags = [t for t in tags
            if get_environment().factory.engine(t).is_oneshot_planner()]
    return tags


def up_tests():
    from unified_planning.test.examples import get_example_problems

    cases = []
    for name, problem in get_example_problems().items():
        pb = problem.problem.clone()
        pb.name = f"up:{name}"
        cases.append(TestCase(pb, solvable=True))
    return cases


def hddl_problems():
    import os
    import unified_planning.test
    up_tests_path = os.path.dirname(unified_planning.test.__file__)
    # directory where to find hddl instances
    hddl_dir = os.path.join(up_tests_path, "hddl")

    subfolders = [f.path for f in os.scandir(hddl_dir) if f.is_dir()]
    problems = []
    for id, domain in enumerate(subfolders[:]):
        domain_filename = os.path.join(domain, "domain.hddl")
        problem_filename = os.path.join(domain, "instance.1.pb.hddl")

        if os.path.exists(domain_filename):
            problem_name = "hddl:" + os.path.basename(domain)
            problems.append(PDDLTestCase(
                name=problem_name,
                domain=domain_filename,
                problem=problem_filename,
                solvable=True
            ))

    return problems


class TestCase:
    def __init__(self, problem: up.model.Problem, solvable: bool):
        self._problem = problem
        self._solvable = solvable

    def problem(self) -> up.model.Problem:
        return self._problem

    @property
    def solvable(self):
        return self._solvable

    @property
    def name(self) -> str:
        return self.problem().name

class PDDLTestCase(TestCase):
    def __init__(self, name: str, domain: str, problem: str, solvable: bool):
        self._name = name
        self._domain_file = domain
        self._problem_file = problem
        super().__init__(problem=None, solvable=solvable)

    def problem(self):
        if self._problem is None:
            # problem has not been parsed yet, parse and store
            from unified_planning.io import PDDLReader
            self._problem = PDDLReader().parse_problem(self._domain_file, self._problem_file)
            self._problem.name = self._name
        return self._problem

    @property
    def name(self):
        return self._name


def report(planner: Optional[str] = None,
           planners: Optional[List[str]] = None,
           problem_prefix: str = ""):

    if planner is not None:
        planners = [planner]
    if planners is None:
        planners = oneshot_planners()

    problems = up_tests() + hddl_problems()
    problems = [p for p in problems if p.name.startswith(problem_prefix)]

    for test_case in problems:
        # if test_case.name != "up:htn-go-temporal":
        #     continue
        print()
        print(test_case.name.ljust(40), end='\n')
        pb = test_case.problem()

        for planner in planners:
            planner = OneshotPlanner(name=planner)
            if planner.supports(pb.kind):

                print("  ", planner.name.ljust(80), end='')
                start = time.time()
                try:
                    result = planner.solve(pb, timeout=1) #, output_stream=sys.stdout)
                    end = time.time()
                    status = str(result.status).replace("PlanGenerationResultStatus.", "").ljust(20)
                    print("\t  ", status, "\t    ", end - start)
                    if result.status == PlanGenerationResultStatus.INTERNAL_ERROR and result.log_messages is not None:
                        print('\n'.join(map(str, result.log_messages)))

                except Exception as e:
                    print("\t CRASH !!!!", e)

    

TEST_REPO_DIR = os.path.dirname(os.path.realpath(__file__))


if __name__ == "__main__":

    # report(planner="fast-downward", problem_prefix="up:")
    report(planners=["aries","fast-downward"], problem_prefix="hddl")

    # # aries = up_aries.Aries()
    # planners = oneshot_planners()
    # print(planners)
    #
    # pbs = []
    # pbs += up_tests()
    # pbs += hddl_problems()
    #
    # planner = OneshotPlanner(name="aries")
    #
    #
    # for test_case in pbs:
    #     # if test_case.name != "up:htn-go-temporal":
    #     #     continue
    #     print()
    #     print(test_case.name.ljust(40), end='\n')
    #     pb = test_case.problem()
    #
    #     for planner in oneshot_planners():
    #         planner = OneshotPlanner(name=planner)
    #         if planner.supports(pb.kind):
    #
    #             print("  ", planner.name.ljust(80), end='')
    #             start = time.time()
    #             try:
    #                 result = planner.solve(pb, timeout=1) #, output_stream=sys.stdout)
    #                 end = time.time()
    #                 status = str(result.status).replace("PlanGenerationResultStatus.", "").ljust(20)
    #                 print("\t  ", status, "\t    ", end - start)
    #                 if result.status == PlanGenerationResultStatus.INTERNAL_ERROR and result.log_messages is not None:
    #                     print('\n'.join(map(str, result.log_messages)))
    #
    #             except Exception as e:
    #                 print("\t CRASH !!!!", e)

            # print(result.plan)

