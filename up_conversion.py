import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io.pddl_writer import PDDLWriter
from unified_planning.io.python_writer import PythonWriter
from unified_planning.io.pddl_reader import PDDLReader

path = 'planning_tests/temporal_planning/pddl_problems/'
reader = PDDLReader()
# Put here the path for the domain and the problem

pddl_problem = reader.parse_problem((path + 'rovers/rovers_domain.pddl'),(path + 'rovers/rovers_pfile2.pddl'))




w = PythonWriter(pddl_problem)
w.write_problem_code_to_file('output')

