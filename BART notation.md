#notation #bart #statistical-learning

(in [[Statistical Learning Lectures]])

- $K$ - number of regression trees
- $B$ - number of iterations for which the BART algorithm will be run
- $\hat{f}_k^b(x)$ - the prediction at $x$ for the $k$th regression tree used in the $b$th iteration
- at the end of each iteration, the $K$ trees from that iteration will be summed:
$$
\hat{f}^b(x) = \sum_{k=1}^K \hat{f}_k^b(x), \space \text{ for } b=1,\dots,B
$$
- $L < B$ is chosen as the number of *burn-in iterations* and discarded
- final prediction:
$$
\hat{f}(x) = \frac{1}{B-L}\sum_{b=L+1}^B \hat{f}^b(x)
$$
