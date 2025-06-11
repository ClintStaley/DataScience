# Chapter 19, 20, 22, 7

## Readings
Zaki Chapter 19, 20.1, 22.1, 7.1, 7.2

## Exercises

1. Ch 19 Q1 (and explain your answers)\
  **a. False, since high entropy implies uniform spread and low purity**\
  **b. True, since it may permit finer division of points by category**
1. Ch 19 Q2 Do this using only 2-way categorical splits.  Report the gain resulting from each branch in the tree. Hints: 
     * The entropy of a 1/3; 2/3 distribution is worth computing once, and using multiple times here and later. You should find it to be between .9 and .95.
     * You should end up with just two splits in the tree  
**1/3;2/3 distribution has entropy .918. First split $\in  Sports$, gain .459; Second split < 25, gain .449.  (27, Vintage) => H**
1. Ch 19 Q5.  Hints:
    * $AB-B^2 = B(A-B)$.  This is useful.

|Data|AB-B^2|Class|
|---|---|---|
|1|less|H|
|2|less|H|
|3|gtr|L|
|4|less|H|
|5|less|H|
|6|gtr|H|
|7|less|L|
|8|gtr|L|

Entropy before = $-(.375 lg_2(.375) + .625 lg_2(.625)) = -(.375(-1.415)+.625(-.678)) = .954$
Entropy after = less: $(.8 lg(.8) + .2 lg(.2)) = .722; greater: .333 lg(.333) + .667 lg(.667) = .920 Total: .625 (.722) + .375(.920) = .796

Gain = .954 - .796 = .158



1. Ch 22 Q5. And give the actual ROC value. **See diagram for ROC curve (2 up, 1 right, 1 up, 3 right, 1 up, 1 right, 1 up) Area is 3.5 - 1 = 2.5**

|.95|.94|.87|.86|.86|.86|.76|.53|.44|.25|
|---|---|---|---|---|---|---|---|---|---|
|+1|+1|-1|+1|-1|-1|-1|+1|-1|+1|

7. Ch22 Q5, but redo the problem after dividing all P values in half.**Absolutely no change**

1. Ch 7 Q1, but do parts a, b and d by writing and executing appropriate Numpy code, leaving only c and e to do by hand.  Include the code in your answer.  

```
import numpy as np
import numpy.linalg as la

def main():
   d = np.array([[8, -20], [0, -1], [10, -19], [10, -20], [2, 0]])
   numPts = len(d)
   mean = d.mean(axis=0)
   dBar = d - mean
   sigmas = np.matmul(dBar.reshape(numPts, 2, 1), dBar.reshape(numPts, 1, 2))
   sigma = sigmas.sum(axis=0) / numPts
   eVals, eVecs = np.linalg.eigh(sigma)
   print(f"Mean:\n{mean}\nSigma:\n{sigma}\nEigs:\n{list(zip(eVals, eVecs))}\n")

main()

Mean:
[  6. -12.]
 Sigma:
[[ 17.6 -38. ]
 [-38.   88.4]]
Eigs:
[(1.0658108756861413, array([-0.91696017, -0.39897876])), (104.93418912431386, array([-0.39897876,  0.91696017]))]

Principal component is (.399, -.917).  Shape is very long ellipse with major axis
at slope -2.3.  "Intrinsic" dimensionality is 1, since second component has
eigenvalue of 1 vs first component eigenvalue 105 (10/1 ratio of std dev)
```

9. A PCA analysis on a 5-dimensional dataset D, where |D| = 1000 and var($\bar{D}$) = 200, results in $\lambda_1 = 40$.  Does this indicate an error in the analysis? If so, why? If there is no error, describe the shape of the point cloud. **If 20% of the variance is in the principal component, then all five components must have 20% each of the variance since they cannot have more variance than prior components.  This in turn implies a 5-D hyperspherical point cloud.**

1. Answer the above question if var($\bar{D}$) = 40.
**Now the principal component has *all* the variance, with none left for others.  Point cloud is a line along the principal component.**

1. Answer the same question if var($\bar{D}$) = 201.
**Analysis error since at least 1/5 of variance must be in principal component.**
  