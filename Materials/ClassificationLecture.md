# Supervised Learning and Classification Lecture 

* These methods are all about supervised Learning.  We *know* the classes.

# Bayesian Classification
* Review EM Clustering if already done
* Review Eq 18.2 -- 18.5
* Does this sound familiar? **Should see it's the same ideas as EM clustering with mixed gaussian model**
* What is difference? 
   * We already *know* who belongs to what cluster, so this is about using that knowledege.
* Alg 18.1
  * Doing full Gaussians at this point
  * Dimensions of vectors (all un-transposed are vertical, per book standard).  Relevant variables are n samples, d dimensions, k classes
  * $D_i$? **$n_ixd$, varying per i**
  * $\hat{\mu_i}$? **1xd**
  * $1_{n_i}$? **$n_i$x, all 1s** 
  * $\bar{D_i}$? **$n_ixd$, varying per i**
  * $\bar{D_i}^T\bar{D_i}$? **dxd, a covariance total**
  * $\hat{E_i}$? **Also dxd -- covariance matrix**
  * $\hat{y}$? **scalar, identifying class of x**
  * Order of complexity
    * For training? **$O(nd^2)$ due to line 7**
    * Does this depend on k? **No, since each op is n/k**
    * For classification? **$O(kd^2)$ due to $\Sigma$ product in numerator**
* "Naive Bayes"
  * Naive in the sense of Eq 18.9
    * What does this say? **Distribution in each dimension is independent**
    * So, for instance, true for:
       * Housing size and distance from town? **Possibly**
       * Housing size and housing price? **No, not really**
       * Height and width of a character image? **Sure**
       * Fig 18.1? **No!**
   * So, what if each dimension/attribute is a univariate normal distribution, with a $\mu$ and $\sigma^2$?
     * Recall homework first week.  What does the multidimensional distribution for a class look like? **Multivariate normal, but axis aligned**
     * And what does $\Sigma$ look like? **Diagonal, with $\sigma_i^2$ values** 
     * To be clear, Naive Bayes, and Bayes in general, does not demand normal distributions, but this is often the choice.
   * Alg 18.2
     * Where different from 18.1?
        * Line 8 is, I think, a bug.  What is $\bar{X_j^i}$, and how would we instead get it from $\bar{D_i}$? **J'th column of $\bar{D_i}$**
     * Line 11
        * How is this related to line 8 of Alg 18.1? **Multivariate axis-aligned computed as product of univariates per axis**
     * Order of complexity
       * For training? **$O(nd)$ due to line 7**
       * For classification? **$O(kd)$**
* Categorical Attributes with Bayesian Estimation
   * p 473 in Zaki
   * "multivariate Bernoulli random variable", more commonly "categorical distribution", is simply a discrete probability distribution on a set of possible outcomes, e.g roll of a dice
   * $e_{j1}$, etc represent what? **One-hot vectors**
   * Understand the v vector.  
      * Say I have three categories, with 5, 8, and 4 choices each.  
      * What is $m_j$?  $d'$? **number of choices for each (5,8,4) and total choices 17**
      * What is dimension of v, then? **17, with 5, 8, and 4 parts**
      * How many possible collective values?  **5(8)(4)=160**
      * Why merge three properties into one big property like that? **Allows correlations to be considered.  We already "merge" continuous properties into one hyperdimensional point, after all, for the same reason.**
      * $\hat{f}(v|c_i)$ value.  Just the percentage of $c_i$ instances that exhibit v.
      * But might some v value never appear, say if we have 10000 instances and 160 possibilities? **Possibly, if some vs are just unusually rare**
        * So what? If this occurs, what is the effect on the Bayes equation for one class with no instances? **Posterior probability is just zero for that class**
        * But, what if v doesn't appear in *any* class sample?
           **OK, now we have posterior probability of $\frac{0}{0}$ -- uncool
      * Compensation in eq 18.8.  
         * Given a $c_i$ with 500 representative samples, what will be the min value for $\hat{f}(v|c_i)$? **1/660 = .0015**
   * What would be the "naive" equivalent of what we just analyzed for categorical properties?  What changes?
     * **Each property stands alone with its own probability, as a separate "dimension"**
     * **We only add a "1" for each categorical value, not for all combinations thereof.**
     * $P(x|c_i) = \prod_{j=1}^d P(x_j|c_i)$ and $P(x_j|c_i) = \frac{n_i(x_j)}{n_i}$
      * OR, if we add extra counts like before, we need one per value and attribute, not per all attribute combinations: $\frac{n_i(x_j)+1}{n_i+m_j}$
     * So, for our running (5, 8, 4) example, and a $c_i$ with 500 samples, what's the min probability for a given 3-attribute combination? **It's actually more precise: $\frac{1}{505(508)(504)} = 7.7x10^{-9}$**
     * And, the odds of each combination assuming exactly 3 samples each?  
        * What is $n_i$ in that case? **$160*3 = 480$**
        * Full Bayes odds? **$\frac{3+1}{640} = .00625$
        * Naive Bayes? **\frac{97}{485}\frac{61}{488}\frac{121}{484} = .00625$
        * Always the same? **No, just this time due to independence.** 
        
