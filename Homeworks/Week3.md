# Week 3 Sequences and Substrings

## Readings
Zaki
  * Chapter 1.3.3
  * Chapter 10

## Exercises
All due Monday 2:20p 9/19

### Zaki
Ch 1
 * Find the p and r vector values from projecting [5, 4, 2] onto [2, 1, -1] 

Ch 10 
 * Q1
   * Just use the simple GSP algorithm, not Spade or others
 * Q2
   * Do just d and e
   * For Spade use minsup = 5, and develop only sequences starting with A
   * For PrefixSpan use minsup = 4, but develop only sequences starting with A or C.
 * Q6
 * Consider the Spade tree in Figure 10.2, and the generation of node GAAG from parents GAA and GAG.  Adding G as a final symbol to GAA results in the *L* value given for GAAG, derived from the *L* of GAA and GAG.  But, we're only adding G to the end of GAA, not the full sequence GAG, so shouldn't we be doing a sequential joing using the *L* for sequence G alone (at the top of the tree) which has more positions than the *l* for GAG.  Why or why not?

* In figure 10.3, the projection of $S_2$ in $D_\emptyset$ on A is just AG in $D_A$, rather than the CAG that might be expected.  Why is this, and what line of code in Algorithm 10.3 makes this change? 
