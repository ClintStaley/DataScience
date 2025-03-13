# Chapter 18 Probabilistic Classification

## Readings
Zaki Chapter 18

## Exercises

1. Zaki Ch18 Q1, naive Bayes only. Note that you'll have one numerical and one categorical attribute.
   * Per Zaki, p 479: "Extending the code in Algorithm 18.2 to incorporate categorical attributes is straightforward".  Well, maybe...  Explain briefly here how you would do that.  What lines of the algorithm change, and why?

   **Lines 5-9 get replaced by $n_i$ counting, and f is redefined on line 11 to be equation at top of p 479**

   * Show the naive Bayes calculation for (Age=23, Car=truck). *Change the age on the first item from 25 to 30*

$\mu_{11} = \frac{25 + 30}{2} = 27.5$ 

$\sigma_{11} = \sqrt{\frac{25^2+30^2}{2} - 27.5^2} = 2.5$

$\mu_{21} = \frac{25 + 45 + 20 + 25}{4} = 28.75$ 

$\sigma_{21} = \sqrt{\frac{25^2+45^2+20^2+25^2}{4} - 28.75^2} = 9.6$

$P(v_{sports} | C_1) = \frac{3}{6} = .5$

$P(v_{vint} | C_1) = \frac{1}{6} = .1666$

$P(v_{suv} | C_1) = \frac{1}{6} = .1666$

$P(v_{truck} | C_1) = \frac{1}{6} = .1666$

$P(v_{sports} | C_2) = \frac{2}{8} = .25$

$P(v_{vint} | C_2) = \frac{2}{8} = .25$

$P(v_{suv} | C_2) = \frac{3}{8} = .375$

$P(v_{truck} | C_2) = \frac{1}{8} = .125$

$P(C_1) = .333; P(C_2) = .667$

$P(X | C_1) = .333(.1666)\frac{e^{(-.5)(\frac{-4.5}{2.5})^2}}{\sqrt{2\pi}2.5} = (.0555)\frac{.198}{6.27} = .00175$

$P(X | C_2) = .666(.125)\frac{e^{(-.5)(\frac{-5.75}{9.6})^2}}{\sqrt{2\pi}9.6} = (.0833)\frac{.836}{23.87} = .00292$

C2 is the chosen class.

2. Zaki Ch18Q3, and compute precisely the likelihood of each class given the point.

$x = (3, 4)^T, x-\mu_1 = (2,1)^T, x-\mu_2 = (-2, -1)^T$

$P(x | c_1) = \frac{e^{-\frac{\begin{bmatrix}2 && 1\end{bmatrix}\begin{bmatrix}2&&-3\\-3&&5\end{bmatrix}\begin{bmatrix}2\\1 \end{bmatrix}}{2}}}{2\pi\sqrt{|\begin{bmatrix}5&&3\\3&&2\end{bmatrix}|}} = \frac{e^{-0.5}}{2\pi} = .0965$

$P(x | c_2) = \frac{e^{-\frac{\begin{bmatrix}-2 && -1\end{bmatrix}\begin{bmatrix}0.5&&0\\0&&1\end{bmatrix}\begin{bmatrix}-2\\-1 \end{bmatrix}}{2}}}{2\pi\sqrt{|\begin{bmatrix}2&&0\\0&&1\end{bmatrix}|}} = \frac{e^{-1.5}}{2\pi\sqrt{2}} = .0251$

$P(c_1|x) = \frac{.0965(.5)}{.0965(.5) + .0251(.5)} = .794$
$P(c_1|x) = \frac{.0251(.5)}{.0965(.5) + .0251(.5)} = .206$

3. For the prior problem what P values for the classes would be necessary to change the classification of x?  

$\frac{P(c_1)}{1-P(c_1)} = \frac{.0251}{.0965}$

$P(c_1) = .26 - .26P(c_1)$

$P(c_1) = .206; P(c_2) = .794$

4. In line 7 of Algorithm 18.1 (p. 471) give an example of a 2-attribute, 2-class data set for which $\Sigma_1$ might be nearly diagonal but $\Sigma_2$ is not.  Explain your answer.

**Attributes height and width, for classes square and rectangle.  Diagonal $\Sigma$ indicates independent distribution within the class, which would be true for rectangle, but not for square**

5. Explain the term $\prod_{j=1}^d m_j$ in equation 18.8:

   * What do the $m_j$ values signify?
   * Why would we multiply them all together?
   * What does the product signify?

**$m_j$ is the number of categorical choices for attribute j.  We are supplying one "free" count of each possible mixture of categorical choices for d attributes.  The number of such choices is the product of choices for category 1, times that for category 2, etc.**

6. Give an example of a classification problem where naive Bayes might be expected to do much worse than full Bayes.  Explain your answer.

**The answer to question 3, since it is the very correlation of height and width that marks a square.  Multiplying independent height and width likelihood would not distinguish squares from rectangles.**

7. Do the same for a classification problem where naive Bayes is likely to be about as good as full Bayes.

**Many possibilities.  Need cases where each attribute contributes independently to classification, e.g. house classification as low, mid, high range, with properties like square footage, age, location.**

8. So, what about a classification problem where there are, say, 9 attributes, of which the first three are numerical and correlated, and so are the last two, which are categorical, with the others reasonably likely to be independent.  What might you do to combine full and naive Bayes to get the best of both worlds with respect to efficiency and consideration of the subsets of correlated attributes.

**Could use multivariate normal for the first three as their own subunit, plus the full Bayes categorical for the last two, and then naive Bayes to combine 1-3, 4, 5, 6, 7 and 8-9**

9. Compare the order of complexity for K-Nearest classification, and NB, both training and evaluation of samples.  Use K, k (# of classes), n, and d as variables. Assume no special data structure that will speed determination of near points -- distance to all must be computed.  Don't assume k is trivial wrt n.  Describe a situation where K-NN would actually be about as fast as NB in evaluation.

**No training, so far better than NB's O(nd) there.  Evaluation is O(nd + (n+k)logn), vs NB O(kd), so far worse, unless k = O(n)**

10. Say we have just two classes, each with the same number of sample points, and with sample points uniformly spread around the space.  How would NB classification divide the space between the two classes?  What, roughly, would the division look like?  How would KNN, do so, with K=1?  (Use an appropriate term for the shape of the spaces in the KNN case).   

**NB would have slightly different $\mu$ values by random chance, and very large $\Sigma$, so we'd expect a rough division into half, though this could be complicated if the $\Sigma$s differed and the $\mu$s were close to eachother.  KNN would produce a Voronoi diagram**

11. K-Nearest does not always produce an unambiguous classification.  Why not?  Suggest a way to repair this flaw via thoughtful choices of K.

**Two classes might have the same $K_i$ ratio.  Choosing a prime K would eliminate this possibility, and primes are fairly dense**
