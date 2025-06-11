# Clustering Homework

## Readings
Zaki
  * Chapter 13 minus 13.3.3 and 13.3.4

## Exercises
### Concepts in Clustering

1. Can $P(C_i)$ be zero for any cluster?  Describe how if so, or explain why this isn't possible.


2. A is a 1xN vector, and B is a Nx1 vector.  What is the order of complexity, wrt N, of these two product computations?

3. Consider the four points (2, 0), (0, 1), (-2, 0), (0, -1).  Using these as sample points for a 2-D normal:

* Compute the $\Sigma$ and $\Sigma^{-1}$ matrices using eq 13.12 with n=4 for the four points.
* Compute the $\sigma_x$ and $\sigma_y$ values for the points.  
* Assuming X = $[\sigma_x, \sigma_y]$, compute $X\Sigma^{-1}X^T$ and explain why the result is expected based on the intuitive purpose of $\Sigma^{-1}$ in the 2-D normal distribution.  In a different example case, where we arrived at a different $\Sigma$ and different $\sigma_x$ and $\sigma_y$, how might this result change?
* Based on the prior step, predict, without actually doing the matrix math, the result of the same computation for $[0, \sigma_y]$, $[-\sigma_x, \sigma_y]$ and $[\sigma_x, 0]$
* Compute the orthonormal matrix Q representing a $30^o$ counterclockwise rotation.
* Apply Q to the four points to rotate the entire distribution counterclockwise $30^o$
* Compute the new covariance matrix $\Sigma'$, per eq 13.12, with n = 4 for the four rotated points
* Compute also the positive definite matrix $\Sigma''=Q \Sigma Q^{-1}$, which is the same transform as $\Sigma$ but rotated $30^o$
* Compare $\Sigma'$ and $\Sigma''$.  Why does the result make sense?

### Zaki
 
Q2 
 * Note this refers to the table *above* not below

Q3b (Not a!)
 * Note this refers to the table *above* not below
 * The statement regarding $P(C_i|x_{aj}) = .5$ is somewhat awkward in that i and a should be the same variable.  Simply take it to mean that all such partial probabilities are .5 regardless of point or cluster.
 * You should find you need to compute new values only for one cluster.  Why is this?
 * Factor $\Sigma_1$ into $Q \Lambda Q^{-1}$ form.  (Note that there are many online sources for diagonalizing and inverting matrices.) Explain why the resultant Q makes sense by drawing a diagram of the 5 X points and $\mu_1$ and estimating the implied scaling values and rotation value for $C_1$.  This will also serve as a reality check on your $C_1$ computations.
 * Compute all the way through the new $w_{ij}$ values, but compute only $w_{11}, w_{12}$, and $w_{13}$.
 * Submit precisely these new values, showing your work, and highlighting these values on the page: $\mu_1, \mu_2, \Sigma_1, \Sigma_2, \Sigma_1^{-1}, P(C_1), P(C_2), w_{11}, w_{12}, w_{13}$
 * Predict where $\mu_1$ and $\mu_2$ will end up if we continue to iterate the EM algorithm.  Comment on what this says about choosing the initial $\theta$ value for EM.

### Bayes' Theorem

1. Today is after the 29th of the month (the 30th or 31st).  What is the chance that the month is March?

2. You take a test with a 5% false positive rate and a 10% false negative rate.  (%5 of the positive results are incorrect, as are 10% of the negative results.)  You test positive, but you also know that on average, only 1% of the population is actually positive for this test.  What is the chance that your positive test is accurate?  (Your answer should make use of both the false positive and false negative stat)

3. A college has these statistics.  What is the chance that a random CSCI major, who we know is not a senior, is a freshman?

|Class | % of all students | % that are CSCI majors |
|--------------|-----------|------------|
| Freshman     | 30    | 4       |
| Sophomore   | 25  | 8       |
| Junior    | 20  | 9       |
| Senior     | 25  | 7       |


