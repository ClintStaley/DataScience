# Data Science 1 Lecture Notes

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

* Pandas dataframe

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
 * Translation of continuous data to points in space
 * Translation of discrete, ordinal data similarly
 * Nominal ("just a name") categorical data results in collection of spaces
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
    * $\begin{bmatrix}1&&2&&-1\\2&&1&&2\\0&&-3&&4\end{bmatrix}$
    * What do unit vectors translate to?
    * Do G-J elimination
       * $\begin{bmatrix}1&&0&&.5\\0&&1&&-.75\\0&&0&&0\end{bmatrix}$
    * What is rank, rowspace, colspace? **2, top two rows after G-J, (0, 1, 1.333) and (...)
    * What is determinant?  Why? **0, since rank < 3**>
  * Symmetric matrices (we'll deal a lot with these)
    * $Q^{-1}\Lambda Q$ form
    * Positive semidefinite if all eigenvalues are nonnegative
       * $x^TMx >= 0$ 
      * Dot product of transformed x and x itself is nonnegative
      * What does this say about the "shape"  of the linear transform M? **skews sphere into ellipsoids without inverting or over-rotating**
  * Outer product $P = xx^T$
    * We will use this in probability in form of correlation matrix
    * $Pu$ projects u onto x via dot product, then remultiplies by x
    * Brief example using x = $\begin{bmatrix}1\\3\\-2\end{bmatrix}$ What is $xx^T$? **$\begin{bmatrix}1&&3&&-2\\3&&9&&-6\\-2&&-6&&4\end{bmatrix}$
    * Nullspace? **Orthogonal to x**
    * Laft nullspace? **ditto**
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
    * m tries with p likelihood each.  What are odds of k successes?
    * View as m tries in a row, with k being successful
      * How many different such patterns? $m \choose k$
      * Likelihood of a specific one,  with each outcome exactly as specified...
        * failures (1-p) likely, successes p likely
        * $(1-p)^{m-k}p^k$
        * thus ${m\choose k} p^k (1-p)^{m-k}$
        * Roll a die 7 times, get exactly 3 1's?  **${7 \choose 3} = 35$, each with $0.1666^3 0.8333^4 = .00223$, so .078**
    * Single try is called a Bernoulli distribution, e.g. one roll of a die, so binomial distribution is outcome of m Bernoulli trials.
  * Normal distribution as example of continuous
     * Examine equation $\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
     * General shape, meaning of symbols
     * Symmetrical about ??  **mean**
     * Impact of squared stdev in power denominator? ** Higher stddev results in wider curve, squared means symmetrical
     * What should area under curve be? **1**
     * What happens to area as stdev rises, absent compennsating leading fraction? **Gets too large since same heights, but wider
     * Purpose of leading fraction?  **Normalize to integral of 1**
     * Actual integration is a royal pain, so I won't drag you through it.
     * Why bother with this?
      * What is the Central Limit Theorem?  **Lookup shows it's the limit of sample mean for most actual distributions.
      * Also has maximum entropy (most uncertainty) for any distribution where you specify the mean and variance.  
        * Why not uniform distribution, which normally is most surprising? **Cannot extend infinitely if variance is known**
      * Foundational in many AI algorithms (Naive Bayes estimation, gaussian "splats" for 3-D vision, VAE latent variables, etc.)
      * Generally appears *in multiple dimensions* however
    * $\Nu(\mu, \sigma^2) notation$
    * Standard normal has mean 0 and variance/stdev 1
  * Use of cumulative table (See image)
    * Chance of more than 2 stdevs from mean?  3? 
  * Joint or multivariate distributions
    * Discrete case has already been covered
    * Marginal probablities
    * Conditional probabilities, e.g. P(color|normal), p(red|normal)
| | red | non-red |
|---|---|---|
|normal | .1 | .5 |
|sports | .2 | .2 |
    * Continuous has analogous ideas. f(x,y).  Zaki p 22.
    * How would we do a marginal distribution for, say, x? **Integrate across y for the given x values: $f_X(x) = \int_{-\infty}^{\infty} f(x,y)dy$**
    * What about conditional probability? **Divide to arrive at area of 1: $f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)}$**
    * Independence: $p(x,y) = p(x)p(y)$ 
      * Can $p(x,y) < p(x)p(y)$?  How much less if so?  **p(x,y) can be zero even if p(x) = p(y) = 1$
      * Same question the other way.  Can $p(x,y) > p(x)p(y)$?  How much greater if so?  **$p(x,y) = p(x) = p(y)$ is possible**
 
  * Multivariate normal
    * $\frac{1}{\tau^{\frac{k}{2}}\sqrt{det(\Sigma)}}e^{-\frac{(x-\mu)^T\Sigma^{-1}(x-\mu)}{2}}$
    * $\Sigma$ is *covariance matrix*.
      * positive semidefinite
      * transforms sphere to ellipsoid shape
      * eigenvectors are the axes, eigenvalues the lengths
      * Why *inverse* transformation in exponent? **Reversing the spread back to a sphere**
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
      * Covariance matrix is structured much like outer-product matrix, but does this mean it's rank 1?  Is it just $E(X-\mu)E(X-\mu)^T$? **No, because $E((X_i-\mu_i)(X_j-\mu_j)) <> E(X_i-\mu_i)E(X_j-\mu_j)$ and expectation of product is not product of expectations**
      * Indeed, under what circumstances are those two the same, and what *is* $E(X_i-\mu_i)E(X_j-\mu_j)$? **Independent distributions, and 0**
      * Give an example of a realistic *continuous independent* joint distribution, and describe its covariance matrix. **
  * Related idea of *correlation matrix* normalizes so that $\sigma$ values aren't a factor:
    * Formally, i,j are $\frac{E((X_i-\mu_i)(X_j-\mu_j))}{\sigma_i\sigma_j}$
    * What range of element values does this imply? **-1 to 1 inclusive**
    * Give correlation matrix for prior (repaired) example: ** $\begin{bmatrix}&&mil&&cost&&perf&&rel\\mil&&1&&.01&&-.5&&.05\\cost&&.01&&1&&.067&&1\\perf&&-.5&&.067&&1&&-.33\\rel&&.05&&1&&-.33&&1\end{bmatrix}$

  * Demo a Galton board
    * Given the balls bounce left/right randomly 50/50, what is the actual distribution? **Binomial**
    * But, what curve actually arises from many binomial trials? **normal**

  * Statistical sampling
    * A *statistic* is some numerical measure of a sample of a distribution
      * Can be mathematically identical to measures like mean, variance, but maintain the distinction -- it's on a *sample*, without assuming the underlying distribution.
      * A statistic is its own random variable.  A statistic that is the mean of n samples has its own mean, variance, etc.
    * **Empirical PMF**.  Probability distribution *as determined by the sample*.
      * Imagine you don't even *know* the underlying PMF
      * Is this discrete or continuous, or does it depend on underlying PMF? **Always discrete**
    * Consider the statistic of a sum of n independent samples: $\sum_1^nx_i$
      * What is the mean of such a statistic? **$n\mu$, for obvious intuitive reasons.**
      * Can also be geometrically "seen" as center of mass of the sample points.
    * Expected *variance* of n-sample-sum is more complex.
      * Sum is on average n times a sample size, so do we expect n-squared the variance?  **Not necessarily because samples may work against one another**
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
  * Is n-sample-average variance a fair estimate of actual variance?
    * What if n = 2? 

  * I flip a coin 1,000 times.  What is the chance the total heads is between 490 and 510?
    * What is the distribution involved? **Binomial**
    * stddev of the Bermoulli 1-coin flip is, assuming tail is 0 and head is 1? **$sqrt{0.25} = .5**
    * stddev of a 1000-coin sample-sum? ** $.5\sqrt{1000} = 15.8$
    * What z-score is indicated? **10/15.8 = .63 stddev**
       * Do we need to find this for binomial distr? **No,Use a normal table.**
       * Value is? **.236*2 = .472**

