# Density Clustering
## Readings
 * Zaki Ch 15
 
 # Homeworks

 1. Zaki Ch 15 Q1

**a. Core: a, b, c, d, e, f, g, h, i, j, k, n, o, p, q, r, s, t, v, w  (all but l, m, u, x)**

**b. Yes**

**c. Yes: i, e, c, f, j, n**

**d. No, since y may not be core**

**e. Yes.  l - t - w - x**

**f Yes, since reachability from central point goes both ways**

**g. {p, q, v, r, s, t, w, x, k, h, d, a, l}, {m, i, e, b, c, f, g, j, n, o}  U is noise**

2. Zaki Ch 15 Q5 but for numbers 2, 2.5, 3, 4, 4.3, 5, 6.1

**Want to find point where 4 neighbors span smallest distance, and name the centerpoint.  That's 2.5 - 4.3, span 1.8, center is 3.4, density is $\frac{4}{7(1.8)} = .317**

3. Does A in algorithm 15.2 contain actual data points?  How often if so?

**No, unless by fluke a max in the continuous function matches a data point**

4. Describe how you might implement line 7 of Alg 15.2

**Any reasonable description that shows we need to find a path from one to the other that doesn't get below a given level**