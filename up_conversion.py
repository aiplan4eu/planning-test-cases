import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io.pddl_writer import PDDLWriter
from unified_planning.io.python_writer import PythonWriter
from unified_planning.io.pddl_reader import PDDLReader

path = 'planning-test-cases/planning_tests/numeric_planning/pddl_problems/'
reader = PDDLReader()
# Put here the path for the domain and the problem
pddl_problem = reader.parse_problem((path + 'sailing/sailing_domain.pddl'),(path + 'sailing/sailing_4_10_1229.pddl'))




w = PythonWriter(pddl_problem)
w.write_problem_code_to_file('output')

