# First Day
 * Syllabus review
   * Challenging course
   * Importance of topic
   * Individual work on coding/assignments

 * Self-study methods
   * multiple sources
   * Try CONCRETE EXAMPLES

## Theory Areas (interwoven through course) 

###  Data, patterns, and high-dimensional space
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
 ◦ Bernoulli (or simply binary) variable has 0/1 value.  Can be nominal or ordinal.  
   * Did/did not purchase an item
   * adult/minor
 * Translation of continuous data to points in space
 * Translation of discrete, ordinal data similarly
 * Nominal ("just a name") categorical data results in collection of spaces
 * Vector spaces
        ◦ Hypercube sequence exercise
        ◦ Reasoning about patterns in hyperdimensional space
            ▪ What do "nearby" patterns look like?  
            ▪ What does a midpoint pattern look like?
            ▪ What does a pattern of only binary variables look like?
        ◦ Pattern space reasoning
            ▪ Typical pattern space is BIG
            ▪ Is a midpoint pattern an "interpolation" of the endpoints?
            ▪ Convex vs nonconvex
        ◦ Dot product computation and geometry
        ◦ Defining a hyperplane with perpendicular and distance

Practice
    • Data matrix concept
        ◦ "select" statement
        ◦ Pandas dataframe
        ◦ Spreadsheet
        ◦ ID-ed list of vectors with typed and named dimensions.
    • Itemsets as initial study
        ◦ shopping carts, web pages visited, etc.
        ◦ Items and transactions; Itemsets and Tidsets
        ◦ i(T) and t(X) functions
            ▪ Use text
            ▪ Subsetting relationships: 
                • Itemset A is subset/superset of Itemset B.  Effect on t(A) vs t(B)?
                • Tidset A is subset/superset of Tidset B.  Effect on i(A) vs i(B)?
        ◦ Bruteforce algorithm
        ◦ Itemset lattice
            ▪ Note support will monotonically decrease down the lattice
        ◦ aPriori algorithm
            ▪ By hand for example set



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
      * Is it a probability vector? **No, not across j**
      * Description intuitively? **How do all the data points "like" $C_i$? or How close is each to $C_i$?**
      * Equations leading up to 13.10
      * Eq 13.10.  Discuss.  
        * Ask intuitive meaning.  **How popular is $C_i$?**
        * Equivalent in K-Means? **How many points in the cluster?**
      * Review sample results in 13.4
        * Advantages of this over k-means?  **probabilistic assignment, so
         point categorization can be "gray".  Also size of clusters, in the
         form of the $\Sigma$ value
    * Full example with multivariate normals
      * Translate univariate to multivariate.  What 1x1 matrix for $\Sigma$? **$[\sigma^2], so \Sigma^{-1} = \frac{1}{\sigma^2} and |\Sigma|^{1/2} = \sigma$**
      * EQ 13.11 
         * Assume 100 3-D points.  Dimensions of the matrices are?? **$D^T is 3x100. w_i is 100x1, w_i^T is 1x100, \bm{1} is 100x1$
         * Intuitive interpretation?  **Weighted average of all points by "closeness" to $C_i$**
         * Is this a weighted average with total weight of 1? **Yes, due to denominator**
      * EQ 13.12
         * Dimensions of matrices $\bar{D}_i, \bm{1}, \mu_i^T? **$\bar{D}_i is 100x3, \mu_i^T is 1x3, \bm{1} is 100x1 and \bm{1}\dot\mu_i^T is 100x3$ which is perhaps surprising$ **
         * Outer product concept
            * vertical dot horizontal (transpose)
            * or can be written $u \otimes v$
         * What is center point of $\bar{D}_i$? ** origin **
         * Dimensions of matrices in 13.12 itself and of the product in the numerator? **$\bar{x}_ji is 3x1 so \bar{x}_ji^T is 1 x 3, product is 3x3, w_i^T is 1x100 and \bm{1} is 100x1**
         * So, weighted sum of correlation matrices
         * Analagous to what 1-D equation? **Computation of $\sigma^2$ earlier**
      * EQ 13.13
        * Can $P(C_i) = 0$? **No, always some probability
      * Note that this all is intuitively reasonable, but not *proven* to provide optimal results.  Don't bother with 13.3.3, though it's very interesting math.
      * Algorithm 13.3
        * Line 8 equates to what in the KMeans algorithm?  
        * How does this change if we use a diagonal covariance matrix per the suggested optimization? **Line 11, create diagonal by single loop iteration through $x_j - \mu_i$
      * Complexity
        * Take determinant at face value -- done by GJ elimination for which each of d steps is $O(d^2)$
        * Why is f computation $O(d^2)$? ** multiplication through $\Sigma$ takes $d^2$ steps.**
        * Going with pure diagonal drops $d^2$ not just d.  Why? **Determinant is now just O(d)**
        * What type of situation would make you want to go with just the diagonals? **Large d, so points with many attributes**


