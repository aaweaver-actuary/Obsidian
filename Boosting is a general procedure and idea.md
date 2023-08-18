#boosting #regression #hyperparameter #tree #bootstrap 

## What is the idea behind this procedure?

- Like [[Bagging|bagging]], #boosting is an approach that can be applied to many statistical learning methods for #regression or #classification
- We only discuss #boosting for [[8. Tree-Based Methods#8.1 Tree-based Methods|decision trees]]
- Recall that [[Bagging|bagging]] involves:
    1.  Creating multiple copies of the original training dataset using [[5. Resampling Methods#5.8 The bootstrap|the bootstrap]]
    2.  Fitting a separate [[8. Tree-Based Methods#8.1 Tree-based Methods|decision tree]] to each copy
    3.  Combining all the #trees to create a single predictive model
- Notably, each #tree is built on a #bootstrap data set, independent of the other #trees
- #boosting works in a similar way, except the #trees are grown _sequentially_:
    - each #tree is grown using information from previously-grown #trees

- Unlike fitting a single large decision #tree to the data, which amounts to fitting the data hard and potentially #overfitting, boosting instead learns **slowly** ([[Overfitting is reduced by slower learning]])
- Given the current model, we fit a decision #tree to the #residuals from the model
- We then add this new decision #tree into the fitted function in order to update the #residuals
- Each of these #trees can be rather small, with just a few terminal nodes determined by the parameter $d$ in the algorithm [^1]
- By fitting small #trees to the #residuals, we slowly improve $\hat{f}$ in areas where it does not perform well
- The #shrinkage-parameter $\lambda$ slows the process down even more, allowing more and differently-shaped trees to attack the residuals

[^1]:[[Boosting algorithm for regression trees]] 