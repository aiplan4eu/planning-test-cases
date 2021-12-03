import os
import sys

import pytest

TEST_REPO_DIR = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    pytest.main([os.path.join(TEST_REPO_DIR, 'ptc/classical_planning/operation_modes/oneshot')])