[[Survival Analysis]]

- Closely related to the [[Cox Proportional Hazards Model]][^1]
- Analogous to the #t-test, but for survival data
- Looking at two [[Kaplan-Meier]] curves
    - Suppose it looks like females survive longer than males
    - But sample size relatively small, so you want to know whether the difference is significant or not
    - Normally would look at a #t-test for this sort of thing, but #censored data presents a [[Bias|bias]] issue

## Notation

- We let
    - $d_1 < d_2 < \cdots < d_K$ be the unique death times among the #non-censored patients
    - $r_k$ - number of patients at risk at time $d_k$
        - $r_{1k}, r_{2k}$ - number of patients from groups 1 and 2 who are at risk at time $d_k$
        - Note $r_k = r_{1k} + r_{2k}$
    - $q_k$ - number of patients who died at time $d_k$
        - $q_{1k}, q_{2k}$ - number of patients from groups 1 and 2 who died at time $d_k$
        - Note $q_k = q_{1k} + q_{2k}$

|           | Group 1         | Group 2         | Total     |
| --------- | --------------- | --------------- | --------- |
| Died      | $q_{1k}$        | $q_{2k}$        | $q_k$     |
| Survived  | $r_{1k}-q_{1k}$ | $r_{2k}-q_{2k}$ | $r_k-q_k$ |
| **Total** | $r_{1k}$        | $r_{2k}$        | $r_k$     |

- At each time of death $d_k$, we create a $2 \times 2$ table of counts for the form shown above
- if the death times are unique (eg no two individuals die at the same time), the one of $q_{1k}$ and $q_{2k}$ are 1 and the other is 0

## Test statistic

- To test $H_0: E[X] = 0$ for some random variable $X$, one approach is to construct a #test-statistic of the form:
    $$
    W = \frac{X-E[X]}{\sqrt{\text{Var}(X)}} \hspace{20em}
    $$
- In order to construct the #log-rank test statistic, we compute a quantity that takes this form, with $X=\sum_{k=1}^K q_{1k}$
- Resulting test statistic:
    $$
    \begin{align}
    W =& \space \frac{\sum_{k=1}^K \left(q_{1k} -  E[q_{1k}]\right)}{\sqrt{\sum_{k=1}^K \text{Var}(q_{1k})}} \\
    =& \space \frac{\sum_{k=1}^K \left( q_{1k} - \frac{q_k}{r_k}r_{1k} \right)}{\sqrt{\sum_{k=1}^K \frac{q_k(r_{1k} / r_k)(1- r_{1k} / r_k)(r_k - q_k)}{r_k - 1}}}
    \end{align} \hspace{15em}
    $$
- when the sample size is large, the #log-rank test statistic has approximately $N(0,1)$ - #standard-normal distribution
- this can be used to compute a $p$-value for the null hypothesis that there is no difference between the survival curves in the two groups

### idea we are trying to get at with this test statistic:

- on average, is the number of people in group 1 we see die more or less than we would expect if the two groups were the same?

[^1]: [[Cox Proportional Hazards Model]]
