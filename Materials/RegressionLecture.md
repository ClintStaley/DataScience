# Regression

## Linear Regression
### Core Concepts
  * Core definition of "regression" -- prediction of single value from multivariate input.
  * Walk lightly through standard derivative presentation.
  * Zaki 23.1.  Why is this a hyperplane? **Plane eq**
  * Zaki 23.4.  Note analogy to MSE error for deep learning.  We can do closed form for simple cases, but regression data is usually larger than that.
### Bivariate Regression
  * Just one-dimensional input, many samples
  * Zaki 23.5
  * Walk lightly through to 23.11, noting this is classic presentation but prefer geometric
  * $\Sigma(x_i - \mu)^2 = \Sigma(x_i^2 - 2x_i\mu + \mu^2) = \Sigma x_i^2 - n\mu^2$ pattern
  * Geometric interpretation
    * Zaki 23.13
       * Be sure we know dimensions of tensors, with n the number of samples
    * Review projection math
      * 23.14 and corresponding diagram
      * 23.15  Tie back to original
### Multivariate Regression
   * Augmented $\tilde{D}$ and brief overview of geometry of homogenous coordinates
   * 23.19
   * 23.20.  
     * Dimensions of $\tilde{D}^T\tilde{D}$? **d+1xd+1**
     * Nature of that matrix?  A covariance? **Uncentered covariance**
   * Can compute $\tilde{w}$ from 23.20.  Order of complexity? **$O(d^2n)$**

