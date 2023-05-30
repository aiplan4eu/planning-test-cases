# Planning-Approaches-Test-Cases
This repository contains the test cases for the planning engines developed within the AIPLAN4EU project.

There are currently two main modes that you can follow for implementing your tests or running existing tests.

## Pytest
The first one uses pytest, to execute tests open the planning_tests folder and from your command window call pytest, in this way, all texts will be executed. 
There are a couple of options if you want to run only a subset of tests:
1) call only a specific set of tests using pytest markers, all the available markers are listed in the pytest.ini file.
```python
pytest -m MARKERNAME
```
2) specify the name of the planner, or the name of the grounder, that you want to use to execute the tests, to do that write --planner_name or --grounder_name followed by the name of the planner/grounder.
```python
pytest --planner_name enhsp
```
## Report.py
The second one uses the report.py file, to execute the tests run the file using python from your command window.
```python
Usage
 - python report.py                          # will run all solvers on all all problems
 - python report.py aries tamer              # will run aries an tamer on all problems they support 
 - python report.py aries --prefix up:basic  # will run aries on all problems whose name starts with "up:basic" """)
 
```
