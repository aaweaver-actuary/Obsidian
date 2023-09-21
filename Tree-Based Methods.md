[[Tree-Based Methods - Intro]]

# 8.2 More details on trees

## 8.2.1 Predictions

* We predict the response for a given test observation using the mean of the training observations in the region to which that test observation belongs.

## 8.2.2 Tree Pruning

* When growing a tree, could ask, "how big should we grow the tree?"
    * At one extreme, we could grow a very large tree, until each region contains only a single observation.
    * This will create a tree with perfect fit to the training data, but likely overfits the data, leading to poor test set performance.
* The process described above may produce good predictions on the training set, but is likely to overfit the data, leading to poor test set performance.
* A smaller tree with fewer splits (that is, fewer regions $R_1$, $R_2$, ..., $R_J$) might lead to lower [[Variance|variance]] and better interpretation at the cost of a little [[Bias|bias]].
* One possible alternative to the process described above is to grow the tree only so long as the decrease in the [[Residual Sum of Squares (RSS)|RSS]] due to each split exceeds some (high) threshold.
* This strategy will result in smaller trees, but is likely to be too **conservative** in the sense that it may not capture important structure in the data:
    * A seemingly worthless split early on in the tree might lead to a very good split later on (meaning that the early split should have been included).
    * This is called **early stopping**.
* A better strategy is to grow a very large tree $T_0$, and then **prune** it back in order to obtain a **subtree**.
* The idea is to use a **cost complexity** criterion to seek a subtree that leads to the lowest test error rate.
    * Also called **weakest link pruning** or **minimal cost complexity pruning**.
* We consider a sequence of trees indexed by a nonnegative tuning parameter $\alpha$.
* For each value of $\alpha$ there corresponds a subtree $T \subset T_0$ such that
$$
\sum_{m=1}^{|T|} \sum_{i:x_i \in R_m} (y_i - \hat{y}_{R_m})^2 + \alpha |T|
$$
* is as small as possible.
* Here $|T|$ indicates the number of terminal nodes of the tree $T$
* $R_m$ is the rectangle (i.e. the subset of predictor space) corresponding to the $m$th terminal node
* $\hat{y}_{R_m}$ is the mean response for the training observations in $R_m$.
* $\alpha|T|$ is a [[Complexity|complexity penalty]] that is a function of the number of terminal nodes of the tree, $|T|$.
    * This is very much like [[The Lasso for regularization|the lasso]], where we had a sum of squares penalty that was a function of the absolute size of the regression coefficients.

### Choosing the best subtree

* The tuning parameter $\alpha$ controls a trade-off between the subtree's **complexity** and its **fit to the training data**.
* We select an optimal value of $\widehat{\alpha}$ using **cross-validation**
* We then return the subtree corresponding to the chosen value of $\widehat{\alpha}$.

### Summary - Tree Algorithm

1. Use #recursive-binary-splitting to grow a large [[Tree-Based Methods|tree]] on the training data, stopping only when each [[Terminal nodes represent the prediction regions in a decision tree|terminal node]] has fewer than some minimum number of observations.
2. Apply [[Cost Complexity Pruning|cost complexity pruning]] to the large [[Tree-Based Methods|tree]] in order to obtain a sequence of best subtrees, as a function of $\alpha$
3. Use [[k-fold Cross Validation|k-fold cross-validation]] [[Use cross validation to select hyperparameters|to choose]] $\alpha$. Divide the training observations into $k$ folds. For each $k = 1, 2, ..., K$:
    * Repeat Steps 1 and 2 on all but the $k$th fold of the training data.
    * Evaluate the [[Mean Squared Error (MSE)|mean squared prediction error]] on the data in the left-out $k$th fold, as a function of $\alpha$.
    * Average the results for each value of $\alpha$, and pick $\widehat{\alpha}$ to minimize the average error.
4. Return the subtree from Step 2 that corresponds to the chosen value of $\widehat{\alpha}$.

## 8.2.3 Classification Trees

* Very similar to [[Regression|regression]] trees, except that it is used to predict a qualitative response rather than a quantitative one.
* For a [[Classification|classification]] tree, we predict that each observation belongs to the most commonly occurring class of training observations in the region to which it belongs.
  
