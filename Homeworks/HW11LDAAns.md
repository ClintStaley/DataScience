# Linear Discriminant Analysis

## Readings

Zaki Chapter 20.1

1. Do the following experiment with LD analysis, using eq 20.10 with C1 = (6, 1), (1, 0), (1, 2) and (-4, 1), and C2 = -C1
    * What are the two means, and the unadjusted w (simple difference without S)? **(1, 1) and (-1, -1), and (2, 2)**
    * How well does that unadjusted w separate the clusters?  **So-so. extreme points overlap**
    * What is $S_1$? $S_2$? **Same for each $\begin{bmatrix}50&&0\\0&&2\end{bmatrix}$**
    * What is $(S_1+S_2)^{-1}$? $\begin{bmatrix}.01&&0\\0&&.25\end{bmatrix}$
    * What is the adjusted w? $\begin{bmatrix}.01&&0\\0&&.25\end{bmatrix}\begin{bmatrix}2\\2\end{bmatrix} = \begin{bmatrix}.02\\.5\end{bmatrix}$, almost a perfect vertical
    * How well does the adjusted w separate the clusters? **Great, even extremes are well separated**

2. Zaki Ch20 Q2, and draw both the optimal discriminant and the 
mean-difference, including how many overlaps each have. Hints:\

    * The math for the means is simple, and should arrive at integral coordinates.
    * Even with the optimal discriminant, you'll get some overlap, but less than with the mean-difference.

$\mu_\triangle = (5,4)$, $\mu_O = (7, 4)$,  $\mu_O - \mu_\triangle = (2,0)$, $normed = (1,0)$,\
 $\Sigma^{-1} \begin{bmatrix}1\\0\end{bmatrix}= \begin{bmatrix}.056\\-.029\end{bmatrix}$, $normed \begin{bmatrix}.887\\-.460\end{bmatrix}$

**Draw a horizontal arrow for mean diff and another arrow at about -.5 slope for optimal.  Show that three points overlap for former, and only one for latter.**

3. What is the determinant of matrix B in eq 20.7.  Why?  Onto what vector 
does it project, if any?  Why?\

**0 since it has rank 1 and projects onto mean-diff vector.**

4. We can usually apply Eq 20.10 to satisfy line 7 of Algorithm 20.1, but it is interesting to consider a case where we cannot.  Come up with a straightforward example where it would not work.

**Any example with singular S, e.g. point spreads along a line, would suffice.  You can't invert such a spread**