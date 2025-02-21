# Python Analysis of Normal Distributions
## Readings
"Your Python Code":
Review the most sophisticated Python app or two that you wrote in 171 or other earlier courses.

## Exercises
1. Python Build Environment
   * Update (or install for the first time) a recent Python3 interpreter on your machine, and the Python VSCode plugin.
   * Use venv to create a Python environment for the class.  Install numpy and matplotlib in addition to the standard libraries.
   * From VSCode, take one of the Python example programs from your review reading, bring it up in VSCode and run it from VSCode. Edit it trivially and rerun it.
   * Submit an image of Python working from VSCode.

2. Write Python script CheckCorrelation.py to read Properties.tsv, a file of 8-dimensional patterns, with properties we'll call P0 through P7.  Analyze appropriately the relationships between these 8 properties, and for each, output the other property that has the strongest relationship with it, whether positive or negative. Submit your Python code and an output of 8 lines, each listing the zero-based property number that most influences that property.  And again, no Python loops of any sort.
   
3. Write a python script CheckSeparableClouds.py to output an equation for a hyperplane in 5 dimensional space that separates the points in Set1.tsv and Set2.tsv, with the first on one side of the hyperplane, and the second on the opposite side.  Do this thus:
   * Read each set into a numpy array
   * Find the center of mass (the mean) of each set.
   * Find the unit vector direction p that leads from one center to the other.
   * Determine whether that vector direction actually *can* separate the clouds, or whether the two overlap so as to make separation impossible.  In the latter case print an error and exit.
   * Compute a "d" value for projection along that vector that splits the two clouds with the dividing plane pX = d being equally far from either cloud's nearest point to it.
   * Print p and d\
   
   And, *importantly*, use no Python loops nor list comprehensions.  Do the entire job with numpy operations.  (They do the looping, and they operate in C, and are much faster.)

4. Once you have done problem 3, extend CheckSeparableClouds.py to read file ToTest.tsv as a third command line parameter, and classify each line it in as belonging to Set1 or Set2.  Output each row of ToTest.tsv, followed by a final column with value 1.0 or 2.0, indicating the set it belongs to.  As before, use no Python loops of any sort.  Submit your final Python code, and the augmented file as ToTestLabels.tsv, as your answer for this and the prior problem.

