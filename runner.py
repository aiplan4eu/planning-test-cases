import os
import sys

import pytest

TEST_REPO_DIR = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    pytest.main(["-v","-rA",os.path.join(TEST_REPO_DIR, 'planning_tests/classical_planning/operation_modes/oneshot'),
                 os.path.join(TEST_REPO_DIR, 'planning_tests/numeric_planning/operation_modes/oneshot')])
