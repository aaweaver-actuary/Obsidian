# [[Statistical Learning Lectures]]

- Like [[Bagging|bagging]], boosting is an approach that can be applied to many statistical learning methods for regression or classification
- We only discuss boosting for [[8. Tree-Based Methods#8.1 Tree-based Methods|decision trees]]
- Recall that [[Bagging|bagging]] involves:
    1.  Creating multiple copies of the original training dataset using [[5. Resampling Methods#5.8 The bootstrap|the bootstrap]]
    2.  Fitting a separate [[8. Tree-Based Methods#8.1 Tree-based Methods|decision tree]] to each copy
    3.  Combining all the trees to create a single predictive model
- Notably, each tree is built on a [[5. Resampling Methods#5.8 The bootstrap|bootstrap]] data set, independent of the other trees
- **Boosting** works in a similar way, except the trees are grown _sequentially_:
    - each tree is grown using information from previously-grown trees

## Boosting algorithm for regression trees

1. Set $\hat{f}(x)=0$ and $r_i=y_i$ for all $i$ in the training set
2. For $b=1, 2, \dots, B$, repeat:
    1. Fit a tree $\hat{f}^{b}$ with $d$ splits (so $d+1$ terminal nodes) to the training data $(X, r)$
    2. Update $\hat{f}$ by adding in a shrunken version of the new tree:
        $$
        \hat{f}(x)\leftarrow \hat{f}(x) + \lambda\hat{f}^b(x)
        $$
    3. Update the residuals:
        $$
        r_i \leftarrow r_i - \lambda\hat{f}^b(x_i)
        $$
3. Output the **boosted** model:
    $$
    \hat{f}(x) = \sum_{b=1}^B \lambda \hat{f}^b(x)
    $$

- We basically keep fitting trees to the residuals, and so we improve the fit
- When each tree is added, it is shrunken by a factor of $\lambda$
- Unlike [[Random forests|random forests]] and [[Boosting|boosting]], these trees are not independent:
    - the $i$th new tree $T_i$ is fit to the residuals of the previous $i-1$ trees $(T_0, \dots, T_{i-1})$

## What is the idea behind this procedure?

- Unlike fitting a single large decision tree to the data, which amounts to \*fitting the data **hard\*** and potentially overfitting, boosting instead learns **slowly**
- Given the current model, we fit a decision tree to the residuals from the model
- We then add this new decision tree into the fitted function in order to update the residuals
- Each of these trees can be rather small, with just a few terminal nodes determined by the parameter $d$ in the algorithm
- By fitting small trees to the residuals, we slowly improve $\hat{f}$ in areas where it does not perform well
- The [[6. Linear Model Selection and Regularization#6.9 Shrinkage methods|shrinkage parameter]] $\lambda$ slows the process down even more, allowing more and differently-shaped trees to attack the residuals

## Boosting for classification

- Similar in spirit to boosting for regression, but a bit more complex

> [!info]
>
> -   Don't go into detail in [[Statistical Learning Lectures]] or in the [[Introduction to Statistical Learning]] book
> -   See [[Elements of Statistical Learning]], Ch10
