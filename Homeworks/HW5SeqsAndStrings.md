# Sequences and Substrings

## Readings
Zaki
  * Chapter 10

## Exercises

1. Zaki Ch10 Q1
For a, just use the simple GSP algorithm, and draw the tree, or in text, show
each level of the tree with child nodes roughly aligned below parent.

2. Zaki Ch10 Q2 d and e only
   * For Spade use minsup = 5, and develop only sequences starting with A
   * For PrefixSpan use minsup = 4, but develop only sequences starting with A or C, and use only $s_1$ through $s_5$ from the database.  Remember to use 1-based numbering like the text.


3. Zaki Ch10 Q6
 Number the existing nodes 0 - 6, from top to bottom, left to right, for
 reference sake.  Number added nodes 7->, **in the order you add them, 
 not necessarily level-order**
 
 Based on that numbering, first list any existing suffix links that would 
 have to exist assuming Ukkonen's had been used to build the current suffix tree
 in format N# -> N#.  There are three.


Now, for each of the 10 added symbols, show new nodes and their suffix, the
changes to active_node, active_edge/len (or none), active_length, and 
remainder including possibly several such changes.  Also list any new suffix 
links created. Since this is complicated, here are the first 6 lines of the 
desired answer.  You must add another 12.

```
G          N#, none, remainder 1 (G)
GA         N6, none, remainder 2 (GA)
GAA        N6, A/1, remainder 3 (GAA)
GAAG       N6, A/2, remainder 4 (GAAG)
GAAGC      add N7/C for GAAGC. Use N6->N1. N1, A/2, remainder 3 (AAG)
           add N8/C for AAGC. Add N7->N8. N5, none, remainder 2 (AG)
```

4. Consider the Spade tree in Figure 10.2, and the generation of node GAAG 
from parents GAA and GAG.  Adding G as a final symbol to GAA results in 
the *L* value given for GAAG, derived from the *L* of GAA and GAG.  But, 
we're only adding G to the end of GAA, not adding the full sequence GAG, 
so shouldn't we be doing a sequential join using the *L* for sequence G 
alone (at the top of the tree) which has more positions than the *l* for GAG.  
Why or why not?

5. In figure 10.3, in the $D_A$ branch,  $S_2$ is just AG, rather than the 
CAG that might be expected from projecting on the $D_\emptyset S_2$ value
of TGACAG.  Why is this, and what line of code in Algorithm 10.3 makes 
this change? 