* "Nonparametric" statistics and classification
  * Parametric (broadly, traditional) stats assume some probability distribution at work (e.g. normal, binomial, etc) and attempt to estimate its paramters (e.g. $\mu$, $\sigma) via sample data.
  * "Nonparametric" can be used in subly different ways but essentially means classification by algorithms other than fixed statistical probabilities and their parameters. (e.g. neural networks, k-nearest neighbor, decision trees)
  * "Nonparametric" methods have parameters, often vastly more than parametric methods, but these characterize a nonprobabilistic model, e.g. the weights of a neural network, the centroids of a cluster, the cutting hyperplanes of a decision tree, etc.).  
    * One telltale difference: the answer to the question "how many parameters do we need?".  
       * Parametric: the number determined by the relevant probability distribution, e.g. 9 for a trivariate normal.  (Why 9 values,btw? **3 for $\mu$ and 6 for $\Sigma$)**
       * Nonparametric: "I dunno, how many do you want??" (Tradeoff between lack of power and overfitting)
    * Another: "What might be a good regularization of the parameter space?"
      * Nonparametris: "You might limit overall magnitude of the parameters (neural nets), or limit the conditions in which you introduce further parameters (decision tree min leaf size)
      * Parametric: "What the hell is `regularization`?"
* Probabilistic K-nearest Neighbor
  * Example nonparametric, though still probabilistic
  * $B_d(x,r)$ meaning.
   * Not a hypervolume; a set of sample points  
  * Choose r such that $|B_d(x,r)|$ = K
  * Eq 18.11, intuitively, means what? **Pick the class most represented among your K neighbors**
  * Starting with Eq 18.10, for a subtler intuitive justification
    * Why does this reasonably represent the likelihood of x, *assuming $c_i$?* **Because it gauges the proportion of $c_i$ that is in the neighborhood, further conditioned by neighborhood size.**
    * Can $\hat{f}(x|c_i)$ be larger for class $c_i$ than for class $c_j$ if the latter has more points in the neighborhood? **Sure, if $n_i$ is lower than $n_j$ so $c_i$ has more "skin in the game"**
    * Intuitive meaning of $\hat{f}(x|c_i)$? **Density of class i in hyperball volume V, meansured not by count, but by proportion of class i's total representation**
    * Not tie this into Bayesian equation following it. Math shows that the intuitive $\frac{K_i}{K}$ is actually justified by Bayesian logic.

## LD Analysis
  * Review projection concept (first eq in ch20)
  * Fig 20.1
    * Note that only w orientation is relevant.  Try moving W to origin.  Changes nothing.
    * $\bar{D}$ is assumed in much of this
  * Mean of projection is projection of mean
  * Consider a case where means are aligned on w = [.707, .707] but serious overlap occurs.
     **Two ellipses of points with long axes SW/NE, and means slightly
     apart will do this**
  * Case where we still might be able to separate them?
     **Turn each long axis clockwise a bit, to pull them apart from each other while keeping
     the same means**
  * Scatter concept
     * Why not divide by n?  **Allows more populated classes to dominate, like P(C) in EM clustering**
  * Eq 20.2 pattern
    * Follow second line carefully.  Note that $x^Ty = y^Tx$ iff x and y are one-dimensional
    * Matrix B allows determination of squared mean distance for any $w$
    * What is rank of B?  Try multiplying a vector through its expaneded version.
  * 20.3 Same pattern for total scatter (squared variance)
    * What is rank of this matrix?  **Up to d, not necessarily 1.  Positive semidefinite**
    * Ditto for total of the two S matrices
  * Eq 20.8: 
     * Why is $\frac{d}{dx} w^TBw == 2Bw$?  Is this always true?
        * Conrete example with $B = \begin{bmatrix}a&&b\\c&&d\end{bmatrix}$
        * $w^TBw = ax_1^2 + bx_1x_2 + cx_1x_2 + dx_2^2$
        * $\frac{d}{dw}w^TBw = \begin{bmatrix}\frac{d(w^TBw)}{dx_1}\\\frac{d(w^TBw)}{dx_2}\end{bmatrix}
     = \begin{bmatrix}2ax_1 + bx_2 + cx_2\\bx_1 + cx_1 + 2dx_2\end{bmatrix}
     = 2\begin{bmatrix}ax_1 + bx_2\\cx_1 + dx_2\end{bmatrix}$ 
        * So true iff b = c, or more generally B is symmetric.
  * EQ 20.9
    * Follow eigenvector math
  * Follow alg 20.1
  * Intuition
    * S is the transform that describes the "spread" of the two clusters (weight-averaged over both)
    * $S^{-1}$ is the transform that pulls them back to circular/hyperspherical shape
    * What is B?
      * Is it nonsingular or singular? **Singular**
      * To what space does it map vectors? **To the $\mu_1 - \mu_2$ line**
    * $S^{-1}B$ thus represents that mapping, reoriented by removing the spread.
  