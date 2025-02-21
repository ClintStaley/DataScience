# ItemSets

## Itemsets
  * shopping carts, web pages visited, etc.
  * Items and transactions; Itemsets and Tidsets
  * i(T) and t(X) functions
    * Use text definitions
    * Subsetting relationships: 
        * Itemset A is subset/superset of Itemset B.  Effect on t(A) vs t(B)?
        * Tidset A is subset/superset of Tidset B.  Effect on i(A) vs i(B)?

## Example 8.3
 * Possible for item in $F^{(3)}$ to not be prefix of some item in $F^{(2)}$? *No*

## Association Rules
 * Compute $sup(AB \rightarrow D)$  **Answer: 3**
 * Compute $conf(AB \rightarrow D)$  **Answer: 3/4 = .75**
 * Can conf(X->Y) be greater than 1.0?  Why or why not?

## Example problem to consider
 * |I| = 10,000: 10,000 distinct items
 * |D| = 1,000,000,000 transactions of average 5 items, but 1% (10,000,000) have 100 items
 * What is average $sup(x_i)$ for single item? **(5,000,000,000 + 95*10,000,000)/10,000 = 5,950,000,000/10,000 = 595,000**  
 * With relative minsup = .01, what is absolute minsup, then?\
  **10,000,000**

## Brute Force Algorithm
 * Walk through and explain each step
 * Compute complexity
    * Iterations of loop 8? **|D|**
    * Line 9? (Assume both sets are ordered by item) **|i(t)|, not |I|**
    * So, around 5,950,000,000 steps in ComputeSupport
    * And, number of iterations for line 2? **$2^{|I|}$ possible, and $2^{100}$ in our example.  Hmm...**
    * Plus, DB scan for each candidate set.  DBs can be large enough to need out-of-memory I/O
       * Our D is how big? **Assuming two bytes/item just under 12G.  Fits in memory -- maybe.**
 * How to improve?  What order would you explore the itemsets: big to small? Small to big? Item order? Can we trim?
   * This is how you should do reading: question and anticipate
 * Look at lattice
   * How does sup change as you move down?
   * What are definitions of partial order and DAG? **Should know from prior courses**
   * Lattice adds to partial order an "up and down convergence", roughly speaking.  Up/down bounds of empty set and full set make this DAG a lattice.

## Apriori
 * Walk through ComputeSupport for sample itemsets
   * Why is this better?
   * Note ComputeSupport works "in reverse", generating all k-subsets of each i(t).
    * Would it be faster to go through each $c\in C^{(k)}$?  **Probably not, since we can arrange $C^{(k)}$ by prefix order for faster hunt.**
  * ExtendPrefixTree
    * What are b and a in line 17? **Sequence left to right, or if you like, first differing letter after common prefix**
    * What does line 18 really do? How much larger is $X_{ab}$ than $X_a$ or $X_b$? **Adds next letter to $X_a$, by merge with $X_b$, to get to next tree level.**
    * Reframe line 19 a bit.  "if for all $X_j \subset X_{ab}$ such that $|X_j| = k$, $X_j \in C^{(k)}$ then add $X_{ab}$" Why? **This tests for k-sized subsets of the new $X_{ab}$ that are infrequent.**
      * What happens if we omit this test? **Still finds inadequate support, but with another D traverse in ComputeSupport.  The test uses our existing knowledge of $C^{(k)}$ to cull new elements of $C^{(k+1)}$
      * Name one node in Fig 8.3 that is culled by this test. Needs to be a node that has non-culled ancestors, but a culled subset. **ONLY BCD on level 3 -- all other dotted circles are due to culled ancestors**
    * What is lowest sup value for all elements of $C^{(k)}$ at start of ExtendPrefixTree? **All have at least minsup or would have been trimmed**
    * Why the final removal of non-productive leaves *and their ancestors*? **Want to keep only leaves that are possibly productive, and only at the current "k" level.**
  * Does $C^({k})$ contain only leaf nodes? **No, it keeps all parents of current leaves. Culling is only by the final lines of the code.**
  * "a priori" - "having to do with what came before".  Why does this relate to algorithm? **Considers support of smaller subsets that build into current one**
  * Run time?
    * ComputeSupport
      * Database scan reduction, since we do it once per level
      * Subset computation on line 14?  Always a worry to do subset scans..
        * But only for k-subsets, not all... How bad can this get?
        * **Consider |i(t)| = 100 and k = 10? ${100 \choose 10} = 1.7x10^{13}$ -- 17 trillion**
        * So what kind of itemset data will make this algorithm very slow? **Large i(t) values, and even modestly large k-sets**
        * Could we fix this?  **Possibly, by doing foreach( $X \in C^k$) instead...**
        * But how big might even $c^{10}$ be?  **10,000*9,999*...9,901 = $10^{40}$ if none are culled.**

    * Line 14? **$2^{|i(t)|}$ for 5 items, 32 but for 100 items $2^{100}$**
      * Better have fairly small transactions
    * Line 13 is clearly O(|D|), so multiply all this by 1 billion
    * Other lines are harder to count, but how many times will we add a set on lines 18-20?
      * Is this the number of sets $2^{|I|}$ Why or why not? **No, it's vastly less because we drop off sets as support wanes, moving down tree.**
    * And how expensive is the subset-scan on line 19?
      **Candidate sets can't be supported if larger than largest tidsets, but still could be that $2^{100}$ we were hit by earlier.**
  * So, much better than brute force, but still a problem for what cases?
    * **large |D|**
    * **above all large |i(t)| with low minsup**

