# Regression

## Graph Basics
  * Review initial concepts from Zaki 4.1
  * Review DFS basics
    * Basic stack-based process
    * Forward and backward edges

## GSpan -- finding Isomorphisms
  * Zaki Ch 11
  * Graph example in Fig 11.1, including labels.
  * Isomoprhism and "subgraph isomorphism" -- Fig 11.3
    * Review "injective" -- domain is covered
    * Review "surjective" -- codomain or range is inversely covered.
    * Another name for "injective and surjective"? **One to one**
  * Review mappints in Example 11.3 to see that isomorphism can be "slippery"
  * DFS concept
    * Use Figure 11.4 for an example
    * Do a DFS that has a path of 7.  **Multiple possibilities**
    * One with a path of at most 2.  **Start at c**
    * Forward and backward edges.
      * Can there be forward edges not in the DFS tree? **No, since they'd have become forward edges from the opposite side**
      * Could there be with a *directed* graph? **Yes, directed graphs result in two new categories, often termed forward and cross, with "tree edge" for those in the DFS**
  * Jump to Fig 11.6
    * Are the three graphs isomorphic? **Yes, but a little hard to see that, even with just four nodes**
    * Can we use DFS to identify isomorphisms?
    * Edge orders in the DFScodes for each
  * Fig 11.5, a systematic way to pick a representative DFS
    * At each node as we traverse
      * Do all reverse edges before proceeding, and in order from root down.
      * When backtracking to pick alternate forward paths, do so in order from leaf to root.
        * This is natural for DFS anyway.
    * Try this on Fig 11.2, preferring lower labels first
  * Now back to Fig 11.6
    * Strict rules for ordering of edges, Eq 11.2
    * Review each of the steps for edge-order, ask for intuition on each
    * Analyze noncanonical cases in Fig 11.6.
    * Try another DFS, starting with b, and produce its edges.  Are they canonical?
    


