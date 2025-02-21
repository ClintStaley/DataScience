# Homework 1 Review and Basics

## Readings
Zaki:
Ch 1, 2, 3.1

## Exercises
1. Provide a 3x3 matrix that rotates $\tau/8$ about the z-axis, folllowed by $-\tau/4$ about the y axis.

**Answer: $\begin{bmatrix}0&&0&&-1\\0&&1&&0\\1&&0&&0\end{bmatrix}\begin{bmatrix}.707&&-.707&&0\\.707&&.707&&0\\0&&0&&1\end{bmatrix}=\begin{bmatrix}0&&0&&1\\.707&&.707&&0\\.707&&-.707&&0\end{bmatrix}$**

2. Prove Zaki Eq 2.18, by starting with the right side, and evolving it into the left.  You should need at least 6 steps.\
**Answer:
$\Sigma{(x_i-\hat\mu)^2} + n(\hat\mu - \mu)^2$\
$= \Sigma{(x_i^2 -2x_i\hat{\mu} + \hat\mu^2)} + n(\hat{\mu}^2 -2\hat\mu\mu+ \mu^2)$\
$= (\Sigma{x_i^2}) -2n\hat{\mu}^2 + n\hat\mu^2 + n\hat{\mu}^2 -2n\hat\mu\mu+ n\mu^2$\
$= (\Sigma{x_i^2}) -2n\hat\mu\mu+ n\mu^2$\
$= \Sigma{(x_i^2 - 2x_i\mu + \mu^2)}$\
$= \Sigma{(x_i - \mu)^2}$**

3. Assume a set of 11 test scores, all between 0 and 100

   a. If the average score is above 90, what is the lowest possible median score?  **With 5 100s, 5 80s, and 1 81 you get 90.09 avg and 81 median**

   b. If the average score is under 50, what is the highest possible median score? **6 91s, and 5 0s gives median of 91**

   c. If the median is 50, what is the lowest possible mode? **0, with 5 at that value, and 5 spread out above 50**

4. I have an unreliable network provider, and they're down on 10% of days.\
In the course of a 365-day year, how likely is it they will be out on exactly\
36 of the days?  What number of outage days should I plan for, so that there\
is a 99.9% chance there won't be more days than that?  Show your work.  

**Binomial distribution ${365\choose36} .1^{36}.9^{329} = .0696$.  
Bernoulli distribution has $\mu = .1, \sigma^2 = .1(.9)^2 + .9(.1)^2 = 0.9, \sigma = .3$ 
Need z-value of 3.1 for 99.9% For 365 samples, $\sigma = .3\sqrt{365} = 19.1$  
So we need 36.5+19.1 = 55.6, rounded up to 56$**

5. Say a 3-D distribution is formed by multiplying independent univariate normal distributions $\mathcal{N}(x|\mu_x, \sigma_x^2)$, $\mathcal{N}(y|\mu_y, \sigma_y^2)$ and $\mathcal{N}(z|\mu_z, \sigma_z^2)$.  Give a single multivariate normal distribution that describes that 3-D distribution, in $\mathcal{N}(X|\Mu, \Sigma)$ form, with X representing $[x,y,z]^T$.  What are the values of $\Mu$ and $\Sigma$?

**$\Mu = [\mu_x, \mu_y, \mu_z]^T$ and $\Sigma = \begin{bmatrix}\sigma_x^2&&0&&0
\\0&&\sigma_y^2&&0\\0&&0&&\sigma_z^2\end{bmatrix}$**

6. Prove algebraically that your answer for the prior question is correct.
**Starting with product of independent distributions for x, y, and z:
 $X = \frac{1}{\sqrt{2\pi\sigma_x^2}}e^{-\frac{(x-\mu_x)^2}{2\sigma_x^2}}
 \frac{1}{\sqrt{2\pi\sigma_y^2}}e^{-\frac{(x-\mu_y)^2}{2\sigma_y^2}}
 \frac{1}{\sqrt{2\pi\sigma_z^2}}e^{-\frac{(x-\mu_z)^2}{2\sigma_z^2}}$
 $=\frac{1}{\sqrt{2\pi}^3} \frac{1}{\sqrt{\sigma_x^2\sigma_y^2\sigma_z^2}} e^{-(\frac{(x-\mu_x)^2}{2\sigma_x^2}+\frac{(x-\mu_y)^2}{2\sigma_y^2}+\frac{(x-\mu_z)^2}{2\sigma_z^2})}$\
 $=\frac{1}{\sqrt{2\pi}^3} \frac{1}{\sqrt{|\Sigma|}} e^{(-\frac{(x-\mu_x)\frac{1}{\sigma_x^2}(x-\mu_x)+(y-\mu_y)\frac{1}{\sigma_y^2}(y-\mu_y)+(z-\mu_z)\frac{1}{\sigma_z^2}(z-\mu_z)}{2})}$\
  $=\frac{1}{\sqrt{2\pi}^3\sqrt{|\Sigma|}} e^{(-\frac{(X-\Mu)^T\Sigma^{-1}(X-\Mu)}{2})}$**

7. Given a 3-dimensional multivariate normal distribution $\mathcal{N}(X|[1, 2, 3]^T, \begin{bmatrix}.417&&-.0589&&.0589
\\-.0589&&.708&&.292\\.0589&&.292&&.708\end{bmatrix})$, what is the conditional distribution taken along the x axis, with y=2 and z=3?  Provide a precise equation for this, using ($\tau$ not $\pi$, this time).

**Inverse is**\
[ 2.5    0.354  -0.354    ]\
[ 0.354  1.75   -0.75      ]\
[-0.354 -0.75    1.75      ]\

**So numerator of exponent is $2.5(x^2-1)$ and thus $\sigma^2 = .4$ and exact equation is $\frac{1}{\sqrt{\tau 0.4}}e^{-\frac{(x-1)^2}{.8}}$.**

8. Three bags contain colored balls in the proportions below.  I choose from bag 1 10% of the time, from bag 2 40% of the time, and from bag 3 50% of the time.  I choose a ball via this rule, and it's red.  What is the chance it came from bag 2?
  * Bag 1: 10% red, no green, 90% blue
  * Bag 2: 50% red, 25% green, 25% blue
  * Bag 3: 90% red, 5% green, 5%% blue

**$p(b2|red) = \frac{p(red|b2)p(b2)]}{p(red)} = .4(.5) / (.1(.1) + .4(.5) + .5(.9) = .2 / .66 = .303$

