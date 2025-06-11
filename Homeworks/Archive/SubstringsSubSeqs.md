# Week 3 Sequences and Substrings

## Readings
Zaki
  * Chapter 1.3.3
  * Chapter 10

## Exercises

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
    * Number the existing nodes 0 - 6, from top to bottom, left to right, for reference sake.  Number added nodes 7->, in the order of addition, not in level-order.
    * Add any suffix links that would have to exist assuming Ukkonen's had been used to build the current suffix tree.
    * Hand run the algorithm on the specified string (10 symbols in all), carefully tracking the following for your own reference.  You don't need to hand in all this detail (see below) but you should retain it for reference if you need help getting the right answer.
      * the changes to active_node, active_edge/active_length (or none), and remainder
      * any new suffix links created
      * which suffix links are actually used
      * An example from my notes looks like this.  Yours may differ but should have the same content: add N10/$ for AGAA$. Add N9->N10, use N5->N3. N6 A/1, remainder 3 (GAA)
    * As a reality check, you should end up with 
      * 13 nodes total
      * a remainder as high as 5 at one point.
      * 9 suffix links, three in advance and 6 during the string addition
    * Submit the following:
      * The final tree, without any suffix links added (reduces clutter). 
      * A list of the suffix links you added *before* even starting the algorithm, in the form NX -> NY with X and Y node numbers
      * A similar list of suffix links you added while inserting the string.
      * After each suffix link in either list, put "used" if it was used during the insertion of the string.

 * QA
 Consider the Spade tree in Figure 10.2, and the generation of node GAAG from parents GAA and GAG.  Adding G as a final symbol to GAA results in the *L* value given for GAAG, derived from the *L* of GAA and GAG.  But, we're only adding G to the end of GAA, not the full sequence GAG, so shouldn't we be doing a sequential joing using the *L* for sequence G alone (at the top of the tree) which has more positions than the *l* for GAG.  Why or why not?

 * QB
In figure 10.3, in $D_A$,  $S_2$ is just AG, rather than the CAG that might 
be expected from projecting on the $D_\emptyset S_2$ value of TGACAG.  Why is 
this, and what line of code in Algorithm 10.3 makes this change? 

