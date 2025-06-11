# Python Analysis of Clouds and Correlations
## Readings
"Your Python Code":
Review the most sophisticated Python app or two that you wrote in 171 or other earlier courses.

## Exercises
1. Python Build Environment
   * Update (or install for the first time) a recent Python3 interpreter on your machine, and the Python VSCode plugin.
   * Use venv to create a Python environment for the class.  Install numpy and matplotlib in addition to the standard libraries.
   * From VSCode, take one of the Python example programs from your review reading, bring it up in VSCode and run it from VSCode. Edit it trivially and rerun it.
   * Submit an image of Python working from VSCode.
   
2. Write a python script to output an equation for a hyperplane in 5 dimensional space that separates the points in Set1.tsv and Set2.tsv, with the first on one side of the hyperplane, and the second on the opposite side.  This can be done for the two sets because they each represent a multivariate normal "cloud" that doesn't overlap the other set.  Do this thus:
   * Read each set into a numpy arrayKv
   * Find the center of mass (the mean) of each set.
   * Find the vector direction d that leads from one center to the other.  
   * Define a plane that cuts perpendicular to d, so it can divide the two clouds
   * Figure out the distance from the origin that would cause that plane to pass through the midpoint of the line between the centers of mass
   * And, *importantly*, use no python loops nor list comprehensions.  Do the entire job with numpy operations.  (They do the looping, and they operate in C, and are much faster.)

```
Mean1: [-2.887  7.085 -4.221 -8.218 -9.302]
Mean2: [ 8.301  1.286 -7.468  8.888  4.611]
Min1: -17.93551729945652 Max1: -9.456795019219607
Min2: 9.567497406944499 Max2: 14.945888437513897
Direction: [ 0.437 -0.227 -0.127  0.668  0.543], Midpoint projection: 0.05535
```

3. Once you have done problem 2, extend the program to read file ToTest.tsv, and classify each line it in as belonging to Set1 or Set2.  (Output a single column of "1" or "2" for each row of ToTest.tsv).  As before, use no Python loops of any sort.
Submit your final Python code, and the 1/2 output file, as your answer for this and the prior problem.

```
Top rows
9.0149 2.2738 -7.8024 11.0177 5.7530 2.0000
8.3319 2.4861 -7.5263 8.1662 5.0829 2.0000
6.4953 -0.6013 -8.9187 8.1431 3.4932 2.0000
7.8723 2.1150 -6.4533 8.8572 4.3934 2.0000
9.4731 1.6278 -6.9446 9.9651 1.9215 2.0000
-3.3869 5.0944 -6.8755 -8.6600 -9.2100 1.0000
-2.6130 7.9519 -2.9301 -7.4205 -9.6582 1.0000
-3.3896 8.0541 -6.1430 -5.9523 -7.2367 1.0000
-2.1985 9.6585 -4.8978 -7.5050 -8.3845 1.0000
9.4499 2.3040 -6.7829 7.0460 3.6447 2.0000
```

4. Write Python to read Properties.tsv, a file of 8-dimensional patterns, with properties we'll call P0 through P7.  Analyze appropriately the relationships between these 10 properties, and for each, output the other property that has the strongest relationship with it, whether positive or negative. Submit your Python code and an output of 10 lines, each listing a property as "P#".

6
7
3
4
3
6
5
3