* Practice
  * Data matrix concept
    * "select" statement
    * Pandas dataframe
    * Itemsets as initial study
    * shopping carts, web pages visited, etc.
    * Items and transactions; Itemsets and Tidsets
    * i(T) and t(X) functions
      * Use text
      * Subsetting relationships: 
        * Itemset A is subset/superset of Itemset B.  Effect on t(A) vs t(B)?
        * Tidset A is subset/superset of Tidset B.  Effect on i(A) vs i(B)?
      * Bruteforce algorithm
      * Itemset lattice
        * Note support will monotonically decrease down the lattice
        * aPriori algorithm
          * By hand for example set

# Chapter 1 Fundamentals (in stages)
## 1.3.3 Projection
 * Equation 1.11, with diagram
 * Why divide by |a| twice?
 * Compute for a = (1, 1, 1) b = (1, 2, 3).  **Should get 6/3 = 2. **
    * Significance...  What point does project hit on (1, 1, 1) direction
    * What if reversed a <-> b?  **6/14**
    * Closest point along a of (1,2,3)?  **(2,2,2)**
    * Closest along b of (1,1,1)? **(6/14, 12/14, 18/14)**

## Day 2 --------------------------------

## Prelim test

 * t({C, D}) =?
 * i({2,4}) = ?
 * t(0) = ?
 * How many yotta-atoms in a mole?  ($6 * 10^{23}$)

