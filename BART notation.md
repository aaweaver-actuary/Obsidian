[[Statistical Learning Lectures]]

- $K$ - number of [[Regression|regression]] [[Tree-Based Methods|trees]]
- $B$ - number of iterations for which the [[Bayesian Additive Regression Trees (BART)|BART]] algorithm will be run
- $\hat{f}_k^b(x)$ - the prediction at $x$ for the $k$th [[Regression|regression]] [[Tree-Based Methods|tree]] used in the $b$th iteration
- at the end of each iteration, the $K$ [[Tree-Based Methods|trees]] from that iteration will be summed:
$$
\hat{f}^b(x) = \sum_{k=1}^K \hat{f}_k^b(x), \space \text{ for } b=1,\dots,B
$$
- $L < B$ is chosen as the number of #burn-in-iterations and discarded
- final prediction:
$$
\hat{f}(x) = \frac{1}{B-L}\sum_{b=L+1}^B \hat{f}^b(x)
$$
