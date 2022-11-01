# Chapters 14, 15, 17

## Readings
Zaki
  * Chapter 14, 15 and 17

## Exercises
### Zaki

1. Ch 14 Q2 (but provide only the final distance matrix)

2. Ch 14 Q4b

3. Ch 15 Q1, plus find the clusters that DBScan would discover


### Information Entropy

4. Assume you have a non-uniform probability distribution, with event probabilities ranging from .25 down to .01.  You divide one of the existing events into two equally-likely events, e.g. dividing an event E with 20% probability into E1 and E2 each with 10% probability.  Assuming $log_2$, what is the largest possible increase in entropy resulting from such a division?  The smallest?



5. Entropy is a common means of measuring password strength.  A very good password will have, for instance, 40 bits of entropy.  Describe a password choosing system that would result in that much entropy.

 

6. A very good means of choosing high-strength password is to randomly build a phrase by drawing words from a dictionary of say 4096 possibilities.  A four-word such phrase might be "red dog true red".  Assumingly uniformly random choices from a 4096 word dictionary, what is the information entropy of such a pass phrase?  Why? Is it as random, for instance, as a safe password of 7 2-digit numbers, e.g. 01-00-20-98-43-28-42?  Why or why not?


### Numpy

7. Assume you have a numpy array vals of 10 3-D data points.  Vals has shape (10, 3).   *With a single numpy assignment and no Python loops*, create a numpy array relativeVals of shape (10, 5, 3) comprising 5 columns of points, each a copy of vals. Actually write the code and confirm it works via printing relativeVals.shape and relativeVals.  Submit the code and a run.


8. Now also assume a numpy array "means" of 3-D means of 5 clusters, of shape (5, 3).  Modify your one assignment to relativeVals so each column now represents the difference between the points and the mean point of one of the clusters.