## Example 8.3

 * Possible for item in $F^(3)$ to not be prefix of some item in $F^(2)$?

## Association Rules

 * Compute $sup(AB \rightarrow D)$  **Answer: 3**
 * Compute $conf(AB \rightarrow D)$  **Answer: 3/4 = .75**
 * Can conf(X->Y) be greater than 1.0?  Why or why not?

## Brute Force Algorithm
 * Walk through and expalin each step
 * Consider complexity
 * How to improve?  What order would you explore the itemsets?  Why?  Can we trim?
   * This is how you should do reading: question and anticipate
 * Look at lattice
   * How does sup change as you move down?

## Apriori
 * Walk through ComputeSupport for sample itemsets
   * Why is this better?
 * Walk through 
   * Reframe line 19 a bit.  "if for all $X_j \subset X_{ab}...$"
   * What is sup value for eleements of $C^{(k)}$ at start of call?
 * Pick a homework problem or two to analyze

## Python Lab
 * Get Pandas and Numpy installed
 * Pull down zip file
 * Do a Pandas read-in of Orders100.csv and try out a bit of Pandas

## Day 3 ------------------------------------

## Eclat / dEclat (assumes reading and Q/A)
 * Quiz (use our sample database):
     * Find a 3-itemset X for which d(X) = $\emptyset$
     * What is the largest $|d(X)|$ possible in our sample database? Why?

  * Discuss book suggestion of starting with Eclat or t(X) values and shifting to d(X)
    * Would this be useful with our sample database?
    * What about a typical shopping database?
    * Why go to d(X) at 2-itemsets?  Might t(X) still be smaller than d(X) that early?
    * Is it *even possible* for t(X) to be smaller than d(X) if $|X| \geq 2$? 
  
## FPGrowth
 * FP Tree
   * Compact version of the entire database and supports; used in place of it
   * Build FP-tree from ACE BCE BCD CE
   * Do the same with order ABCDE, just to show less efficient version
   * Can support increase as we descend? (No)
   * Can we generate all subsets as paths in tree?  (No)
 * Generating subsets from FPTree
   * Start with 1-itemsets, then 2-itemsets, etc.
   * Easy degenerate FPTree case
     * Do actual exercise on AC A ACE ACED ACE
     * Generate 1-itemsets, 2-itemsets, etc reading right off the tree
     * Use least-supported (lowest) node as support for each itemset
     * Actually generate the 16 possibles from this example
     * They come up with alternate example using 4 items and try it.
 * General FPTree case
  * Subsets spread across multiple paths.
  * Try to reduce to degenerate case.
  * Generate "projected" (filtered or collapsed) FP trees for each item.
    * Effectively dividing the database into A,B,C,D... groups
    * Easy to do from leaf values.  
    * Can least-supported elements ever have children in the FP-tree?
    * Can we do a subtree *assuming D is in the itemsets*?
      * Count support by scanning tree
      * Rehang the paths to create subtree for patterns 
    * Now remove the D leaves, and we're left with the same solution for
      C patterns minus any D patterns
    * Do the same for C, A, etc.
    * How do we understand B?
      * Will it ever appear a lower than top level?
      * Is it the *only* top level element?
      * What does the prefix tree of "itemsets with B, and no other elements" look like?
 * Pseudocode in Algorithm 8.5
   * Will line 1 remove internal nodes?  What happens if so? **No.  Any infrequent item has only other infrequents as descendants**
   * What about line 13 -- just from root to node? What if interior? **Effective removal of less-supported leaves is OK since they're already covered under other trees.
   * Finish up recursive call for D, then generate sets.
 * Another example 

