# Chapter 18 Probabilistic Classification

## Readings
Zaki Chapter 18

## Exercises

1. Zaki Ch18 Q1, naive Bayes only. Note that you'll have one numerical and one categorical attribute.
   * Per Zaki, p 479: "Extending the code in Algorithm 18.2 to incorporate categorical attributes is straightforward".  Well, maybe...  Explain briefly here how you would do that.  What lines of the algorithm change, and why?


   * Show the naive Bayes calculation for (Age=23, Car=truck). *Change the age on the first item from 25 to 30*



2. Zaki Ch18Q3, and compute precisely the likelihood of each class given the point.


3. For the prior problem what P values for the classes would be necessary to change the classification of x?  


4. In line 7 of Algorithm 18.1 (p. 471) give an example of a 2-attribute, 2-class data set for which $\Sigma_1$ might be nearly diagonal but $\Sigma_2$ is not.  Explain your answer.


5. Explain the term $\prod_{j=1}^d m_j$ in equation 18.8:

   * What do the $m_j$ values signify?
   * Why would we multiply them all together?
   * What does the product signify?


6. Give an example of a classification problem where naive Bayes might be expected to do much worse than full Bayes.  Explain your answer.



7. Do the same for a classification problem where naive Bayes is likely to be about as good as full Bayes.



8. So, what about a classification problem where there are, say, 9 attributes, of which the first three are numerical and correlated, and so are the last two, which are categorical, with the others reasonably likely to be independent.  What might you do to combine full and naive Bayes to get the best of both worlds with respect to efficiency and consideration of the subsets of correlated attributes.



9. Compare the order of complexity for K-Nearest classification, and NB, both training and evaluation of samples.  Use K, k (# of classes), n, and d as variables. Assume no special data structure that will speed determination of near points -- distance to all must be computed.  Don't assume k is trivial wrt n.  Describe a situation where K-NN would actually be about as fast as NB in evaluation.



10. Say we have just two classes, each with the same number of sample points, and with sample points uniformly spread around the space.  How would NB classification divide the space between the two classes?  What, roughly, would the division look like?  How would KNN, do so, with K=1?  (Use an appropriate term for the shape of the spaces in the KNN case).   



11. K-Nearest does not always produce an unambiguous classification.  Why not?  Suggest a way to repair this flaw via thoughtful choices of K.


