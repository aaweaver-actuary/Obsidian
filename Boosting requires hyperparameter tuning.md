

1. The number of [[Tree-Based Methods|trees]] $B$
    - Unlike [[Bagging|bagging]] and [[Random Forests|random forests]], [[Boosting|boosting]] can overfit if $B$ is too large.
    - This [[Overfitting|overfitting]] tends to occur slowly if at all.
    - We use [[Use cross validation to select hyperparameters|use cross-validation]] to select $B$
2. The #shrinkage-parameter $\lambda > 0$
    - $\lambda$ is a small positive number
    - $\lambda$ controls the rate at which [[Boosting]] learns
        - typical values are 0.01 or 0.001, but the right choice can depend on the problem
    - Very small $\lambda$ can require using a very large value of $B$ in order to achieve good performance
3. The number of splits $d$ in each [[Tree-Based Methods|tree]]
    - controls the complexity of the [[Boosting|boosting]] [[Ensemble Methods|ensemble]]
    - a typical #hyperparameter grid would search $d=1,2,4,8$ ([[Use cross validation to select hyperparameters]])
    - often $d=1$ works well
        - in this case each [[Tree-Based Methods|tree]] is a #stump, consisting of a single split and resulting in an [[Additive Models|additive model]]
    - more generally, $d$ is the _interaction depth_, and controls the #interaction order of the [[Boosting|boosting]] model
        - since $d$ splits can involve at most $d$ variables
