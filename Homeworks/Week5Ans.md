# Week 5

## Readings
Zaki
  * Chapter 13 minus 13.3.3 and 13.3.4

## Exercises
### Concepts in Clustering

1. Can $P(C_i)$ be zero for any cluster?  Describe how if so, or explain why this isn't possible.

**Not possible.  Every datapoint contributes some nonzero value to each $P(C_i)$ no matter how distant since the multivariate normal is everywhere > 0**

2. A is a 1xN vector, and B is a Nx1 vector.  What is the order of complexity, wrt N, of these two product computations?

* AB   **O(N) since it's a dot product**
* BA   **$O(N^2)$ since it's an outer product**

3. Consider the four points (2, 0), (0, 1), (-2, 0), (0, -1).  Using these as sample points for a 2-D normal:

* Compute the $\Sigma$ and $\Sigma^{-1}$ matrices using eq 13.12 with n=4 for the four points.  
**$\Sigma = \begin{bmatrix}2 & 0 \\ 0 && 0.5 \\ \end{bmatrix} \Sigma^{-1} = \begin{bmatrix}0.5 && 0 \\ 0 && 2 \\ \end{bmatrix}$**
* Compute the $\sigma_x$ and $\sigma_y$ values for the points.  **$\sigma_x = 1.414, \sigma_y = .707$**
* Assuming X = $[\sigma_x, \sigma_y]$, compute $X\Sigma^{-1}X^T$ and explain why the result is expected based on the intuitive purpose of $\Sigma^{-1}$ in the 2-D normal distribution.  In a different example case, where we arrived at a different $\Sigma$ and different $\sigma_x$ and $\sigma_y$, how might this result change?
**$X\Sigma^{-1}X^T = 2$ This is reasonable because $\Sigma^{-1}$ converts the scaled rotated multivariate $X - \mu$ into a simple multivariate normal with $\sigma_x = \sigma_y = 1$, and the product of X with itself arrives at the squared distance from mean, with $\sigma = 1$, which would be $1^2 + 1^2 = 2$  The result should be exactly the same with a different example case.**
* Based on the prior step, predict, without actually doing the matrix math, the result of the same computation for $[0, \sigma_y]$, $[-\sigma_x, \sigma_y]$ and $[\sigma_x, 0]$
**By the reasoning above, we'd get 1, 2, and 1, respectively.**
* Compute the orthonormal matrix Q representing a $30^o$ counterclockwise rotation.
$\begin{bmatrix}.866 && -.5\\.5 && .866\\ \end{bmatrix}$
* Apply Q to the four points to rotate the entire distribution counterclockwise $30^o$ **$(\pm 1.7321, pm1), (\pm.5, \mp.866)$**
* Compute the new covariance matrix $\Sigma'$, per eq 13.12, with n = 4 for the four rotated points $\begin{bmatrix}1.625 && .65\\.65 && .875\\ \end{bmatrix}$
* Compute also the positive definite matrix $\Sigma''=Q \Sigma Q^{-1}$, which is the same transform as $\Sigma$ but rotated $30^o$ 
$\begin{bmatrix}.866 && .5\\-.5 && .866\\ \end{bmatrix}
 \begin{bmatrix}2 & 0 \\ 0 && 0.5 \\ \end{bmatrix}
 \begin{bmatrix}.866 && -.5\\.5 && .866\\ \end{bmatrix} = 
 \begin{bmatrix}1.625 && .65\\.65 && .875\\ \end{bmatrix}$
* Compare $\Sigma'$ and $\Sigma''$.  Why does the result make sense? **The same, since the covariance matrix is the transform needed to scale and rotate the spherical multivariate normal**

### Zaki
 
Q2 
 * Note this refers to the table *above* not below

**Q2a $\mu_1 = \frac{2(.9)+3(.8)+7(.3)+2(.9)+1(.8)}{.9+.8+.3+.1+.9+.8)} = \frac{9.8}{3.8} = 2.58$; $\mu_2 = 6.62$ similarly**

