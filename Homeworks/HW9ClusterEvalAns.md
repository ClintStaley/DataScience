# Cluster Evaluation

## Readings
 * Zaki Ch 17
 * Info Theory Overview
 
1. Describe a situation where $prec_i = 1.0$ but $recall_i = .1$ for all values of i.  How many classes are needed?  What is the F-score in this case?

**10 classes have the same $T_{j_i}$, with no other samples in other columns. F = .182**

2. What is the total purity and recall of a K-NN classifier with K=1, assuming the sample points used are the same as those for training?  What does this say about the measures and choice of test sample points?

**Both are 1.0, yet the 1-NN isn't a great classifier, so measures are imperfect, and we would do better with sample points not from the training set**

3. Say we trade off precision vs recall in various ways, but always so that precision = 1 - recall.  What is the highest and lowest possible F-score? **.5 and 0**

4. Assume you have a non-uniform probability distribution, with event probabilities ranging from .25 down to .01.  You divide one of the existing events into two equally-likely events, e.g. dividing an event E with 20% probability into E1 and E2 each with 10% probability.  Assuming $log_2$, what is the largest possible increase in entropy resulting from such a division?  The smallest?

**Dividing a .25 event will result in increase of .25 entropy.  Dividing a .01 event results in .01 entropy increase.**

5. If r = k, and I(C,T) = 4, what is the minimum possible value for r and k and why?  What will the contingency table look like in this case? (Do *not* try this by messing with the equations -- reason it out intuitively)

**This implies that C and T each communicate 4 bits of information about the other.  For this to be possible, there must be 4 bits of entropy in C and T, which implies a minimum of r = k = 16, and uniform likelihood of C and T elements.  The contingency table has 16 nonzero elements, all with same $n_{ij}$, though not necessarily on the diagonal as long as there are no common rows or columns**

6. If I(C,T) = 0, what does this say about the value of "match"?

**All matches are equally good.**

7. I transmit information about the classes of a set of sample values from a known ground-truth clustering.  But, I send the C values for each sample, not the T value, which means there may be some error.  For each case, indicate how many *additional* bits per sample I must transmit to correct any errors, on average, or indicate that you can't tell this from the value given.

a. I(C, T) = 4  **Can't tell -- depends on H(T)**\
b. H(T|C) = 3  **3 additional bits**\
c. H(C|T) = 3  **Can't tell**\
d. I(C, T) = 2 and H(C) = 3 **Still can't tell**\
e. I(C, T) = 2 and H(T) = 4 **2 additional bits**

8. Now, assume instead I'm trying to communicate the results of a C-based classification of a set of samples from a known ground-truth T.  Answer the same question as above, for the same data:

a. I(C, T) = 4  **Can't tell -- depends on H(C)**\
b. H(T|C) = 3  **Can't tell**\
c. H(C|T) = 3  **3 additional bits**\
d. I(C, T) = 2 and H(C) = 3 **1 additional bit**\
e. I(C, T) = 2 and H(T) = 4 **Can't tell**

