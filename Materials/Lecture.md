# Day 2
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
  * 
  * 9.4
    * Can maximal itemset be expanded by closure? (No, so M $\subseteq$ C)
    * Is closed itemset automatically maximal? (No)

## Min Generator
  * English meaning of 9.5?  ("Can't lose an item without gaining a transaction")
  * Unique min-generator to maximal subset pairing? (No, can lose different items without gaining transactions)
  * Consider ABCD, ABC, ACD,

## Fig 9.2
  * 

   
   

 