**Q2b $P(5|C_1) = \frac{e^{-\frac{(x-2)^2}{2}}}{\sqrt{2\pi}} = .0044$
$P(5|C_2) = \frac{e^{-\frac{(x-7)^2}{2}}}{\sqrt{2\pi}} = .054$, so since all P(C) are equal, $P(C_1|5) = \frac{P(5|C_1)}{P(5|C_1)+P(5|C_2)}=\frac{.0044}{.0044+.054} = .075$; similarly $P(C_2|5) = \frac{.054}{.0044+.054} = .925$**


Q3b (Not a!)
 * Note this refers to the table *above* not below
 * You should find you need to compute new values only for one cluster.  Why is this?
 * Factor $\Sigma_1$ into $Q \Lambda Q^{-1}$ form.  (Note that there are many online sources for diagonalizing and inverting matrices.) Explain why the resultant Q makes sense by drawing a diagram of the 5 X points and $\mu_1$ and estimating the implied scaling values and rotation value for $C_1$.  This will also serve as a reality check on your $C_1$ computations.
 * Compute all the way through the new $w_{ij}$ values, but compute only $w_{11}, w_{12}$, and $w_{13}$.
 * Submit precisely these new values, showing your work, and highlighting these values on the page: $\mu_1, \mu_2, \Sigma_1, \Sigma_2, \Sigma_1^{-1}, P(C_1), P(C_2), w_{11}, w_{12}, w_{13}$

 **The interesting thing here is that the w values are preset, so we don't need to know prior $\theta$ values, and also they are uniform, so both clusters will have identical $\mu$, $\Sigma$ and P values.  

 So, we have $\mu_1 = \mu_2 = \frac{\begin{bmatrix}5.75 && 2 \end{bmatrix}}{2.5} = \begin{bmatrix}2.3 && .8 \end{bmatrix}$

 And, $\Sigma_1 = \Sigma_2 = \ \frac{\begin{bmatrix}25.8 && -5.68 \\ -5.68 && 4.8\end{bmatrix}}{2.5} = \begin{bmatrix}10.32 && -2.27 \\ -2.27 && 1.92\end{bmatrix}$

And, $\Sigma^{-1} = \begin{bmatrix}.131 && .155 \\ .155 && .704\end{bmatrix}$

And $P(C_1) = P(C_2) = .5$

Computing the w values is actually trivial, since the two clusters have identical $\mu$ and $\Sigma$.  Each w value must be .5 as a result.

And this means the algorithm will never make any progress.  Lesson learned is to start with asymmetrical values, or with actual random cluster stats.

### Bayes' Theorem

1. Today is after the 29th of the month (the 30th or 31st).  What is the chance that the month is March?

$P(March|date) = \frac{P(date \land March)}{P(date)} = \frac{2}{18} = .111$

2. You take a test with a 5% false positive rate and a 10% false negative rate.  (%5 of the positive results are incorrect, as are 10% of the negative results.)  You test positive, but you also know that on average, only 1% of the population is actually positive for this test.  What is the chance that your positive test is accurate?  (Your answer should make use of both the false positive and false negative stat)

$P(real|pos) = \frac{P(pos \land real)}{P(pos \land real)+P(pos \land \lnot real)}
 = \frac{.90 .01}{.90 .01 + .05 .99} = .154$

3. A college has these statistics.  What is the chance that a random CSCI major, who we know is not a senior, is a freshman?

|Class | % of all students | % that are CSCI majors |
|--------------|-----------|------------|
| Freshman     | 30    | 4       |
| Sophomore   | 25  | 8       |
| Junior    | 20  | 9       |
| Senior     | 25  | 7       |

** $P(Fr|CSCI) = \frac{P(Fr \land CSCI)}{P(Fr \land CSCI)+P(So \land CSCI)+P(Jr \land CSCI)} = \frac{.3(.04)}{.3(.04)+.25(.08)+.2(.09)} = .24$


