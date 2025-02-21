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
  * Alg 15.1
     * Read and explain
     * Concept of flood fill
     * Is order of graph search DFS or BFS? **DFS**
     * Error in loop 12-17? **Yes, it doesn't flag already visited**
     * Can cores compete for a border?  If so, who wins? **Yes, highest k**

     -------------REVIEW BELOW -------------------
     
  * DENCLUE algorithm (15.2.2)
      * Concept of hypercube
      * Eq 15.6/.7 
         * Why $h^d$? (hypervolume of hypercube)
         * In 15.7, what if we use $|\bold{z}|$ rather than $|z_j|$? **We get hypersphere not hypercube.**
      * NN density -- brief review
      * eq 15.10
        * What is shape of $\frac{\partial\hat{f}}{\partial\textbf{x}}$?  **Vertical vector of dimension d**
        * How about $\frac{\partial\textbf{z}^T\textbf{z}}{\partial\textbf{x}}$ with x and z vectors?
           * Write the dot product
           * Consider partial wrt $x_1$ as example
           * Remaining terms drop out
           * Summarizing form as $-\textbf{z}\frac{\partial\textbf{z}}{\partial\textbf{x}}$
      * eq 15.11
      * eq 15.12  weighted average of each other point pulling on x
      * Gradient descent/ascent concept
        * 2-D example of gradient descent
        * Refinements (simulated annealing,S momentum for saddles, possible irrelevance of local optima)
      * Alg 15.2
        * A is set of maxima, *not* in the actual dataset
        * R are points attracted to As
      
* Cluster Validation
  * Like itemset validation in that it's a research lit review.  We'll do only part
  * External
    * We know the right clustering; this is about checking algorithms.
    * cluster vs partition.  Partition is "ground truth".
      * |C| = r; |T| = k
    * 17.1  Read and give intuititive definition.  **Assume highest partition is ground truth cluster attempts to match.  How high a percent is that**
    * Matching.  What assumption of r and k is sorta implied? **Equality**
    * 17.3. What meaning? **How much of a partition does a cluster capture?**
    * Entropy and 17.1.2
       * bit count example
    * Cluster-specific -- explain meaning **"surprise" or information content of T samples limited to C**
