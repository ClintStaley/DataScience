# Linear Discriminant Analysis

## Readings

Zaki Chapter 20.1

1. Do the following experiment with LD analysis, using eq 20.10 with C1 = (6, 1), (1, 0), (1, 2) and (-4, 1), and C2 = -C1
    * What are the two means, and the unadjusted w (simple difference without S)?
    * How well does that unadjusted w separate the clusters?  
    * What is $S_1$? $S_2$? 
    * What is $(S_1+S_2)^{-1}$? 
    * What is the adjusted w? 
    * How well does the adjusted w separate the clusters? 

2. Zaki Ch20 Q2, and draw both the optimal discriminant and the 
mean-difference, including how many overlaps each have. Hints:\

    * The math for the means is simple, and should arrive at integral coordinates.
    * Discriminants are *normalized*, per the presentation in Zaki.
    * The optimal discriminant should be clearly superior to the mean-difference.
    
3. What is the determinant of matrix B in eq 20.7.  Why?  Onto what vector 
does it project, if any?  Why?

4. We can usually apply Eq 20.10 to satisfy line 7 of Algorithm 20.1, but it is interesting to consider a case where we cannot.  Come up with a straightforward example where it would not work.

