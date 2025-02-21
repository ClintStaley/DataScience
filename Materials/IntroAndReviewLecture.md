# Intro and Review

## First Day
 * Syllabus review
   * Challenging course
   * Importance of topic
   * Individual work on coding/assignments

 * Self-study methods
   * multiple sources
   * Try CONCRETE EXAMPLES

## Data, patterns, and high-dimensional space review
* Raw data overview 
  * data types
  * discrete/continuous
  * interval-scaled/ratio-scaled
  * categorical/numeric attributes
  * nominal/ordinal
  * Notion of pattern spaces
  * Examples of continuous data
    * Numberline-based, int or float
    * income, debt, income growth rate
    * purchase volumes for each month of year
    * square footage, age, neighborhood ranking
    * grayscale image
  * Example of discrete ordinal data
    * education level
    * age group (sometimes there's an underlying continuous variable)
  * Example of discrete nominal data
    * Zip code
    * gender
  * Discrete one-hot vs discrete sets
 * Translation of continuous data to points in space
 * Translation of discrete, ordinal data similarly
 * Nominal ("just a name") categorical data results in one dimension per possible value
 * Vector spaces brief reminder (should be obvious by now)
    * N dimensional hypercube has how many corners?
    * Using example of imanges
      ▪ What do "nearby" patterns look like?  
      ▪ What does a midpoint pattern look like?
      * What is a "convex" subspace?
    * Defining a hyperplane with perpendicular and distance

## Math Review/Basics
* Vector math review
  * Dot product and projection
    * What is projection (scalar) of (1, 2, 3) along direction of (2, 1, -2)? **Unit is (.667, .333, -.667), so projection is -.667**
    * What is the vector projection of (1,2,3) on that direction? **.667(.667, .333, -.667) = (.444, .222, -.444)**
    * What is the angle between (1, 2, 3) and (1, -2, 1)? **Dot product of 0 means 90 degrees*
* Bit of linear algebra review
  * (Text uses T notation for transpose)
  * Matrix as linear transform
    * Simple Example: $\begin{bmatrix}1&&2&&-1\\2&&1&&2\\0&&-3&&4\end{bmatrix}$
    * What do unit vectors translate to?
    * Do G-J elimination
       * $\begin{bmatrix}1&&0&&1.67\\0&&1&&-1.33\\0&&0&&0\end{bmatrix}$
    * What is rank, rowspace, colspace? **2, top two rows of G-J, first/second original cols since these are pivots**
    * What is determinant?  Why? **0, since rank < 3**>
    * Compute nullspace? **Set third value to 1, compute necessary first/second vals to satisfy Mx = 0: (-1.67, 1.33, 1)**
  * Symmetric matrices (we'll deal a lot with these)
    * $Q^{-1}\Lambda Q$ form, with Q orthonormal and $\Lambda$ diagonal
    * Positive semidefinite if all eigenvalues are nonnegative
       * $x^TMx >= 0$ 
      * Dot product of transformed x and x itself is nonnegative
      * What does this say about the "shape"  of the linear transform M? **skews sphere into ellipsoids without inverting or over-rotating**
  * Outer product $P = xx^T$
    * We will use something similar in probability in form of correlation matrix
    * $Pu = xx^Tu$ projects u onto x via dot product, then remultiplies by x
    * Brief example using x = $\begin{bmatrix}1\\3\\-2\end{bmatrix}$ What is $xx^T$? 
      **$\begin{bmatrix}1&&3&&-2\\3&&9&&-6\\-2&&-6&&4\end{bmatrix}$**
    * Nullspace? **Orthogonal to x**
    * Left nullspace? **ditto**
    * rowspace? colspace? **both x**
    * Positive definite? **No, but positive semidefinite**
    * Any other distinctive property? **symmetric**

* Probability review
  * discrete probability
    * Discrete, possibly nominal sample space
  * continuous probability
    * Continuous, necessarily ordered, sample space
    * P(X=x) = 0 for any particular x!
    * Value of CDF for dealing with this (differential values)
  * mean, median, mode as measures of a probability distribution
  * variance and std deviation.
    * Follow logic of Eq 1.8 simplification from Zaki p. 11
  * Binomial distribution as example of discrete distribution
    * m 0/1 tries, each with p likelihood of a 1.  What are odds of k 1's?
    * View as m 0/1's, with k being 1s.
      * How many different such patterns? $m \choose k$
      * Likelihood of a specific pattern,  with each outcome exactly as specified...
        * failures (1-p) likely, successes p likely
        * $(1-p)^{m-k}p^k$
        * thus ${m\choose k} p^k (1-p)^{m-k}$
        * Roll a die 7 times, get exactly 3 1's?  **${7 \choose 3} = 35$, each with $0.1666^3 0.8333^4 = .00223$, so .078**
    * Single try is called a Bernoulli distribution, e.g. one flip of a (possibly unfair) coin with probability p of a head
    * Binomial distribution is thus the outcome of m Bernoulli trials.

  * Joint or multivariate distributions
    * Discrete case has already been covered
    * Marginal probablities
    * Conditional probabilities, e.g. P(color|normal), p(red|normal)

| | red | non-red |
|---|---|---|
|normal | .1 | .5 |
|sports | .2 | .2 |

*
  *
    * Continuous has analogous ideas. f(x,y).  Zaki p 22.
    * How would we do a marginal distribution for, say, x? **Integrate across y for the given x values: $f_X(x) = \int_{-\infty}^{\infty} f(x,y)dy$**
    * What about conditional probability? **Divide to arrive at area of 1: $f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)}$**
    * Independence: $p(x,y) = p(x)p(y)$ 
      * Can $p(x,y) < p(x)p(y)$?  How much less if so?  **p(x,y) can be zero even if p(x) = p(y) = 1$**
      * Same question the other way.  Can $p(x,y) > p(x)p(y)$?  How much greater if so?  **$p(x,y) = p(x) = p(y)$ is possible**
  * Probability chain rule
    * p(red, sports) = p(sports)p(red|sports) = p(red)p(sports|red)
    * Do math **.2 = .4(.5) = (.3)(.667)**
    * Full version accommodates many variables 
      * Is this right? p(a, b, c) = p(a)p(b|a)p(c|b) **No, need p(c|a,b)**
    * $p(x_1,x_2, ... x_n) = \prod\limits_{k=1}^n{p(x_k|x_1, ... x_{k-1})}$
  * Bayes Theorem
    * Relates p(x|y) to p(y|x)
    * In example above, what is p(red|sports)? And p(sports|red)? **.5 and .67** 
    * How can we compute the latter? 
      * $p(sports|red) = \frac{p(sports, red)}{p(red)}$
      * If it's red, that's the "evidence" -- a subset of the probability space
      * Probability of "sports", given red, is the p(sports, red) portion of this space.
      * Compute it: **.2/.3 = .67**
      * Other ways to look at it:
        * Via chain rule $p(sports|red) = \frac{p(sports)(p(red|sports)}{p(red)}$
        * $p(x|y) = \frac{p(x)p(y|x)}{p(y)}$
        * Or a shift of "viewpoint" $p(x|y) = p(x)\frac{p(y|x)}{p(y)}$
        * $p(hypothesis|evidence) = p(hypothesis)\frac{p(evidence|hypothesis)}{p(evidence)}$  Sometimes p(evidence) is called "marginal" since that's how we generally get p(evidence), e.g. adding up marginal red probability.
        * ${posterior} = {prior}\frac{p(evidence|hypothesis)}{p(evidence)}$
          * Generally, x is such-and-such likely, but seeing y, we update it by the chance y would occur assuming x.
          * Generally, .4 of cars are sports, but we update that by p(red|sports)/p(red) or (.5/.3) to arrive at .667 for p(sports|red)
        * May need to 
      * I have a set of 4 fair coins and 6 loaded ones, the latter having .75 likelihood of a head.  I grab a coin, flip it, and get a head.  What is the chance it's a loaded coin?
        * **$p(loaded|head) = p(loaded)\frac{p(head|loaded)}{p(head)}$**
        * **p(head) is p(head|loaded)p(loaded) + p(head|fair)p(fair) = .75(.6) + .5(.4) = .65**
        * So, .6(.75/.65) = .692
        * Do same for p(fair|head) to confirm
      * You have a bin of parts, from three makers: 5% from maker A, 45% from B, and 50% from C.  Maker A's parts are 40% defective, B's are 4%, and C's are 1%.  You draw a part at random, and it's defective.  What is the chance it's a maker-A part? **.465**
  * Normal distribution as example of continuous
     * Examine equation $\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
     * General shape, meaning of symbols
     * Symmetrical about ??  **mean**
     * Impact of squared stdev in power denominator? ** Higher stddev results in wider curve, squared means symmetrical
     * What should area under curve be? **1**
     * What happens to area as stdev rises, absent compennsating leading fraction? **Gets too large since same heights, but wider**
     * Purpose of leading fraction?  **Normalize to integral of 1**
     * Actual integration is a royal pain, so I won't drag you through it.
     * Why bother with this?
      * What is the Central Limit Theorem?  **Lookup shows it's the limit of sample mean for most actual distributions.**
      * Also has maximum entropy (most uncertainty) for any distribution where you specify the mean and variance.  
        * Why not uniform distribution, which normally is most surprising? **Cannot extend infinitely if variance is known**
      * Foundational in many AI algorithms (Naive Bayes estimation, gaussian "splats" for 3-D vision, VAE latent variables, etc.)
      * Generally appears *in multiple dimensions* however
    * $\mathcal{N}(\mu, \sigma^2) notation$
    * Standard normal has mean 0 and variance/stdev 1
  * Use of cumulative table (See image)
    * Notion of z-value
    * Chance of more than 2 stdevs from mean?  3? 

  * Multivariate normal
    * $\frac{1}{\tau^{\frac{k}{2}}\sqrt{det(\Sigma)}}e^{-\frac{(x-\mu)^T\Sigma^{-1}(x-\mu)}{2}}$
    * $\Sigma$ is *covariance matrix*.
      * positive semidefinite
      * transforms sphere to ellipsoid shape
      * eigenvectors are the axes, eigenvalues the lengths, and conditional variances
      * Why *inverse* transformation in exponent? **Reversing the spread back to a sphere, and using that for probability computation**
      * But don't we need to "reverse" both vectors? **Sigma is squared**
      * Why dot product? **Like the squared mean-distance in univariate**
      * Why root of determinant? **Like normalizing with stddev**
  * Drill down on covariance matrix
      * Formally, elements i,j are $E((X_i-\mu_i)(X_j-\mu_j))$
      * Assume mean of 0, or equivalently subtraction from mean
      * n variables $x_i$
      * Row i, col j, compares $x_i$ with $x_j$.  Expected product.
      * Symbol is either $cov(x_i, x_j)$ or $\sigma_{ij}$
      * What is $\sigma_{ii}$ the same as?  **Variance for $x_i$**
      * How does $\sigma_{ij}$ relate to $\sigma_{ji}$? **Equal**
      * What values can covariance take? **Full range neg to positive**
      * What does coveriance look like for independent variables? **zero**
      * Does zero covariance imply independence?  **No, there can still be patterns but they don't skew**
      * What does $\Sigma$ look like when variables are all independent? **Diagonal**
      * What comments might we make of this covariance matrix, on cars, with dimensions mileage, cost(K), performance, reliability: 
      $\begin{bmatrix}&&mil&&cost&&perf&&rel\\mil&&100&&1&&-20&&1\\cost&&1&&100&&2&&20\\perf&&-20&&2&&9&&2\\rel&&1&&20&&-2&&4\end{bmatrix}$
        * **Mileage and performance are inversely correlated, as is reasonable**
        * **It's not a covariance matrix since not symmetrical**
        * **Cost and reliability correlated, again as is reasonable**
        * **Reliability and mileage, cost and mileage, cost and performance, all largely unrelated**
        * **Variances of mil and cost exceed those of perf and rel, but this can be simply a matter of units used, e.g. reliability as a 1-5 score**
      * Covariance matrix is structured much like outer-product matrix, but does this mean it's rank 1?  Is it just $E(X-\mu)E(X-\mu)^T$? **No, because $E((X_i-\mu_i)(X_j-\mu_j)) <> E(X_i-\mu_i)E(X_j-\mu_j)$ and expectation of product is not product of expectations**
      * Indeed, under what circumstances are those two the same, and what *is* $E(X_i-\mu_i)E(X_j-\mu_j)$? **Independent distributions, and 0**
      * Give an example of a realistic *continuous independent* joint distribution, and describe its covariance matrix.
  * Related idea of *correlation matrix* normalizes so that $\sigma$ values aren't a factor:
    * Formally, i,j are $\frac{E((X_i-\mu_i)(X_j-\mu_j))}{\sigma_i\sigma_j}$
    * What range of element values does this imply? **-1 to 1 inclusive**
    * Give correlation matrix for prior (repaired) example: **$\begin{bmatrix}&&mil&&cost&&perf&&rel\\mil&&1&&.01&&-.5&&.05\\cost&&.01&&1&&.067&&1\\perf&&-.5&&.067&&1&&-.33\\rel&&.05&&1&&-.33&&1\end{bmatrix}$**

  * Demo a Galton board
    * Given the balls bounce left/right randomly 50/50, what is the actual distribution? **Binomial**
    * But, what curve actually arises from many binomial trials? **normal**

  * Statistical sampling
    * A *statistic* is some numerical measure of a sample of a distribution
      * Can be mathematically identical to measures like mean, variance, but maintain the distinction -- it's on a *sample*, without assuming the underlying distribution.
      * A statistic is its own random variable.  A statistic that is the mean of n samples has its own mean, variance, etc.
    * **Empirical PMF**.  Probability distribution *as determined by the sample*.
      * Imagine you don't even *know* the underlying PMF
    * Consider the statistic of a sum of n independent samples: $\sum_1^nx_i$
      * Assume we do n samples, and compute the sum, over and over, to get many sample sums.
      * What is the mean of such a statistic? **$n\mu$, for obvious intuitive reasons.**
      * Can also be geometrically "seen" as center of mass of the sample points.
    * Expected *variance* of n-sample-sum is more complex.
      * Sum is on average n times a sample size, so do we expect n-squared the variance?  **Not necessarily because mean of a set of n-samples won't actually be $\mu$**
      * Essential point is that $E(((\sum_1^nx_i)-n\mu)^2)
       = E((\sum_1^nx_i-\mu)^2)\ = E(n(x_i-\mu)^2) = nE((x_i-\mu)^2) = n\sigma^2$
      * We can replace the summation with an n-factor because $E((x_1-\mu)+(x_2-\mu)+...+(x_n-\mu))^2 = E((x_1 - \mu)^2 + (x_2-\mu)^2 + ... + (x_n-\mu)^2 + (x_1\mu)(x_2-\mu$ + *other mixed terms*)
      * For any mixed term $E(x_i-\mu)(x_j-\mu)= 0$
        * Assuming what condition, and why? **Independence, so that each term will be negative/positive at same rate.**
    * OK, so variance of a sample-sum grows with n, but not as $n^2$, because only "aligned" terms of the summation actually contribute to the variance.
  * Now, what about n-sample-average: $\frac{1}{n}\sum_1^nx_i$ What is this statistic's mean? **$\mu$, obviously**
  * And its variance? 
    * How does it relate to the variance of the sample-sum? **Each term in the sum is multiplied by $\frac{1}{n^2}$**
    * So, variance is $\frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}$
  * Variance of n-sample-average reduces by 1/n, and stddev by $\frac{1}{\sqrt n}$
    * Is sample average *actually* the same as $\mu$ every time? **No, its expected value is $\mu$ but it has a variance equal to $\sigma^2/n$
    * So is n-sample-average variance (squared difference from *sample average*) different from actual variance? **Yes, we'd intuitively expect the sample average to reduce sample variance by a factor of 1/n**
    * In particular, consider Zaki eq 2.18/2.19.  Sample variance is indeed $\frac{n-1}{n}\sigma^2$, so we compensate by estimating actual variance from sample by using n-1 in denominator, not n.

  * I flip a coin 1,000 times.  What is the chance the total heads is between 490 and 510?
    * What is the distribution involved? **Binomial**
    * stddev of the Bermoulli 1-coin flip is, assuming tail is 0 and head is 1? **$sqrt{0.25} = .5**
    * stddev of a 1000-coin sample-sum? ** $.5\sqrt{1000} = 15.8$
    * What z-score is indicated? **10/15.8 = .63 stddev**
       * Do we need to find this for binomial distr? **No,Use a normal table.**
       * Value is? **.236*2 = .472**