### Details of classification trees

* Just as in the [[Regression|regression]] setting, we use [[Recursive Binary Splitting|recursive binary splitting]] to grow a [[Classification|classification]] [[Tree-Based Methods|tree]].[^4]
* In the [[Classification|classification]] setting, [[Residual Sum of Squares (RSS)|RSS]] cannot be used as a criterion for making the binary splits.
* A natural alternative to [[Residual Sum of Squares (RSS)|RSS]] is the **[[Classification|classification]] error rate**.
    * This is simply the fraction of the training observations in that region that do not belong to the most common class:    $$
    E = 1 - \max_k(\hat{p}_{mk})
    $$
    * Here $\hat{p}_{mk}$ represents the proportion of training observations in the $m$th region that are from the $k$th class.
* However the classification error rate is not sufficiently sensitive for tree-growing, and in practice two other measures are preferable.
    * It is jumpy and noisy, in the sense that a small change in the data can cause a large change in the error rate.
    * Does not lead to a smooth tree-growing process.

### Gini Index and Deviance

* [[The Gini Index|The Gini index]] is defined by$$
    G = \sum_{k=1}^K \hat{p}_{mk}(1 - \hat{p}_{mk})
    $$
    and is a measure of total variance across the $K$ classes.
    * Also note the similarity to the variance formula for a binomial random variable.
    * It turns out you are summing over the diagonal of the variance-covariance matrix.
* [[The Gini Index|The Gini index]] takes on a small value if all of the $\hat{p}_{mk}$'s are close to zero or one.
    * At one extreme, if $\hat{p}_{mk} = 1$ for each $k$ then each term will be $1 \cdot (1 - 1) = 0$ and the Gini index will attain its minimum value of zero.
* For this reason the Gini index is referred to as a measure of **node purity**
    * a small value indicates that a node contains predominantly observations from a single class.
* An alternative to the Gini index is **cross-entropy** or **deviance**, given by

    $$
    D = -\sum_{k=1}^K \hat{p}_{mk} \log \hat{p}_{mk}
    $$
    * This time there is a similarity to the binomial **log-likelihood.**
    * Cross-entropy will take on a value near zero if the $\hat{p}_{mk}$'s are all near zero or near one.
    * Hence, like the Gini index, the cross-entropy will take on a small value if the $m$th node is pure.
* It turns out that the Gini index and the cross-entropy are quite similar numerically.
    * For this reason, in practice the classification error rate is usually replaced by one of these two measures when constructing a decision tree.

* Once you have your tree, it gets pruned in the same way as the regression tree -- using cross-validation with a cost-complexity criterion.

## 8.2.4 Trees Versus Linear Models

* Trees aren't always the right thing to do.
    * Trees always pick box-shaped regions.
    * If your decision boundary is not box-shaped, then trees will not work well.

## 8.2.5 Advantages and Disadvantages of Trees

* **PRO:** [[Trees are very easy to explain to people.]] #interpretability 
    * In fact, they are even easier to explain than [[Linear Regression|linear regression]] 
* **PRO:** Some people believe that decision trees more closely mirror human decision-making than do the [[Regression|regression]] and [[Classification|classification]] approaches discussed in [[Classification|chapter 4]] and [[Resampling Methods|chapter 5]].
* **PRO:** [[Trees can be displayed graphically, and are easily interpreted even by a non-expert (especially if they are small).]]
* **PRO:** [[Trees can easily handle qualitative predictors without the need to create dummy variables.]]
* **CON:** [[Unfortunately, trees generally do not have the same level of predictive accuracy as some of the other regression and classification approaches seen in this book.]]

* However, by aggregating many decision trees, using methods like [[Bagging|bagging]], [[Random Forests|random forests]], and [[Boosting|boosting]], the predictive performance of [[Tree-Based Methods|trees]] can be substantially improved.
* We consider these approaches in the next section.

[^1]: [[Terminal nodes represent the prediction regions in a decision tree]]
[^2]: [[Internal nodes are the splits inside a decision tree before the terminal node]]
[^3]: [[The predictor space is the set of possible values for X_1, X_2, ..., X_p]]