## Eclat/DEclat
  * Maintenance of explicit support lists
    * No need to rescan D
    * Follow tree in book and Eclat code
  * How does this improve on APriori?
    * No multiple passes through D
    * No powerset operations
  * How is it weaker than APriori?
    * Whopping large support lists and intersection ops.
  * Tid-difference concept
    * Definition of set subtraction as $A \backslash B (sometimes A-B) = A \cap \bar{B}$ or A minus anything that was in B.
    * Why does it make *sense* that $d(X_a) = t(X) \backslash t(X_a)$? **Because what we lose in support by including $X_a$ is what was in X's support but not in $X_a$'s support.**
   
  * Quiz (use our sample database):
    * Say for an itemset ABC, d(X) = $\emptyset$.  What does this say about the relevant transactions? **Any transaction that includes AB also includes C**
    * What is the largest $∣d(X)|$ possible in our sample database? Why? **10,000,000 if item is in no transactions**
  * Discuss book suggestion of starting with t(X) values and shifting to d(X)
    * Would this be useful with our sample database? **Yes.  Initial support per-item averages 5300 transactions**
    * What about a typical shopping database? **Even more so given smaller carts and larger inventory**
    * Why go to d(X) at 2-itemsets? Might t(X) still be smaller than d(X) that early? **Sure, if we lost more than half the support of the 1-itemsets when adding second items**
    * Do we have to make the t(x) -> d(x) shift at the same level across the tree? **No, each branch gets a separate recursive call**
    * Broadly, when is dEclat preferred?  **With lots of large transactions and slow reduction of support downtree**

## FPGrowth
 * Building the FPTree
   * Compact version of the entire database and supports; used in place of it
   * Build FP-tree from ACE BCE BCD CE
   * Note the "layers" in DCAEB order from bottom to top.
   * Could maintain linked lists through those layers
   * Do the same with order ABCDE, just to show less efficient version
   * Can support increase as we descend? **No**
   * Can we generate all subsets as paths in tree? **No**
 * Generating subsets from FPTree
   * Start with 1-itemsets, then 2-itemsets, etc.
   * Easy degenerate FPTree case
     * Do actual exercise on AC A ACE ACED ACE
       * **Should end with degenerate A(5)->C(4)->E(3)->D(2)
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
    * Can least-supported elements ever have children in the FP-tree? Why/Whynot? **No, since they are always last added in paths.**
    * Can we do a subtree *assuming D is in the itemsets*?
      * Count support by scanning tree
      * Rehang the paths to create subtree for patterns 
    * Now remove the D leaves, and we're left with the same solution for
      C patterns minus any D patterns
    * Do the same for C assuming no D at all
      * Ditto for A assuming no C or D, etc.
    * For each such generated tree, track assumed prefix, and do recursion.
    * How do we understand B?
      * Will it ever appear a lower than top level? **No, even as we generate subcases**
      * What does the prefix tree of "itemsets with B, and no other elements" look like? **Just B itself, with its support**
 * Pseudocode in Algorithm 8.5
   * Will line 1 remove frequent nodes that are children of infrequent? **No.  Any infrequent item has only other infrequents as descendants**
   * What is X for on lines 9 and 16? **Prefix of subcall**
   * Does subset operation on line 3 include emptyset? **No, because already handled on line 11**
   * Finish up recursive call for D, then generate sets.
 * Another example