## Generating Association Rules
 * Independent of algorithm.
 * If we know ABCD is a frequent itemset, what rules can we deduce?
    * AB -> CD for instance?  What confidence that this is so?
    * What might it take for AB -> CD to be very lightly supported?  Very heavily?
 * Equation 8.7
 * What might it take for all inferences to be low confidence?
 * Algorithm 8.6
    * What type of thing is X?  (itemset)
    * Why choose maximal on line 4?

# Chapter 9 Representing Itemsets

## Maximal Itemsets
  * Intro concept
  * Different "directions" of expansion
  * Maximal means we can't add an element without losing a transaction and dropping below min support
  * Could we possibly add an element and both gain/lose one transaction to "hold even"?

## Closed itemset
  * Idea of closure of X: i(t(X))
  * What effect does closure operation have on support? (None)
  * 9.3 in English? (Can't add an item without losing a transaction.)
  * Ask: isn't a closure the same as a maximal? (No, could be at a higher level of support than minsup.)
  * 9.4
    * Can maximal itemset be expanded by closure? (No, so M $\subseteq$ C)
    * Is closed itemset automatically maximal? (No)

## Min Generator
  * English meaning of 9.5?  ("Can't lose an item without gaining a transaction")
  * Unique min-generator to maximal subset pairing? (No, can lose different items without gaining transactions)
  * Consider ABCD, ABC, ACD,

## Fig 9.2

# Sequence Mining

## Basics
 * Sequence, subsequence, and substring
 * Fig 10.0
    * What is different about this tree vs the itemsets lattice?
 * Support concepts
    * Definition of support
    * Explain a few of the nodes in the tree
    * SAuper/sub *sequences* not subsets
    * Still monotonic?  Why/why not?  **subseq has to also be supported same.  superseq can't be more.** 
 * Trace standard apriori style algorithm, DFS on the tree
    * Note similarities to Apriori
    * Why children(parent) on 17, and no a<b?  **symbols, including self, are repeatable.**
    * Trace tree development briefly
 * Spade algorithm
    * Concept of final-symbol potential locations
    * Trace logic of 10.4 tree, for a few.  Then have them trace the rest.
    * Algorithm 10.2: 
       * What is definition of intersection on line 6?
       * What is the algorithm analagous to?


## GSP Algorithm
 * What the heck does this, in 10.2.1, mean: "It uses the antimonotonic property of support toprune c andidate patterns, that is, no supersequence of an infrequent sequence can be frequent, and all subsequences of a frequent sequence must be frequent."
 * 

## Suffix trees
 * Review basic suffix tree idea.  
   * Do exercises, adding new strings
   * Efficiencies
      * Substring ranges on branches
      * Track support
   * Use for finding substrings
   * Trie, Patricia tree or radix tree
   * Why suffix and not prefix?  **forward seeking requires suffix mode**
   * Order of complexity for string hunt -- clear choice at each node
 * Building one fast.  Ukkonen's.  
   * (Sample patterns  CAGAAGT TGACAG, abcabxabcd, abracadabra)
   * Build by extension
   * Try simple case like abcd -- all explicit suffixes
   * ABCABCD implicit suffixes
     * How do we find the "fallback location"? **Simple search if off of root**
   * Try ABCABXABCD
     * Need skip into fallback prefix
   * Run example
     * How to get second level of suffix links to be used? ABCABXABCDABCX


## Evaluating Itemsets
 * Well-supported itemsets aren't the final result
   * Lots of them.  Still a "data science" job to cull them
   * Some are less meaningful, e.g. {milk, eggs, bread}
   * Rich set of quantitative measures for evaluating itemsets and association rules, clearly from many research papers
     * Understand all in order to reason well about this, and to deepen probability thinking
     * Confidence and lift are most common in my limited experience, especially lift

 * First look at Association Rules more closely
   * Is confidence a sufficient indicator?
      * Example of Lox -> Bagel 40% confidence vs Lox -> Milk 40%
      * Even highly confident rule can indicate *reverse* causation.
   * Lift concept
      * EQ 12.4
      * Advantages
      * Takes background likelihood into account.  
      * If Bagel is .05 likely, lox .03 and milk .5, what are the lifts of our bagel/lox/milk example?
         * Lox -> Bagel **.4 / .05 = 8
         * Lox -> Milk **.4 / .5 = .08
      * Can be high or low (above or less than 1.0)
         * Arrive at a lift of 10?  **probs of .1 can arrive at lift of 10**
         * How about low lift?  How low can it go? **0 for any completely disjoint X and Y**
      * Disadvantages
      * Show how a rare pair of events can result in lift of 1000?  **Both .001 likely, but 100% correlated**
      * Symmetrical.  Why is this bad?  **No causality info**

   * Leverage concept
      * Looks to me like this is just lift - 1.0, or "differential lift".  Is this so? **No, because it's lift-1.0 times rsup(X)*rsup(Y)**
      * So, like lift, but differential, and magnified by joint support (support of itemset XY).
      * What is max leverage possible?  How obtained?  **Can't exceed 1.0 due to probs, but worse than that.  X and Y = 1/2 and fully correlated gets leverage of .25**
      * How about min leverage?  **Fully uncorrelated with .5 prob for X and Y gets -.25**
      * What is leverage like with light data (low probs), such as high-lift rare case earlier?  ** Tends to near zero.  Fully correlated with .001 -> .00999.  Uncorrelated -.000001 **

   * Jaccard
      * What share of the Venn diagram is the rule?
      * Symmetric
      * Sensitive to low prob values.

   * Conviction 
      * Conviction takes into account how likely rule is to *fail*, in particular X -> !Y$
      * Lift of this measure is bad if larger, so invert to 1 / lift(x -> !y)
      * Assymetrical
      * How to make high?  How high can it go?

   * Odds ratio
      * "Odds" concept.  Alternate way to state relative probability, intuitively considering the "not" case also.
        * Mathematically p/(1-p) ratio, e.g. .75 probability is 3:1 odds.  (Usually state with 1 in "denominator")
        * They do 5:1 odds is what probability **.8333**.  .9 probabililty is what odds? **9:1**
        * Vs probability, has what range?  **0 to infinity**
      * Ratio of chance of Y with and without X.
        * Significance of 1?
        * How to get 0 even if X -> Y is supported? **If Y is always there anyway**
        * Example 12.8
   
   
 * Evaluating entire pattern or itemset
   * Total lift eq 12.9
     * (Product notation)
     * Make lift of an itemset be 1 even if its support is 100% **All items are 100%**
   * Need to consider lift or other measures for *all rules derived*
     * Q-partition and 12.10
     * Revise the min notation
   * Max, min, or average may be used.
     * Table 12.14
     * Discuss which is more important (min, max, ave) and why
       * Min susses out "duh" cases if these are fully explanatory
       * Max finds significance
   * "Productive" itemsets
     * Productive itemset if *all* A->B rules have lift > 1, or $lift_2(X) > 1.0$
 * Productive association rules
  * Idea of "more general" -- reduce antcedent by at least one member
  * Productive association cannot be made more general without loss of confidence
    * Why confidence instead of support? **More general cannot reduce support, only increase it**
    * Example of more general rule with less confidence?  **buns and dogs -> mustard vs dogs -> mustard if dogs are very common**
    * Concept of "improvement": 12.12.
  * Fisher Exact Test
    * Hypergeometric distribution.  
     * Pick X people from a N-person pool of known C1 and C2 categories e.g. studiers/nonstudiers, what is chance of Y C1s and X-Y C2s?
     * Universe of possible X-person choices $N \choose X$
     * Most won't have X C1s.  How many will?  
     * Gotta choose Y from C1, so $C1 \choose Y$.  But, there are also
         many ways to choose the X-Y C2s, so also $C2 \choose {X-Y}$
     * ratio is likelihood of X C1s from N.  $\frac{{C1 \choose Y}{C2 \choose {X-Y}}}{N \choose X}$
  * OK, now consider a second division of the N items into groups, say men/women. 
     * Four-way table: categories (significant or not?) plus C1 and C2, generally termed "success" and "failure"
     * Women/men studier/nonstudier example
     * Question is whether second division has an impact on first.
       * Null hypothesis is "no", but is this believable based on the data?
       * Can get C1, C2 and N from the table/sample: C1 = a+b, C2 = c+d, N = a+b+c+d  Also X = a + c or b + dfrom a column.
       * What is chance of X?  If under, say P-value of .01, then we reject null hypothesis.
       * Do the math for column 1.
       * They expand to simple fraction model.
       * They do the math for column 2 and show it's the same!
       * Do exercise with a, b, c, d = 3, 12, 9, 8 **Likelihood of .049, rejecting null hypothesis at P-value .05**
     * But, is this a complete picture? It gives likelihood of *exactly* 3 male studiers, but treats more extreme cases (2 studiers?) as part of the 95.1% other possibilities.
       * What are "more extreme cases"? Bit of an open question, but a reasonable measure maintains both category counts.
       * Lower our example to two male studiers while maintaining row/col totals? **2, 13, 10, 7**
       * (Can you do that as a simple change from the earlier case?) **Yes, multiply by 3*8/13*10**
       * And again for 1?
       * How does null hypothesis look now?
     * What about the other way?  Does success/failure have an effect on men/women?
       * Intuitively should work both ways, with a being equally unlikely from either perspective
       * Do the math to show this is so.  **Left as homework**
  * Powerful way to evaluate an association rule, assuming existing database is itself just a sample space
    * Use Fisher test to determine whether the effect of a generalization is "surprising".
    * Generalize by removing an antecedent subset Z, so X = W|Z
    * Table 2.17
      * Null hypothesis: Z has no impact on Y.  Rows don't matter.
      * Or equivalently, and somewhat more subtly, can't tell whether Z was in antecedent or not based just on Y vs notY.  (Can't determine whether studier or not based on man or woman)
      * Explore odds calculation eq 12.13
         * Note that it's symmetrical wrt rows/cols, as expected
         * Explore counterexamples to convince all that this is so.   
         * Follow through with Fisher test 12.14
         * Summation in 12.15

