* Bayes
  * Simplest: $p(x|y) = \frac{p(x,y)}{p(y)}$
  * Standard: $p(x|y) = \frac{p(x)p(y|x)}{p(y)}$
  * Inductive: $p(x|y) = p(x)\frac{p(y|x)}{p(y)}$
  * Intuitive: $p(hypothesis|evidence) = p(hypothesis)\frac{p(evidence|hypothesis)}{p(evidence)}$

* Chain Rule for Probability
  * $p(x_1,x_2, ... x_n) = \prod\limits_{k=1}^n{p(x_k|x_1, ... x_{k-1})}$

* Normal
  * Univariate: $\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
  * N-notation: $\mathcal{N}(\mu, \sigma^2)$
  * Multivariate: $\frac{1}{\tau^{\frac{k}{2}}\sqrt{det(\Sigma)}}e^{-\frac{(x-\mu)^T\Sigma^{-1}(x-\mu)}{2}}$

* Binomial
  * ${m\choose k} p^k (1-p)^{m-k}$

* Covariance Matrix
  * $\sigma_{ij} = E((X_i - \mu_i)(X_j - \mu_j))$
  * Example:  $\begin{bmatrix}&&mil&&cost&&perf&&rel\\mil&&100&&1&&-20&&1\\cost&&1&&100&&2&&20\\perf&&-20&&2&&9&&2\\rel&&1&&20&&-2&&4\end{bmatrix}$

  *  $E((X_i-\mu_i)(X_j-\mu_j)) ?= E(X_i-\mu_i)E(X_j-\mu_j)$

  * $\begin{bmatrix}&&mil&&cost&&perf&&rel\\mil&&1&&.01&&-.5&&.05\\cost&&.01&&1&&.067&&1\\perf&&-.5&&.067&&1&&-.33\\rel&&.05&&1&&-.33&&1\end{bmatrix}$

* Sum-of-N-Sample statistics
  * $E(((\sum_1^nx_i)-n\mu)^2) = E((\sum_1^nx_i-\mu)^2)$\
  $ = E(\sum_1^n(x_i-\mu)^2) = E(n(x_i-\mu)^2) = nE((x_i-\mu)^2) = n\sigma^2$
  * Really?  What's with that second step, moving the parentheses inward?  A square of sums isn't the same as a sum of squares..
  * $E((x_1-\mu)+(x_2-\mu)+...+(x_n-\mu))^2 = E((x_1 - \mu)^2 + (x_2-\mu)^2 + ... + (x_n-\mu)^2 + (x_1\mu)(x_2-\mu)$ + *other similarly mixed terms*)
  * So, what is $E(x_i-\mu)(x_j-\mu)$?

* Jensen's inequality
  * For convex f and random variable X: E(f(X)) >= f(E(X))
  * Opposite for concave f
