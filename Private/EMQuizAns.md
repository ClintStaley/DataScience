# EM Clustering
<div style="text-align: right">Name __________________________________________</div>

1. 30pts\
Assume two clusters with $\theta$ values given, and two data points as given.

$\theta_1 = \mathcal{N}([1,1], 5I), P=.25$\
$\theta_2 = \mathcal{N}([5,4], 5I), P=.75$\
$x_1 = [1,1], x_2=[5,4]$

Show the four $w_{ij}$ values that result, and recompute the $\theta$ values 
from them.  **Assume dimensions are independent**

$w_{11}$ = ______\
$w_{12}$ = ______\
$w_{21}$ = ______\
$w_{22}$ = ______

**Answer: $P(x_1|c_1) P(x_2|c_2 )= \frac{1}{\tau5} = .0318, P(x_2|c_1) = P(x_1|c_2) = \frac{e^{-2.5}}{\tau5} = .0026$\
\
$w_{11} = \frac{.25(.0318)}{.25(.0318) + .75(.0026)} = .803$\
$w_{12} = \frac{.25(.0026)}{.75(.0318) + .25(.0026)} = .027$\
$w_{21} = \frac{.75(.0026)}{.25(.0318) + .75(.0026)} = .197$\
$w_{22} = \frac{.75(.0318)}{.75(.0318) + .25(.0026)} = .973$
