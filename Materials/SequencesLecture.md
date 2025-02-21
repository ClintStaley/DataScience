# Sequence Mining

## Basics
 * Sequence, subsequence, and substring
    * Definition of support: Number of sequences, not number of occurrences.

## Subsequence Mining
 * Fig 10.1
    * What is different about this tree vs the itemsets lattice?
    * Super/sub *sequences* not subsets
    * Order matters, so all letters extend
    * Support still monotonic?  Why/why not?\
      **subseq has to also be supported same.  superseq can't be more.** 
 * Brief overview GSP
    * APriori style approach (GSP -- Generalized Sequential Pattern)
    * Why children(parent) on 17, and no a<b?  **symbols, including self, are repeatable.**
    * Trace tree development briefly
    * Really isn't optimal for this problem, so no detailed analysis needed
 * SPADE algorithm
    * Sequential Pattern Discovery Using Equivalence Classes
    * Concept of final-symbol potential locations
    * How to merge different locations (left must have value lower than right)
       * First level is obvious
       * Clarify that later levels can merge **with siblings**
          * Only need final letter, which is guaranteed at the given spot
          * Only need to know if a subsequences is anywhere present.
             * Does this find *all* instances per sequence?
                * How many AAs in s1? **Three, so not all are represented**
                * What if s2 was GGACAG?  Does it keep the GG at 2? **No, gets eliminated**
    * Trace logic of 10.4 tree, for a few.  Then have them trace the rest.
       * Note minsup = 3, and diagram may show dead leaves, but not develop them.
    * Algorithm 10.2: 
       * What is definition of intersection on line 6? **Read to reinforce concept from above**
       * What is the algorithm analagous to?
   
* PrefixSpan
   * Faster than SPADE
   * Figure 10.3
      * Recursive breakdown by letter
      * Prefilter all next-letters to remove infrequent -- thus no $D_C$
   * Similar to?? **FPGrowth**
   * Walk through tree in Fig 10.3
   * Walk through Algorithm 10.3
      * "Projection" means cutting down based on assumption of current prefix

## Suffix trees
 * Review basic suffix tree idea.  
   * Do exercises, adding new strings
   * Efficiencies
      * Substring ranges on branches
      * Track support
   * Use for finding substrings
   * Trie, Patricia tree or radix tree
   * Why suffix and not prefix?  **forward seeking requires suffix mode**
   * Order of complexity for string hunt -- clear choice at each node, so O(n) in # of symbols.
 * Building one fast.  Ukkonen's algorithm.
   * (Sample patterns  CAGAAGT TGACAG, abcabxabcdabcde, abracadabra,ABCABXABCDABCX)
   * Reduce storage by reference to original strings on legs
   * Start by building suffix tree *for a prefix of S*
      * Takes double-thinking.  We extend a given "phase" by adding a new symbol at the end, and extending existing suffixes.
      * Illustrate a phase or two for ABCD using animation site.
   * Implicit suffixes!
     * ABCDABCX as example
        * The prefix-suffix repeats will *eventually* be on this branch, but we don't have enough info to know where it breaks.
        * Build up an "IOU" stack
        * When we get a break, then "pay off" the IOUs
           * Do the main branch, then fall back by taking away first char!
           * How do we find the "fallback location"? **Simple search if off of root**
           * Will fallback always also require a new node? **Yes, since e.g. if ABC but not X is in tree, so is BC but not X.**
      * Try ABCABXABCD
   * OK, now make it *really* efficient
     * Describe legs by index ranges, leaving content in the actual string.
     * Generalize final index as # or e, so we can "lengthen" ALL leaf legs by a single increment.
     * When we do a "fallback", REMEMBER where we went so we don't repeat it.  Not a big deal with one level, but is with many.
   * Don't try to understand this from Zaki; explanation sucks.  Use the SO post instead.
   * Run example, inviting prediction of next steps
     * How to get second level of suffix links to be used? 
   * All this ultimates in an O(n) algorithm.  Each step requires advancing a couple of markers, and possibly an "IOU" payment. 
      * Can IOU payment be arbitrarily long? **Yes, but total of all IOUS cannot exceed n**
   

