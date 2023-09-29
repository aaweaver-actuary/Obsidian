
## Test statistic

- To test $H_0: E[X] = 0$ for some random variable $X$, one approach is to construct a test statistic of the form:
    $$
    W = \frac{X-E[X]}{\sqrt{\text{Var}(X)}} \hspace{20em}
    $$
- In order to construct the [[The Log Rank Test|log rank]] test statistic, we compute a quantity that takes this form, with $X=\sum_{k=1}^K q_{1k}$
- Resulting test statistic:
    $$
    \begin{align}
    W =& \space \frac{\sum_{k=1}^K \left(q_{1k} -  E[q_{1k}]\right)}{\sqrt{\sum_{k=1}^K \text{Var}(q_{1k})}} \\
    =& \space \frac{\sum_{k=1}^K \left( q_{1k} - \frac{q_k}{r_k}r_{1k} \right)}{\sqrt{\sum_{k=1}^K \frac{q_k(r_{1k} / r_k)(1- r_{1k} / r_k)(r_k - q_k)}{r_k - 1}}}
    \end{align} \hspace{15em}
    $$
- when the sample size is large, the [[The Log Rank Test|log rank]] test statistic has approximately $N(0,1)$ - standard normal distribution
- this can be used to compute a $p$-value for the null hypothesis that there is no difference between the survival curves in the two groups

### idea we are trying to get at with this test statistic:

- on average, is the number of people in group 1 we see die more or less than we would expect if the two groups were the same?