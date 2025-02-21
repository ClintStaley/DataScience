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
