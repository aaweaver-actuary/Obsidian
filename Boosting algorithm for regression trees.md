[[Boosting]] [[Regression]] [[Tree-Based Methods]]


1. Set $\hat{f}(x)=0$ and $r_i=y_i$ for all $i$ in the training set
2. For $b=1, 2, \dots, B$, repeat:
    1. Fit a [[Tree-Based Methods|tree]] $\hat{f}^{b}$ with $d$ splits (so $d+1$ [[Terminal nodes represent the prediction regions in a decision tree|terminal nodes]]) to the training data $(X, r)$
    2. Update $\hat{f}$ by adding in a shrunken version of the new [[Tree-Based Methods|tree]]:
        $$
        \hat{f}(x)\leftarrow \hat{f}(x) + \lambda\hat{f}^b(x)
        $$
    3. Update the residuals:
        $$
        r_i \leftarrow r_i - \lambda\hat{f}^b(x_i)
        $$
3. Output the [[Boosting|boosted]] model:
    $$
    \hat{f}(x) = \sum_{b=1}^B \lambda \hat{f}^b(x)
    $$

- We basically keep fitting [[Tree-Based Methods|trees]] to the residuals, and so we improve the fit
- When each [[Tree-Based Methods|tree]] is added, it is shrunken by a factor of $\lambda$
- Unlike [[Random Forests|random forests]] and [[Bagging|bagging]], these [[Tree-Based Methods|trees]] are not independent:
    - the $i$th new [[Tree-Based Methods|tree]] $T_i$ is fit to the residuals of the previous $i-1$ [[Tree-Based Methods|trees]] $(T_0, \dots, T_{i-1})$