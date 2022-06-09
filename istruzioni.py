import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io.pddl_writer import PDDLWriter
from unified_planning.io.python_writer import PythonWriter
from unified_planning.io.pddl_reader import PDDLReader

path = 'planning-test-cases/planning_tests/numeric_planning/pddl_problems/'
reader = PDDLReader()
# Qui metti il path per domino e problema
pddl_problem = reader.parse_problem((path + 'block_grouping/block_grouping_domain.pddl'),(path + 'block_grouping/block_grouping_20_25_6_3.pddl'))




w = PythonWriter(pddl_problem)
print(w.write_problem_code())
w.write_problem_code_to_file('output')