### Logistic Regression
  * "Bernoulli" random variable
    * Simplest possible, in a sense.  Skewed coin flip.
    * Can't estimate this with standard regression since output must be bounded probability distribution
  * Logistic function
    * $\theta(x) = \frac{1}{1+e^{-x}}$ General shape and purpose -- "binary" but continuous.
    * Forces unlimited x to be a probability value between 0 and 1
    * Simple derivative -- derive?  **$\frac{d}{dx}(1+e^{-x})^{-1} = -1(1+e^{-x})^{-2}((-e^{-x})) = \frac{e^{-x}}{(1+e^{-x})^{2}}$**
    * Odd function if shifted down 1/2
    * Sees use in neural networks, too
    * Property 24.2: $1-\theta(z) = \theta(-z)$.  Why does this make intuitive sense? **Subtracting from 1 flips the curve around y=.5, which is the same as flipping across z = 0**
    * What does this say regarding the binary pair of values $\theta(z)$ and $\theta(-z)$ for any given z? **Bernoulli distribution totalling 1**
    * Reframe derivative as $\theta(x)\theta(-x)$ **see sheet**
  * Full 24.4 form.
      * How did we come up with this?
      * Why not just first term? **y=0 would set it to 1 constant**
      * OK, why not just multiply instead of power? **y=0 sets it to 0 constant**
      * Why not just add them? Product gives more weight to outliers, kind of like a harmonic mean  
      * How do the two theta values relate to each other?  **They are a probability distribution**
      * So ultimately this is about two probability distributions being matched, in a push-pull fashion
      * It also makes the math of log-likelihood come out elegantly, which is reassurming.
      * And, it really permits a y between 0 and 1.
  * Odds Ratio
    * Focus mostly on the $\frac{\theta(\tilde{w}^T\tilde{x})}{\theta(-\tilde{w}^T\tilde{x})}$ form.
       * Similar push/pull.
       * What is its range? **0 to infinity**
       * Resolve to simpler form as 24.5
    * Take log to get log-odds ratio
       * What is relationship to $\theta()$?  **Inverse, clearly**
    * logit function
       * Note that $\frac{z}{1-z}$ is odds-ratio
       * Prove that $\theta(logit(x)) = x$
       * How does this look?
         * at z = .5? **0** at z = 0? **-infinity**, at z=1? **ditto**
       * Prove it's inverse of logistic function, or $\theta(logit(x)) = x$ **$\frac{1}{1+e^{-ln(\frac{z}{1-z})}} = \frac{1}{1+\frac{1-z}{z}} = \frac{z}{z + 1 - z} = z$
   * Impact of each $x_i$ on odds ratio itself is exponential, conditioned by $w_i$
   * MLE 
     * Follow 24.7 derivation
        * Recall 24.2.
        * Pushes toward negative or positive $w^Tx$ per 1 or 0 y value
        * 24.7 and general idea of "log likelihood" (familiar to the AI2 group)
      * 24.8 Cross entropy!
        * Of what two distributions? $y$ and $\theta(w^Tx)$
        * Categorical distributions on how many outcomes? **two**
        * Isn't it normally a summation? **expanded as $y_i$ and $1-y_i$**
        * Value of CCE in other contexts, e.g. binary neural networks
      * Follow expansion for gradient ascent 
        * 24.9?  **Simple expansion**
        * 24.10? How do we get $\theta(z_i)\theta(-z_i)$? **From earlier derivative discussion**
        * 24.11?  *Why is $\theta(-z) + \theta(z) = 1$?
      * Algorithm 24.1
        * Follow code
           * Why random order on line 6? **Avoids directional clustering**
           * Where are epochs?  What are batches? (For those familiar) **Repeat loop is one epoch per iteration.  Batches are size 1**
        * Discuss SGD and batch processing, learning rates, etc.
      * Fig 24.2 -- Big picture
  * Multiclass logistic regression
     * One-hot representation
        * Can also be a probability vector totalling to 1
     * Eq 24.15
        * What is analog of $\pi_j(\tilde{x})$ in Eq 24.4, and what is the range of j? 
        * Actually doesn't require pure one-hot and more than Eq 24.4 though easier.
     * Developing the $\pi$ function: Eq 24.16
        * Odds-ratio makes a bit more sense now that we have a lot of probabilities
        to compare.
        * Want an odds-ratio behavior like that for binary.
        * Pick one referential: $\pi_K$, the final $\pi$
        * Assuming we have a linear log-odds ratio, we get values for $\pi_i(\tilde{x})$ as given in 24.16
     * Eq 24.17
       * Now use fact that all $\pi$ sum to 1.
       * Follow the development 
         * Why does it make sense that $\tilde{w}_K = 0$ and $e^{\tilde{w}_K^T\tilde{x}} = 1$? **Odds-ratio of K to K is 1 and log-odds must be 0**
       * Softmax!
     * Softmax is what you get if you try to set up a discrete probability with
       given log-odds relationships to a reference class like K.  The log-odds values are the exponents.  
       * Does it allow negative arguments?  **Yes**
       * What happens if you add 1 to *all* arguments? **Nothing**
       * Can I make a different choice of reference, say $\pi_3$?  How do I make it 1 if so? **Subtract necessary value from all to set $\pi_3 = 1$**
     * Note development after Eq 24.17 that shows the same idea.  Difference of
        log-odds-ratios for a pair, both relative to K, is the same as their mutual log odds. 
     * So, back to binary case for a moment.  
       * 24.4 and 24.5...
       * Log-odds ratio between P(Y=1) and P(Y=0) is the same idea...
          * Which is being used as the "K" in 24.5?  **P(Y=0), actually**
       * Is $P(Y = i)$ the same as $\pi_i$ from the multiclass analysis?
          * In this analysis, K = 0, so $w_K = 0; e^{w_K^Tx} = 1$
          * The "w" in 24.5 is whose w? **$w_1$**
          * $\pi_1 = ?$ **$\frac{e^{w^Tx}}{1 + e^{w^Tx}} = \frac{1}{1 + e^{-w^Tx}} = \theta(w^Tx)$
          * $\pi_0 = ?$ **$\frac{1}{1 + e^{w^Tx}} = \theta(-w^Tx)$
          * QED
     * MLE estimation for multivariate
       * Compute $\frac{\partial}{\partial v_a}\pi_j$ for j <> a. **$\frac{\partial}{\partial v_a}e^{v_j}(\Sigma_i e^{v_i})^{-1} = e^{v_j}(-1)(\Sigma_i e^{v_i})^{-2}e^{v_a} = -e^{v_j}(\Sigma_i e^{v_i})^{-1}e^{v_a}(\Sigma_i e^{v_i})^{-1} = -\pi_j \pi_a$
   



   



