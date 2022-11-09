# Chapter 18 Probabilistic Classification

## Readings
Zaki Chapter 18

## Exercises

1. Zaki Ch18Q1, naive Bayes only. Note that this means you'll have one numerical and one categorical attribute
   * Per Zaki, p 479: "Extending the code in Algorithm 18.2 to incorporate categorical attributes is straightforward".  Well, maybe.  Explain briefly here how you would do that?  What lines of the algorithm change, and why?

   **Lines 5-9 get replaced by $n_i$ counting, and f is redefined on line 11 to be equatino at top of p 479**

   * Show the naive Bayes calculation for (Age=23, Car=truck). *Change the age on the first item from 25 to 30*

$\mu_{11} = \frac{25 + 30}{2} = 27.5$ $\sigma_{11} = \sqrt{\frac{25^2+30^2}{2} - 27.5^2} = 2.5$

$\mu_{21} = \frac{25 + 45 + 20 + 25}{4} = 28.75$ $\sigma_{21} = \sqrt{\frac{25^2+45^2+20^2+25^2}{4} - 28.75^2} = 9.6$



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

3. In line 7 of Algorithm 18.1 (p. 471) give an example of a 2-attribute, 2-class data set for which $\Sigma_1$ might be nearly diagonal but $\Sigma_2$ is not.  Explain your answer.

**Attributes height and width, for classes square and rectangle.  Diagonal $\Sigma$ indicates independent distribution within the class, which would be true for rectangle, but not for square**

4. Explain the term $\prod_{j=1}^d m_j$ in equation 18.8:

   * What do the $m_j$ values signify?
   * Why would we multiply them all together?
   * What does the product signify?

**$m_j$ is the number of categorical choices for attribute j.  We are supplying one "free" count of each possible mixture of categorical choices for d attributes.  The number of such choices is the product of choices for category 1, times that for category 2, etc.**

5. Give an example of a classification problem where naive Bayes might be expected to fail.  Explain your answer.

**The answer to question 3, since it is the very correlation of height and width that marks a square.  Multiplying independent height and width likelihood would not distinguish squares from rectangles.**

6. Do the same for a classification problem where naive Bayes is likely to be about as good as full Bayes.

**Many possibilities.  Need cases where each attribute contributes independently to classification, e.g. house classification as low, mid, high range, with properties like square footage, age, location.**