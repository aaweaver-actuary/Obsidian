[[Statistical Learning Lectures]]

# Bagging
- **Bagging** is an abbreviation for **bootstrap aggregation**.
    - [[Resampling Methods#5.8 The bootstrap|The bootstrap]] is normally used to estimate standard errors of parameter estimates.
    - In bagging, we use the bootstrap to generate a lot of different training data sets, which reduces the variance of our model.
- Bagging is a general-purpose procedure for reducing the variance of a statistical learning method.
    - It is introduced here because it is a particularly useful and frequently used in the context of [[8. Tree-Based Methods#8.1 Tree-based Methods|decision trees]].
- Recall that given a set of $n$ independent observations $Z_1, Z_2, \dots, Z_n$, each with variance $\sigma^2$, the variance of the mean $\bar{Z}$ of the observations is given by $\sigma^2/n$.
- In other words, averaging a set of observations reduces variance.
    - This is not practical because we generally don't have multiple training sets available.
    - For [[8. Tree-Based Methods|decision trees]], we can generate additional bootstrapped training sets by repeatedly sampling observations from the original training set with replacement.
- Since we don't have multiple training sets, we can bootstrap, by taking repeated samples from the (single) training data set.
    - In this way, we can generate $B$ different bootstrapped training data sets.
    - We then train our method on the $b$th bootstrapped training set in order to get $\hat{f}^{*b}(x)$, the prediction at point $x$
    - We finally average all the predictions, to obtain:
        $$
        \hat{f}_{\text{bag}}(x) = \frac{1}{B} \sum_{b=1}^B \hat{f}^{*b}(x)
        $$
        - This is called **bagging**.
- We don't need to worry about pruning the trees since bagging is a way to reduce the variance of a statistical learning method
    - It is this variance reduction that makes bagging so useful in improving the performance of many statistical learning methods.

# Bagging classification trees

- For classification trees: for each test observation:
    1. We can record the class predicted by each of the $B$ trees, and take a majority vote
    2. The overall prediction is the most commonly occurring class among the $B$ predictions.

# Out-of-Bag Error Estimation

- It turns out that there is a very straightforward way to estimate the test error of a bagged model, without the need to perform cross-validation or the validation set approach.
- Recall that the key to bagging is that trees are repeatedly fit to bootstrapped subsets of the observations.
    - On average, each bagged tree makes use of around two-thirds of the observations.
    - The remaining one-third of the observations not used to fit a given bagged tree are referred to as the **out-of-bag (OOB)** observations.
- We can predict the response for the $i$th observation using each of the trees in which that observation was OOB.
    - This will yield around $B/3$ predictions for the $i$th observation.
    - In order to obtain a single prediction for the $i$th observation, we can average these predicted responses (if regression) or can take a majority vote (if classification).
- This estimate is essentially the LOO CV error for bagging if $B$ is sufficiently large.
