import os
import sys

import pytest

TEST_REPO_DIR = os.path.dirname(os.path.realpath(__file__))
if(len(sys.argv) < 2):
    tests = "simple"
else:
    tests = str(sys.argv[1])

if __name__ == "__main__":
    pytest.main(["-rA","-m", tests ,os.path.join(TEST_REPO_DIR, 'planning_tests/classical_planning/operation_modes/oneshot'),
                 os.path.join(TEST_REPO_DIR, 'planning_tests/numeric_planning/operation_modes/oneshot')])
