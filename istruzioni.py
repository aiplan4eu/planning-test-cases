import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io.pddl_writer import PDDLWriter
from unified_planning.io.python_writer import PythonWriter
from unified_planning.io.pddl_reader import PDDLReader

path = 'planning-test-cases/planning_tests/numeric_planning/pddl_problems/'
reader = PDDLReader()
# Qui metti il path per domino e problema
<<<<<<< HEAD
pddl_problem = reader.parse_problem((path + 'sailing/sailing_domain.pddl'),(path + 'sailing/sailing_4_10_1229.pddl'))
=======
pddl_problem = reader.parse_problem((path + 'block_grouping/block_grouping_domain.pddl'),(path + 'block_grouping/block_grouping_20_25_6_3.pddl'))
>>>>>>> 6288bca80dd427391b54cdd284a31b77e4360fd2




w = PythonWriter(pddl_problem)
print(w.write_problem_code())
w.write_problem_code_to_file('output')