## Clustering
* Section 13.1 KMeans
  * Review basic idea
  * 13.1 algorithm. 
     * argmin meaning
     * Why squared norms? **Same comparison, no sqrt needed**
  * Convex nature of regions
     * Remind of limits on convexity, e.g. for MNist data
* Section 13.3
  * Positive definite matrix review
     * Symmetric
     * Factorable as $QDQ^T$ with Q orthonormal and D pure diagonal
     * All diagonals positive
     * Visual picture: rotate from arbitrary ortho axes to X,Y,Z, then scale, then rotate back.
     * Orthogonal scaling with arbitrary axis alignment.
     * Create one: Scale by 2 along (1, 1, 1), by 3 along (1, -.5, -.5) and by
     4 along (0, 1, -1)
     ```
     Orthonormals are (.577, .577, .577)  (.816, -.408, -.408) (0, .707, -.707)
     Use Wolfram or equiv to multiple all together
     ```
  * Determinant review
    * Volume of transformed unit cube
    * What would we expect for our just-computed matrix? **2*3*4 = 24 Check WA**
  
  * Review multivariate normal 13.6
    * Picture of multivariate
    * Correlation matrix -- sum of corresponding products, thus symmetric
    * Will be positive definite as well.
    * Why do the *inverse*?  Reason out the transform
    * Compare to univariate normal.  (section 13.3.1 p345 has one)
       * Where is $\sigma$?
       * Try 1x1 $\Sigma$
       * What 1x1 matrix for $\Sigma$? **$[\sigma^2], so \Sigma^{-1} = \frac{1}{\sigma^2} and |\Sigma|^{1/2} = \sigma$**
       * Note squared is needed
       * Tie back to full $\Sigma$ being a squared $QDDQ^T$, since of course it's squared sums.
       * Why $\sqrt{|\Sigma|}$ in denominator?

  * Now do EM Clustering
    * Cluster centers turn to normal distributions
    * Weighted by probability
    * MLE and eq 13.7 and 13.8
    * Eq 13.7 Discuss, then ask for intuitive description.  **How well do the present clusters predict x?"
    * Eq 13.8 Discuss and ask for intuition.  **How well do the present clusters predict all of D? (log)**
    * Eq 13.9.Discuss and ask. **How likely is it that $C_i predicted x_j$? or How much does $x_j$ "like" $C_i$?
    * 1-D example (simpler since $\Sigma$ is scalar $\sigma$)  
      * w vector (horizontal!)
      * What would equivalent be in K-means? **0/1 vector**
      * Description intuitively? **How do all the data points "like" $C_i$? or How close is each to $C_i$?**
      * Is it a probability vector? **No, not across j**
      * Equations leading up to 13.10
      * Eq 13.10.  Discuss.  
        * Ask intuitive meaning.  **How popular is $C_i$?**
        * Equivalent in K-Means? **How many points in the cluster?**
      * Review sample results in 13.4
        * Advantages of this over k-means?  **probabilistic assignment, so
         point categorization can be "gray".  Also size of clusters, in the
         form of the $\Sigma$ value
    * Full example with multivariate normals
      
      * EQ 13.11 
         * Assume 100 3-D points.  Dimensions of the matrices are?? **$D^T is 3x100. w_i is 100x1, w_i^T is 1x100, \bm{1} is 100x1$
         * Intuitive interpretation?  **Weighted average of all points by "closeness" to $C_i$**
         * Is this a weighted average with total weight of 1? **Yes, due to denominator**
      * EQ 13.12
         * Dimensions of matrices $\bar{D}_i, \bm{1}, \mu_i^T$? **$\bar{D}_i is 100x3, \mu_i^T is 1x3, \bm{1} is 100x1 and \bm{1}\dot\mu_i^T is 100x3$ which is perhaps surprising$**
         * Outer product concept
            * vertical dot horizontal (transpose)
            * or can be written $u \otimes v$
         * What is center point of $\bar{D}_i$? ** origin **
         * Dimensions of matrices in 13.12 itself and of the product in the numerator? **$\bar{X}_ji is 3x1 so \bar{x}_ji^T is 1 x 3, product is 3x3, w_i^T is 1x100 and \bm{1} is 100x1$**
         * So, weighted sum of correlation matrices
         * Analagous to what 1-D equation? **Computation of $\sigma^2$ earlier**
      * EQ 13.13
        * Can $P(C_i) = 0$? **No, always some probability**
      * Note that this all is intuitively reasonable, but not *proven* to provide optimal results.  Don't bother with 13.3.3, though it's very interesting math.
      * Algorithm 13.3
        * Line 8 equates to what in the KMeans algorithm?  
        * How does this change if we use a diagonal covariance matrix per the suggested optimization? **Line 11, create diagonal by single loop iteration through $x_j - \mu_i$**
      * Complexity
        * Take determinant at face value -- done by GJ elimination for which each of d steps is $O(d^2)$
        * Why is f computation $O(d^2)$? ** multiplication through $\Sigma$ takes $d^2$ steps.**
        * Going with pure diagonal drops $d^2$ not just d.  Why? **Determinant is now just O(d)**
        * What type of situation would make you want to go with just the diagonals? **Large d, so points with many attributes**

