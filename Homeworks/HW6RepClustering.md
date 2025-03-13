# EM Clustering

## Readings
Zaki
  * Chapter 13.1 through 13.3.2

## Exercises

1. Can $P(C_i)$ be zero for any cluster?  Describe how if so, or explain why this isn't possible. 


2. A is a 1xN vector, and B is a Nx1 vector.  What is the order of complexity, wrt N, of these two product computations?

* AB   
* BA   

**The next questions consider the four points (2, 0), (0, 1), (-2, 0), (0, -1), and using these as sample points for a 2-D normal:**

3. Compute the $\Sigma$ and $\Sigma^{-1}$ matrices using eq 13.12 with n=4 for the four points.  


4. Compute the $\sigma_x$ and $\sigma_y$ values for the points.  

5. Assuming X = $[\sigma_x, \sigma_y]$, compute $X\Sigma^{-1}X^T$ and explain why the result is expected based on the intuitive purpose of $\Sigma^{-1}$ in the 2-D normal distribution.  In a different example case, where we arrived at a different $\Sigma$ and different $\sigma_x$ and $\sigma_y$, how might this result change? 

6. Based on the prior step, predict, without actually doing the matrix math, the result of the same computation for $[0, \sigma_y]$, $[-\sigma_x, \sigma_y]$ and $[\sigma_x, 0]$ 

7. Compute the orthonormal matrix Q representing a $30^o$ counterclockwise rotation.


8. Apply Q to the four points to rotate the entire distribution counterclockwise $30^o$ 

9. Compute the new covariance matrix $\Sigma'$, per eq 13.12, with n = 4 for the four rotated points 

10.  Compute also the positive definite matrix $\Sigma''=Q \Sigma Q^{-1}$, which is the same transform as $\Sigma$ but rotated $30^o$ 

11. Compare $\Sigma'$ and $\Sigma''$.  Why does the result make sense?

12. Zaki Ch13 Q2 
 * Note this refers to the table *above* not below

13. Zaki Ch13 Q3b (Not a!)
 * Note this refers to the table *above* not below
 * The statement regarding $P(C_i|x_{aj}) = .5$ is somewhat awkward in that i and a should be the same variable.  Simply take it to mean that all such partial probabilities are .5 regardless of point or cluster.
 * You should find you need to compute new values only for one cluster. 
 * Compute all the way through the new $w_{ij}$ values, but compute only $w_{11}, w_{12}$, and $w_{13}$.
 * Submit precisely these new values, showing your work, and highlighting these values on the page: $\mu_1, \mu_2, \Sigma_1, \Sigma_2, \Sigma_1^{-1}, P(C_1), P(C_2), w_{11}, w_{12}, w_{13}$

14. Zaki Ch13 3b Followup\
Using your results from the prior question, factor $\Sigma_1$ into $Q \Lambda Q^{-1}$ form.  (Note that there are many online sources for diagonalizing and inverting matrices.)  Explain why the resultant Q makes sense.  Draw a diagram of the 5 points and $\mu_1$ and estimate the implied scaling values and rotation value for $C_1$.  This will also serve as a reality check on your $C_1$ computations.\
\
Submit the factoring, the estimated scaling factors, the diagram, and an explanation of how the Q and the scaling factors lead to an ellipse that corresponds with the 5 points.\
\
Finally, comment on how long the EM algorithm will take to converge in this case, and what lessons might be drawn from this regarding initialization.