## Generating Association Rules
 * Independent of algorithm
  * how we use frequent itemsets to deduce causality
 * If we know ABCD is a frequent itemset, what rules can we deduce?
  * AB -> CD for instance?  Can we assume that AB in an item set often or always means CD will also be there?
    * Support for such a rule?  How often have we seen it happen? **Support for ABCD**
    * Reality check: Do we also need support for, say, ABCDEF? **No, sup(ABCDEF) <= sup(ABCD)**
    * *Confidence* c for such a rule?  How often is it followed vs broken?
      * Ratio of ABCD cases to all AB classes
      * Zaki eq 8.7
    * How might we get:
      * sup(AB -> CD) = 100, c(AB -> CD) = .1 **100 ABCDs and 9,900 AB with only C or D at most**
      * sup(AB -> CD) = 4, c(AB -> CD) = .9 (trick question)? **Can't.  Lowest non-1 confidence would be .8** 
 * ABCD also supports other association rules, e.g. A -> BCD, CD -> AB, etc.
  * How many, assuming n items in the set and at least one item on each side of the ->? **powerset for LHS, minus full and empty sets, so $2^n - 2$**
  * How do c(B->ACD), c(AB->CD) and c(ABD->C) relate? **Monotonically higher, since supports of left hand sides monotonically decrease**
  * What is the minimum requirement for all association rules to be < 50% confidence if sup(Z) = 100?
    * Need at least n*101 itemsets each missing just one of the items from Z.
 * Algorithm 8.6
    * Why |Z| >= 2 on line 1? **Need a left and right side**
    * Why choose maximal on line 4? **Reasons just explored.  Subsets will be dropped if superset lacks confidence.  Aim high**

# Chapter 9 Representing Itemsets
## Maximal Itemsets
  * Intro concept
  * Different "directions" of expansion
  * Maximal means we can't add an element without losing a transaction and dropping below min support
  * Could we possibly add an element and both gain/lose one transaction to "hold even"? **No.  Gain by adding an element is impossible**

## Closed itemset
  * Idea of closure of X: i(t(X))
  * What effect does closure operation have on support? **None**
  * 9.3 in English? **Can't add an item without losing a transaction.**
  * Ask: isn't a closure the same as a maximal? **No, could be at a higher level of support than minsup.**
  * 9.4
    * Can maximal itemset be expanded by closure? **No, so M $\subseteq$ C**
    * Is closed itemset automatically maximal? **No**

## Min Generator
  * English meaning of 9.5?  **"Can't lose an item without gaining a transaction"**
  * Unique min-generator to maximal subset pairing? **No, can lose different items without gaining transactions**

## Figure 9.2 Big Picture
  * Consider maximal set C *for given set t*.
     * Must be unique for t.  Why? **Two would be mergeable to make larger union**
  * All subsets of C are also supportable by at least t.  Some may be supported by exactly t.
  * Some t-supported subsets will be minimal.  Not necessarily unique
  * The maximal sets for t-sets with cardinality minsup are the "maximals".  May be several, one per t-set.