* Density clustering
  * Fig 15.1 and 15.2.  Concept of core, border, and noise
    * Can all points in a core neighborhood be border? ** Sure if all are on edge**
    * Can none be order? **Yes if in the middle of core density area**
  * Density-reachability.  
    * Why nonsymmetric?  **x need not be core point**
    * Symmetric if all points are core? **Yes**
  * Alg 15.1
     * Read and explain
     * Concept of flood fill
     * Is order of graph search DFS or BFS? **DFS**
     * Error in loop 12-17? **Yes, it doesn't flag already visited**
     * Can cores compete for a border?  If so, who wins? **Yes, highest k**
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

## Fun with numpy
  * ??

## Linear Discriminants
  * Review projection concept (first eq in ch20)
  * Fig 20.1
    * Note that only w orientation is relevant.  Try moving W to origin.  Changes nothing.
    * $\bar{D}$ is assumed in much of this
  * mean of projection is projection of mean
  * Try exercise where means are aligned on w = [.707, .707] but serious overlap occurs.
  * Scatter concept
     * Why not divide by n?  **Allows more populated classes to dominate, like P(C) in EM clustering**
  * Eq 20.2 pattern
    * Note that $x^Ty = y^Tx$ iff x and y are one-dimensional
    * Allows reorganization to concentrate all the unprojected space coefficients into one matrix
    * Thus, squared *projected* vector equals $w^T\Sigma w$ where $\Sigma$ is correlation matrix in unprojected space.
    * Same pattern for total scatter (squared variance)
    * Better form for doing derivatives, next..
  * Eq 20.8: 
  * Why is $\frac{d}{dx} w^TBw == 2Bw$?
     * Conrete example with $B = \begin{bmatrix}a&&b\\c&&d\end{bmatrix}$
     * $w^TBw = ax_1^2 + bx_1x_2 + cx_1x_2 + dx_2^2$
     * $\frac{d}{dw}w^TBw = \begin{bmatrix}\frac{d(w^TBw)}{dx_1}\\\frac{d(w^TBw)}{dx_2}\end{bmatrix}
     = \begin{bmatrix}2ax_1 + bx_2 + cx_2\\bx_1 + cx_1 + 2dx_2\end{bmatrix}
     = 2\begin{bmatrix}ax_1 + bx_2\\cx_1 + dx_2\end{bmatrix}$ iff b = c
  * Follow eigenvector math
  * Follow alg 20.1
  * Use eq 20.10 with C1 = (6, 1), (1, 0), (1, 2) and (-4, 1), and C2 = -C1
    * What are means? **(1, 1) and (-1, -1)**
    * How well does $w = \mu_1 - \mu_2$ separate?  **So-so. extreme points overlap**
    * What is S? **Same for each** $\begin{bmatrix}50&&0\\0&&2\end{bmatrix}$
    * What is $(S_1+S_2)^-1$? $\begin{bmatrix}.01&&0\\0&&.25\end{bmatrix}$
    * What is adjusted w? $\begin{bmatrix}.01&&0\\0&&.25\end{bmatrix}\begin{bmatrix}2\\2\end{bmatrix} = \begin{bmatrix}.02\\.5\end{bmatrix}$, almost a perfect vertical
    * How is separation now? **Great, even extremes are well separated**
  * Intuition
    * S is the transform that "spreads" the two clusters (weight-averaged over both)
    * $S^{-1}$ is the transform that pulls them back to circular/hyperspherical shape
    * What is B?
      * Is it nonsingular or singular? **Singular**
      * To what space does it map vectors? $\mu_1 - \mu_2$
      * So, it represents a mapping to the $\mu$-difference vector.  
    * $S^{-1}B$ 

