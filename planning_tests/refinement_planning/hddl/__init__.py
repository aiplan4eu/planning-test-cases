
import os
from typing import List

import unified_planning.test
from planning_tests.commons.problem import PDDLTestCase

# cache of a set of prebuilt HDDL problems
# This is important to avoid parsing the HDDL problems multiple times.
_HDDL_PROBLEMS = None


def problems() -> List[PDDLTestCase]:
    """Returns a list of PDDL test cases."""
    global _HDDL_PROBLEMS
    if _HDDL_PROBLEMS is None:
        # HDDL problems were not discovered yet,
        # look for them in the unified_planning distribution `unified_planning/test/hddl`
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
                # Adds a PDDL test case for this file.
                problems.append(PDDLTestCase(
                    name=problem_name,
                    domain=domain_filename,
                    problem=problem_filename,
                    solvable=True
                ))
        _HDDL_PROBLEMS = problems

    return _HDDL_PROBLEMS



            
