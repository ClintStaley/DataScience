# Week 3 Sequences and Substrings

## Readings
Zaki
  * Chapter 1.3.3
  * Chapter 10

## Exercises

### Zaki
Ch 1
 * Find the p and r vector values from projecting [5, 4, 2] onto [2, 1, -1] 

 **$p = \frac{12}{6}  \left[ \begin{array}{c} 2 \\ 1 \\ -1 \end{array}\right] = \left[\begin{array}{c} 4 \\ 2 \\ -2 \end{array}\right]$**

 $r = \left[ \begin{array}{c} 5 \\ -1 \\ 2 \end{array}\right] - \left[\begin{array}{c} 4 \\ 2 \\ -2 \end{array}\right] = \left[\begin{array}{c} 1 \\ 2 \\ 4 \end{array}\right]$

Ch 10 
 * Q1
   * Just use the simple GSP algorithm, not Spade or others

a. GSP gives tree of 17 frequent sequences (all supports 4)
```
A                        G         T        
AA    AG    AT           GA        TA   TG 
AAT   AGA   ATA  ATG     GAA       TAA  TGA
                 ATGA
```

b. At each step, including the first, there are four choices: GATC.  So,
there are $4^k$ possible sequences.
 * Q2
   * Do just d and e
   * For Spade use minsup = 5, and develop only sequences starting with A
   [Spade minsup 5](Ch10Q2Spade.jpg)
   * For PrefixSpan use minsup = 4, but develop only sequences starting with A or C. [Prfix minsup 4](Ch10Q2Prefix.jpg)

 * Q6
   * Number the existing nodes 0 - 6, from top to bottom, left to right, for reference sake.  Number added nodes 7->, **in the order you add them, not necessarily level-order**
   * Name any existing suffix links that would have to exist assuming    Ukkonen's had been used to build the current suffix tree.
   ```
   N5 -> N3
   N6 -> N1
   N2 -> N5
   ```
   * For each of the 10 added symbols, show new nodes and their suffix, the changes to active_node, active_edge/len (or none), active_length, and remainder including possibly several such changes.  Also list any new suffix links created.
   * Show the final tree, including leaf node contents.

```
G          N#, none, remainder 1 (G)
GA         N6, none, remainder 2 (GA)
GAA        N6, A/1, remainder 3 (GAA)
GAAG       N6, A/2, remainder 4 (GAAG)
GAAGC      add N7/C for GAAGC. Use N6->N1. N1, A/2, remainder 3 (AAG)
           add N8/C for AAGC. Add N7->N8. N5, none, remainder 2 (AG)
           add N5/C for AGC. Add N8->N5, use N5->N3. N3, none, remainder 1 (G)
           add N3/C for GC. N0, C/1, remainder 1 (C)
GAAGCA     N0, C/2, remainder 2 (CA)
GAAGCAG    N0, C/3, remainder 3 (CAG)
GAAGCAGA   N2, A/1, remainder 4 (CAGA)
GAAGCAGAA  N2, A/2, remainder 5 (CAGAA)
GAABCAGAA$ add N9/$ for CAGAA$. Use N2->N5. N5 A/2, remainder 4 (AGAA)
           add N10/$ for AGAA$. Add N9->N10, use N5->N3. N6 A/1, remainder 3 (GAA)
           add N11/$ for GAA$. Add N10->N11, use N6->N1. N1 A/1, remainder 2 (AA)
           add N12/$ for AA$. Add N11->N12. N1, none, remainder 1 (A)
           add N1/$ for A$. Add N12->N1. N0, none remainder 0
           add N0/$
```

 * Consider the Spade tree in Figure 10.2, and the generation of node GAAG from parents GAA and GAG.  Adding G as a final symbol to GAA results in the *L* value given for GAAG, derived from the *L* of GAA and GAG.  But, we're only adding G to the end of GAA, not the full sequence GAG, so shouldn't we be doing a sequential joing using the *L* for sequence G alone (at the top of the tree) which has more positions than the *l* for GAG.  Why or why not?

```
The L for G doesn't take into account the fact that the final G must be 
preceded by GA.  The L for GAG assumes that GA will precede the final G,
which is correct for the case where the merged sequece will be GAAG.  Using
G won't cause errors, but is inefficient.
```

* In figure 10.3, in $D_A$,  $S_2$ is just AG, rather than the CAG that might 
be expected from projecting on the $D_\emptyset S_2$ value of TGACAG.  Why is 
this, and what line of code in Algorithm 10.3 makes this change? 

```
Line 7 removes the C from the $D_\emptyset$ representation of $S_2$ before 
the projection even occurs, since no sequence containing C can meet the
minsup of 3
```
