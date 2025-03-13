# Cluster Evaluation

## Readings
 * Zaki Ch 17
 * Info Theory Overview

1. Describe a situation where $prec_i = 1.0$ but $recall_i = .1$ for all values of i.  How many classes are needed?  What is the F-score in this case?

2. What is the total purity and recall of a K-NN classifier with K=1, assuming the sample points used are the same as those for training?  What does this say about the measures and choice of test sample points?

3. Say we trade off precision vs recall in various ways, but always so that precision = 1 - recall.  What is the highest and lowest possible F-score? 

4. Assume you have a non-uniform probability distribution, with event probabilities ranging from .25 down to .01.  You divide one of the existing events into two equally-likely events, e.g. dividing an event E with 20% probability into E1 and E2 each with 10% probability.  Assuming $log_2$, what is the largest possible increase in entropy resulting from such a division?  The smallest?

5. If r = k, and I(C,T) = 4, what is the minimum possible value for r and k and why?  What will the contingency table look like in this case? (Do *not* try this by messing with the equations -- reason it out intuitively)

6. If I(C,T) = 0, what does this say about the value of "match"?

7. I transmit information about the classes of a set of sample values from a known ground-truth clustering.  But, I send the C values for each sample, not the T value, which means there may be some error.  For each case, indicate how many *additional* bits per sample I must transmit to correct any errors, on average, or indicate that you can't tell this from the value given.

a. I(C, T) = 4\
b. H(T|C) = 3\
c. H(C|T) = 3\
d. I(C, T) = 2 and H(C) = 3 \
e. I(C, T) = 2 and H(T) = 4

8. Now, assume instead I'm trying to communicate the results of a C-based classification of a set of samples from a known ground-truth T.  Answer the same question as above, for the same data:

a. I(C, T) = 4  \
b. H(T|C) = 3 \
c. H(C|T) = 3  \
d. I(C, T) = 2 and H(C) = 3 \
e. I(C, T) = 2 and H(T) = 4 

