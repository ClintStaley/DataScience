# EMClusters Quiz
<div style="text-align: right">Name __________________________________________</div>

1. 5pts \
$\begin{bmatrix}2 \\ 3 \end{bmatrix} \begin{bmatrix}4&&5\end{bmatrix}$ = $\begin{bmatrix}8&&10\\12&&15\end{bmatrix}$

2. 15pts \
5% of cars are red, and 2% of red car drivers are speeders.  Non-red car drivers are only 1% likely to speed.  If a car is speeding, what is the likelihood it's red?

$P(r|s) = \frac{P(r)P(s|r)}{P(r)P(s|r)+P(\neg r)P(s|\neg r)} = \frac{.05(.02)}{.05(.02)+.95(.01)} = \frac{.01}{.01+.095} = .0952$

3. 15pts \
Two clusters $C_1$ and $C_2$ have centers at (1, 1), and (0, 10), respectively.  Point $x_i$ is at (0,0), yet $w_{2i} > w_{1i}$  Explain two different ways this could be possible despite the distance of $x_i$ from the respective centers.

$P(C_1) << P(C_2)$ 7pts


$|\Sigma_1| << |\Sigma_2|$, in the right directions. 8pts


4. 15pts (extra credit) \
\
A cluster has $\mu = \begin{bmatrix}5\\5\end{bmatrix}$ and
 $\Sigma = \begin{bmatrix}0.84&&-1.67\\-1.67&&8.66\end{bmatrix} = \begin{bmatrix}.98&&-0.2\\0.2&&0.98\end{bmatrix}\begin{bmatrix}0.5&&0\\0&&9\end{bmatrix}\begin{bmatrix}.98&&0.2\\-0.2&&0.98\end{bmatrix}$\
 \
 Draw an approximate to-scale picture of the ellipse at one standard deviation distance from the center of this cluster.

 2pts centered at 5,5\
 5pts vertically oriented\
 4pts about 11 degrees ccw\
 4pts long axis of 3, not 9; short axis of about .7, or 1/4 of long