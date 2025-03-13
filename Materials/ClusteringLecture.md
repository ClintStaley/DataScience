# Clustering Lecture

* Section 13.1 KMeans
  * Review basic idea
  * 13.1 algorithm. 
     * argmin meaning
     * Why *squared* norms? **Same comparison, no sqrt needed**
     * [Animation](https://www.youtube.com/watch?v=9nKfViAfajY)
  * Convex nature of regions
     * Remind of limits on convexity, e.g. for MNist data
* Section 13.3
  * Review multivariate normal 13.6
     * What if $\Sigma = I$?
       * **Symmetric around mean, with squared distance as exponent**
     * $\Sigma$ in general
       * Positive semidefinite
       * Factorable as $QDQ^T$ with Q orthonormal and D pure diagonal
       * All diagonals positive
       * Visual picture: rotate from arbitrary ortho axes to X,Y,Z, then scale, then rotate back.
       * So, orthogonal scaling with arbitrary axis alignment.
       * Create one: Scale by 2 along (1, 1, 1), by 3 along (1, -.5, -.5) and by 4 along (0, 1, -1)
     ```
     Orthonormals are (.577, .577, .577)  (.816, -.408, -.408) (0, .707, -.707)
     Use Wolfram or equiv to multiply all together
     ```
     * Determinant review
      * Volume of transformed unit cube
      * What would we expect for our just-computed matrix? **2*3*4 = 24 Check WA**
  
    * Compare to univariate normal.  (section 13.3.1 p345 has one)
       * Where is $\sigma$?
       * Try 1x1 $\Sigma$
       * What 1x1 matrix for $\Sigma$? **$[\sigma^2], so \Sigma^{-1} = \frac{1}{\sigma^2} and |\Sigma|^{1/2} = \sigma$**
       * Note squared is needed
       * Tie back to full $\Sigma$ being a squared $QDDQ^T$, since of course it's squared sums.
       * Why $\sqrt{|\Sigma|}$ in denominator?

  * Now do EM Clustering
    * Cluster centers turn to normal distributions
    * Weighted by probability "mixture parameters"
    * Eq 13.7 Discuss, then ask for intuitive description.  **How likely is x, under the present clusters and mixture parameters?**
       * Is f(x) a probability distribution? **Yes, as weighted sum of distributions**
    * Eq 13.8 Discuss and ask for intuition.  **How well do the present clusters predict all of D? (as log)**
    * Eq 13.9.Discuss and ask intuition. **How likely is it that $C_i$ predicted $x_j$, or that $x_j$ resulted from $C_i$? or How much does $C_i$ "like" $x_j$?  Should $x_j$ be in $C_i$'s cluster?**
      * Brief look at $\epsilon$ reasoning just prior.
         * Can we just directly use the f values? **Yes, since $\epsilon$ is the same for all**
    * Frame this in LA terms
      * 1-D example (simpler since $\Sigma$ is scalar $\sigma$)  
         * $w_i$ vector (which is vertical)
            * Does it have any zero values? **No**
            * Is it a probability **No, not across j**
            * What would equivalent vector be in K-means? **one-hot vector**
            * Description intuitively? **How does $C_i$ like all the data points? or How likely is each under $C_i$?**
      * Equations leading up to 13.10
         * Vector notations, for numpy and GPU
         * $w_{ij}$ is probability in which directions? **Across i, but not j**
      * Eq 13.10.  Discuss.  
        * Ask intuitive meaning.  **How popular is $C_i$?**
        * Equivalent in K-Means? **How many points in the cluster?**
        * Can we do all of these, across all i's, without loops?
          * Yes, numpy operations. W becomes ixj matrix.
      * Review sample results in Fig 13.4
        * Advantages of this over k-means?  **probabilistic assignment, so
         point categorization can be "fuzzy".  Also size of clusters, in the form of the $\Sigma$ value
    * Full example with multivariate normals
      * Diagonal simplification
         * What shape do the clusters take in this case? **axis aligned**
         * Not necessary except in high dimensions.

      * EQ 13.11 
         * Definition of $w_{ij}$ is important: "How likely is it that $C_i$ caused sample $x_j$?".  And $\bm{w_i}$ is vertical vector of weights for one $C_i$
         * Assume 100 3-D points.  Dimensions of the matrices in matrix version of 3.11 are?? 
            * **D is 100x3, so $D^T$ is 3x100. $w_i$ is 100x1, $w_i^T$ is 1x100, $\bm{1}$ is 100x1$&**
         * Intuitive interpretation?  **Weighted average of all points by "closeness" to $C_i$**
         * Is this a weighted average with total weight of 1? **Yes, due to denominator**

      * EQ 13.12
         * Dimensions of matrices $\bar{D}_i, \bm{1}, \mu_i^T$? **$\bar{D}_i$ is 100x3, $\mu_i^T$ is 1x3, $\bm{1}$ is 100x1 and $\bm{1}\cdot\mu_i^T$ is 100x3 which is perhaps surprising**
         * What is centroid of $\bar{D}_i$? **origin**
         * Meaning of **$\bar{X}_{ji}$? **Sample j relative to center of class i**
         * Dimensions of matrices in 13.12 itself and of the product in the numerator? **$\bar{X}_{ji}$ is 3x1 so $\bar{x}_{ji}^T$ is 1 x 3, product is 3x3, $w_i^T$ is 1x100 and $\bm{1}$ is 100x1$**
         * Outer product concept
            * vertical dot horizontal (transpose)
            * or can be written $u \otimes v$
         * So, weighted sum of correlation matrices
         * Analagous to what 1-D equation? **Computation of $\sigma^2$ earlier**
         * Eq 13.12 is a no-loops numpy operation!

      * Eq 13.13
        * Can $P(C_i) = 0$? **No, always some probability**
      * [Illustration](https://www.youtube.com/watch?v=eXdGCO-2n90)

      * Algorithm 13.3
        * Line 8 equates to what in the KMeans algorithm? **Distance from j to i centroid**
        * What equation above is line 11 implementing?
        * How does this change if we use a diagonal covariance matrix per the suggested optimization? **Line 11, create diagonal by single loop iteration through $x_j - \mu_i$**
      * Complexity
        * Determinant is $O(d^3)$ -- done by GJ elimination for which each of d steps is $O(d^2)$
        * Why is f computation $O(d^2)$? **Multiplication through $\Sigma$ takes $d^2$ steps.**
        * Going with pure diagonal drops to d not just $d^2$.  Why? **Determinant is now just O(d)**
        * Overall $O(nkd^3)$ or just $O(nkd)$.  What's the big cost in the former case?  **Dimensionality**
        * What type of situation would make you want to go with just the diagonals? **Large d, so points with many attributes**

      * Note that this all is intuitively reasonable, but not *proven* to provide optimal results.  Don't bother with section13.3.3, though it's very interesting math and may be covered in AI under VAEs.

* Density clustering
  * Fig 15.1 and 15.2.  Concept of core, border, and noise
    * Can all points in a core neighborhood be border? **Sure if all are on edge**
    * Can none be border? **Yes if in the middle of core density area**
  * Density-reachability.  
    * Why nonsymmetric?  **x need not be core point**
    * Symmetric if all points are core? **Yes**
  * DBScan Alg 15.1
     * Read and explain
     * Concept of flood fill
     * Is order of graph search DFS or BFS? **DFS**
     * Error in loop 12-17? **Yes, it doesn't flag already visited**
     * Can cores compete for a border?  If so, who wins? **Yes, highest k**
   
  * Concepts of density
     * Start at Eq 15.3
       * Unidimensional for now
       * Notion that $x - x_i$ is normalized by h.  Like z-values
       * What happens as $h \rightarrow 0$? As $h \rightarrow \infty$? **Infinte spikes of density;s uniform $\frac{n}{h}$ thus dropping to zero**
       * Fig 15.5
     * Eq 15.5
       * Essentially a z-distribution
       * How many points are in the neighborhood of x? **All of them**
     * Eq 15.6
         * Why $h^d$? **hypervolume of hypercube**
         * Can one point be out of neighborhood, but still be closer than points in neighborhood?  **Yes, sides vs corners of hypercube**
     * Eq 15.7
         * What if we use $|\bold{z}|$ rather than $|z_j|$? **We get hypersphere not hypercube.**
     * Eq 15.8-9
         * Shape of neighborhood? **Hypersphere, not hypercube**
         * What if we consider one dimension more important than another? **Adjust $\Sigma$**
     * Fig 15.8
     * 15.2.3
         * Define neighborhood by point count, not distance
         * Plusses/minuses? **No anomalous zero-data regions; varying precision**
         * Is it continuous or discrete in x? **Discrete**

  * DENCLUE algorithm (15.2.2)
      * Brief reminder of gradient ascent
      * Eq 15.10
        * What is $\Sigma$ in the kernel, and why? **It's I, because we don't weight different dimensions differently in measuring volume**
        * What is tensor shape of $\frac{\partial\hat{f}}{\partial\textbf{x}}$?  **Vertical vector of dimension d**
        * How about $\frac{\partial\textbf{z}^T\textbf{z}}{\partial\textbf{x}}$ with x and z vectors?
           * Write the dot product
           * Consider partial wrt $x_1$ as example
           * Remaining terms drop out
           * Summarizing form as $-\textbf{z}\frac{\partial\textbf{z}}{\partial\textbf{x}}$
         * If I am on the SE side of mean, in a circular K, what does z look like? What gradient direction results and why? **z points NW, proportional to distance from mean/h**
         * How does reducing h affect the derivative, and why **Increases it because slope of distribution is increased by reducing h, proportionally, and because K value is raised**
      * eq 15.11
      * eq 15.12  
         * What are the $x_i$ values in the landscape? **peak points**
         * Which peaks will pull most? **Closest ones**
         * What is sum of all "pull" factors? **1, due to denominator**
      * Alg 15.2
        * Meaning of each parameter?
        * A is set of maxima, *not* in the actual dataset
        * R are points attracted to As
        * How do we implement line 7??

* Hierarchical Clustering
  * Basic concept. 
    * Example 4.1
    * Note one can choose a number of clusters post-analysis
  * Ignore math for number of partitions.  Just "really big"
  * Alg 14.1
    * Very simple algorithm.  It's about how you choose closeness, and how you track pairwise distances.
  * Read distance math
    * They explain meaning of each expression up to Ward's
    * Ward's
      * SSE vs variance
        * Is this basically a measure of cluster "diameter"? **No. Not divided\
          by n, so larger for bigger clusters same diameter**
      * Follow math
        * 14.6 What happened to middle term? **Same as classic variance computation.  $x^T$ sums to $n\mu$**
        * 14.8 
          * Why do summations cancel? **ij summation is total of the other two -- they're not mean-centered**
        * 14.9 is simple algebra
      * So, two cluster pairs, same variance, same distance.  
        * Which gets merged preferentially by Ward's? **Larger ones since $n_in_j$ grows faster than $n_i + n_j$**
   * Lance-Williams
      * A nice summation of 5 different metrics
      * Try it out for Single Link and Group Average **Get reasonable answers**
      * Also demonstrates that removing $C_i,C_j$ and inserting $C_ij$, where there are n clusters, takes what order of complexity? **O(n) since we need to redo 2n pairs, but each is O(1)**
  * Computation complexity of the entire process
     * Assume we merge all the way to one cluster
     * Why not just O(n) since Alg 14.1 loop runs n times? **Lines 2, 4 and 7 are not O(1)**
     * Complexity for 4? What DS to use? **Min heap gives O(1) for this line**
     * Complexity for 7?  Is it just O(n) per earlier discussion? **No, since each new distance also needs insertion into heap**
     * So, then, heap insertion is $O(nlog(n^2))$ since heap has $O(n^2)$ elements? **No, it's just $O(nlog(n))$ since $O(log(n^2)) = O(n2log(n)) = O(log(n)$**)
     * So, big loop is $O(n^2log(n))$
     * But what about initialization step on 2?**$O(n^2log(n))$ also**
     * OK, but, there is one more independent variable to be considered.  What if we have, for instance, points in a 1,000,000 dimension space? Now what O(1) step becomes O(d) and how does that affect complexity? **Each initial computation, so $O(n^2(d+log(n)))** 
     * Note, not $O(n^2dlog(n))$ which would be worse!
     * Also, does line 7 also need an added d factor? **No, it works off the already-known distances to $C_i, C_j$, which is why Ward-Williams is so useful**
     * So, in the final estimation, which part of this algorithm is the most timeconsuming, but a slight margin? **Initialization! This is not uncommon in algorithm analysis**

* Cluster Validation
  * Like itemset validation in that it's a research lit review.
  * External
    * We know the right clustering; this is about checking algorithms.
    * cluster vs partition.  Partition is "ground truth".
      * |C| = r; |T| = k
      * Can r and k be different? Why? **Clustering algorithm may arrive at wrong count of clusters**
    * Contingency table concept
      * What is sum across rows? **Sizes of C clusters**
      * Across columns? **Sizes of T clusters**
      * Is it symmetric if square? **No. $C_i$ vs 
      * But if it is square? **Then yes, symmetric**
      * Related to ?? **Confusion matrix**
      * Is it principally diagonal, if the classification is good? **Technically no since the order of classes in T and C need not be identical**
    * 17.1 
      * Give intuititive definition.  **Assume highest partition is ground truth that cluster attempts to match.  How high a percent is that?**
      * Max value? **1.0 as weighted sum**
    * Matching.  
      * What does the bipartite graph look like? **C connects to T**
      * Match definition implies what assumption of r and k? **Equality**
      * How many matchings are possible? **r! or k!**
    * 17.3. What meaning? **How much of a partition does a cluster capture?**
    * Entropy and 17.1.2
       * bit count example
    * Cluster-specific -- explain meaning **"surprise" or information content of T samples limited to C**

