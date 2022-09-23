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
     * How many q-partitions of a k-set are there?
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
     * Powerful way to evaluate an association rule, assuming existing database is itself just a sample space
     * Use Fisher test to determine whether the effect of a generalization is "surprising".
     * Generalize by removing an antecedent subset Z, so X = W|Z
     * Table 2.17
       * If Z doesn't affect Y then columns should be proportionally the same
       * Odds calculation eq 12.13
       * 