## PCA
  * U basis concept, Fig 7.1
  * Eq 7.3 as dot product projections into U
  * Truncated projection, eq 7.5.  If d = 4 and r = 3, what does $x^r$ look like?
  * Eq 7.7 What is $|U_rU_r^T|$ ?  **0, if r < d**
  * Why is $P_r^2 = P_r$? **Reprojecting onto the same subspace changes nothing**
  * Eq 7.9 Why are x' and $\epsilon$ orthogonal?  epsilon is in $S_{d-r}$
  * Vocab: orthogonal complemen
  * PCA -- Project onto most varied dimensions.  (Fig 7.1 again)
    * Speculate: what direction would produce most variety, given positive definite matrix? **Highest eigenvalue**
    * Vocab: first principal component
  * Eq 7.11 -- familiar pattern?  (scatter matrix concept again)
    * State the idea?  **squared length of a projected point set, as a function of projection axis or vector u, is $u^T\Sigma u$ where $\Sigma$ is a correlation matrix.
  * Eq 7.12 Langrangian... Hmmm...
     * $\alpha$ is constant.  
     * What if we omit it?  **Max will simply run u up to large value; alpha discourages this** 
     * What is effect of including it, especially in u-neighborhoods where $u^T\Sigma u$ is at a max? **"Dents" the curve to encourage staying near point where u is unit length**
  * 7.13 Trace derivatives.
     * Recall $u^T\Sigma u$ derivative?
     * Does followon analysis reach conclusion that there is one max? **No, it only says that maxima are at eigenvalues*
     * So we're right about eigenvalues
  * Follow math on the MSE
     * Vocab: trace
     
     
























