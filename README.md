# Planning-Approaches-Test-Cases
This repository contains the test cases for the planning engines developed within the AIPLAN4EU project.

## Report.py
To execute the tests run the file using python from your command window.
```python
Usage
 - python report.py                          # will run all solvers on all all problems
 - python report.py aries tamer              # will run aries an tamer on all problems they support 
 - python report.py aries --prefix up:basic  # will run aries on all problems whose name starts with "up:basic" """)
 - python report.py --mode anytime           # will run all solvers that support anytime on all problems
 - python report.py --mode plan-repair       # will run all plan-repairers on all problems (only lpg and numeric for now)
```