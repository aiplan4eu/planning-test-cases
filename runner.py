import os
import sys

import pytest

TEST_REPO_DIR = os.path.dirname(os.path.realpath(__file__))
UPF_DIR = os.path.abspath(os.path.join(TEST_REPO_DIR, "../upf")) # Change me if needed

print(UPF_DIR)

sys.path.append(UPF_DIR)

if __name__ == "__main__":
    pytest.main([os.path.join(TEST_REPO_DIR, 'ptc/classical_planning/operation_modes/oneshot')])