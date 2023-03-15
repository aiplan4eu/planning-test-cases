from fractions import Fraction
from typing import Optional, Union, List

import unified_planning.model
import unified_planning.plans
from unified_planning.plans import Plan


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
    

class TestCase:
    def __init__(self,
                 problem: unified_planning.model.Problem,
                 solvable: bool,
                 optimum: Optional[Union[int, Fraction]] = None,
                 valid_plans: Optional[List[Plan]] = None,
                 invalid_plans: Optional[List[Plan]] = None,
                 ):

        self._problem = problem
        self._solvable = solvable
        self._optimum = optimum
        self._valid_plans = valid_plans if valid_plans is not None else []
        self._invalid_plans = invalid_plans if invalid_plans is not None else []

    @property
    def problem(self) -> unified_planning.model.Problem:
        return self._problem

    @property
    def solvable(self) -> bool:
        return self._solvable

    @property
    def name(self) -> str:
        return self.problem.name

    @property
    def optimum(self) -> Optional[Union[int, Fraction]]:
        return self._optimum

    @property
    def valid_plans(self) -> List[Plan]:
        return self._valid_plans

    @property
    def invalid_plans(self) -> List[Plan]:
        return self._invalid_plans

class PDDLTestCase(TestCase):
    """A specialization of `TestCase` for file-based PDDL problems.
       The PDDL problems will be lazily parsed on the first access and the problem cached.
    """
    def __init__(self, name: str, domain: str, problem: str, solvable: bool):
        self._name = name
        self._domain_file = domain
        self._problem_file = problem
        super().__init__(problem=None, solvable=solvable)

    @property
    def problem(self):
        if self._problem is None:
            # problem has not been parsed yet, parse and store
            from unified_planning.io import PDDLReader
            self._problem = PDDLReader().parse_problem(self._domain_file, self._problem_file)
            self._problem.name = self._name
        return self._problem

    @property
    def name(self):
        return self._name # return the name passed to the constructor (avoids parsing the file)