## Eclat modification
   * Algorithm 9.1 generates maximal sets
      * Compare with Eclat

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
         * Which is more significant, and why?  **Former, because bagels aren't that common, while milk is** 
      * Even highly confident rule can indicate *reverse* causation.
   * Lift concept
      * EQ 12.4
      * Emphasizes concept of statistical independence, and has an information theoretic feel.
      * Takes background likelihood of Y into account.  
      * If Bagel is .05 likely, lox .03 and milk .5, what are the lifts of our bagel/lox/milk example?
         * **Lox -> Bagel **.4 / .05 = 8**
         * **Lox -> Milk **.4 / .5 = .08**
       * Is a confidence of 1.0 with rsup .5 always an indication of causation?  What can lift be in  this case: min/max? **Lift can be 1.0, indicating no causation because Y always happens anyway.  It can also be 2.0 if only have Y with X**
       * How about low lift?  
         * Can it be less than confidence? **Cannot be less than confidence since divisor is <= 1.0**
         * So, if I have .5 confidence, lift must be at least .5? **Yes, and actually more since P(Y) < 1.0 in this case**
         * Significance?  **X actually discourages Y**
         * Does confidence of 0 mean that X *prevents* Y? **Not necessarily, if P(Y) = 0**
      * Consider min/max cases
         * How high can it be?  **No limit, with low rsup(Y) and high confidence**
         * How low? **0 if X and Y are completely disjoint, so confidence is 0**
         * Arrive at a lift of 10?  **probs of .1 can arrive at lift of 10**
         * Show how a rare pair of events can result in lift of 1000?  **Both .001 likely, but 100% correlated**
         * Tends to have high ceiling with rare Y -- focuses on probability ratio, not absolute values**
      * Symmetrical.  Why is this bad?  **No causality info**

   * Leverage concept
      * Eq 12.5
      * Division through by P(X)P(Y) results in lift - 1.0.  So is this just "differential lift"? **No, because it's lift-1.0 times rsup(X)*rsup(Y)**
      * So, like lift, but differential, and magnified by joint support (support of itemsets X and Y).
      * What is max leverage possible?  How obtained?  **Can't exceed 1.0 due to probs, but worse than that.  X and Y = 1/2 and fully correlated gets leverage of .25**
      * How about min leverage?  **Fully uncorrelated with .5 prob for X and Y gets -.25**
      * What is leverage like with light data (low probs), such as high-lift rare case earlier?  **Tends to near zero.  Fully correlated with .001 -> .00999.  Uncorrelated -.000001**

   * There are a *lot* of others, but of increasingly less general use.  Support, confidence, lift, and leverage are the major measures.  Here are two brief examples.
      * Jaccard
         * Draw Venn diagram.  Ratio of intersection ot "outer areas"
         * Sensitive at low prob values since just a ratio.

      * Conviction 
         * Conviction takes into account how likely rule is to *fail*, in particular X -> !Y$
         * Lift of this measure is bad if larger, so invert to 1 / lift(x -> !y)
   
 * Evaluating entire pattern or itemset, not just a particular X->Y
   * Support translates directly
   * Total lift
     * Eq 12.9 (Product notation)
     * Min/max
        * How large? **Maxed if all items occur concurrently.  1/P(item), so no limit**
        * How small? **Min of 0 if no items occur together ever.  Not going to have support, though**
        * Can lift of an itemset be 1 even if its support is 100%? **Yes, all items are 100% likely**
   * Need to consider lift or other measures for *all rules derived*
      * Essentially conisdering all causal relationships that might be derived from the itemset
      * Max, min, or average may be used.
         * Table 12.14
         * Discuss which is more important (min, max, ave) and why
            * Min susses out "duh" cases if these are fully explanatory
            * Max finds significance

   * Tradeoff of closed vs maximal
      * Closed gives maximal items (relationships) while maintaining support
      * Maximal will have most items (relationships) but with minimal support

   * "Productive" itemsets
      * EQ 12.11
      * Productive itemset if *all* A->B rules have lift > 1, or $lift_2(X) > 1.0$
      * Every item subset has some impact on remainder

 * Evaluating different rules
   * specificity vs generality
      * ABC->D (specific) vs AB->D (general)
      * Can specific have more support than general? **No, support only drops for superset**
      * If support is equal, what might we say about ABC->D?  **Redundant, don't really need C; could just work with AB**
      * Redundant rule is one where you can lose a precedent item without loss of support
   * Productive rules
      * Productive association cannot be made more general without loss of confidence
      * Why confidence instead of support? **More general cannot reduce support, only increase it**
      * So can confidence go *up* with more specific and less support? **Sure, because the X is narrowed, so it might be that it's more likely to get Y with a less-supported X than a general one.**
      * Example of more spscific rule with more confidence despite less support?  **buns and dogs -> mustard vs dogs -> mustard if dogs are very common**
   * Concept of overall "improvement"
      * Eq 12.12.
      * Minimal boost in confidence over what we'd get with more general rule.
 