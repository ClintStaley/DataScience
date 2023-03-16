# Chapter 19, 20, 22, 7

## Readings
Zaki Chapter 19, 20.1, 22.1, 7.1, 7.2

## Exercises

1. Ch 19 Q1 (and explain your answers)\
  
1. Ch 19 Q2 Do this using only 2-way categorical splits.  Report the gain resulting from each branch in the tree. Hints: 
     * The entropy of a 1/3; 2/3 distribution is worth computing once, and using multiple times here and later. You should find it to be between .9 and .95.
     * You should end up with just two splits in the tree  
1. Ch 19 Q5.  Hints:
    * $AB-B^2 = B(A-B)$.  This is useful.

1. Ch 20 Q2, and draw both the optimal discriminant and the mean-difference, including how many overlaps each have. Hints:
    * The math for the means is simple, and should arrive at integral coordinates.
    * Even with the optimal discriminant, you'll get some overlap, but less than with the mean-difference.

1. What is the determinant of matrix B in eq 20.7.  Why?  Onto what vector does it project, if any?  Why?

1. Ch 22 Q5. And give the actual ROC value.

1. Ch 22 Q5, but redo the problem after dividing all P values in half.

1. Ch 7 Q1, but do parts a, b and d by writing and executing appropriate Numpy code, leaving only c and e to do by hand.  Include the code in your answer.  

1. A PCA analysis on a 5-dimensional dataset D, where |D| = 1000 and var($\bar{D}$) = 200, results in $\lambda_1 = 40$.  Does this indicate an error in the analysis? If so, why? If there is no error, describe the shape of the point cloud.

1. Answer the above question if var($\bar{D}$) = 40.

1. Answer the same question if var($\bar{D}$) = 201.
  