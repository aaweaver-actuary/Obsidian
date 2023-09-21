[[Boosting]] [[Regression]] #hyperparameter [[Tree-Based Methods]] [[The Bootstrap]] 

## What is the idea behind this procedure?

- Like [[Bagging|bagging]], [[Boosting|boosting]] is an approach that can be applied to many statistical learning methods for [[Regression|regression]] or [[Classification|classification]]
- We only discuss [[Boosting|boosting]] for [[Tree-Based Methods#8.1 Tree-based Methods|decision trees]]
- Recall that [[Bagging|bagging]] involves:
    1.  Creating multiple copies of the original training dataset using [[Resampling Methods#5.8 The bootstrap|the bootstrap]]
    2.  Fitting a separate [[Tree-Based Methods#8.1 Tree-based Methods|decision tree]] to each copy
    3.  Combining all the [[Tree-Based Methods|trees]] to create a single predictive model
- Notably, each [[Tree-Based Methods|tree]] is built on a [[The Bootstrap|bootstrapped]] data set, independent of the other [[Tree-Based Methods|trees]]
- [[Boosting]] works in a similar way, except the [[Tree-Based Methods|trees]] are grown _sequentially_:
    - each [[Tree-Based Methods|tree]] is grown using information from previously-grown [[Tree-Based Methods|trees]]

- Unlike fitting a single large decision [[Tree-Based Methods|tree]] to the data, which amounts to fitting the data hard and potentially #overfitting, boosting instead [[Overfitting is reduced by slower learning|learns slowly]]
- Given the current model, we fit a decision [[Tree-Based Methods|tree]] to the [[Residual|residuals]] from the model
- We then add this new decision [[Tree-Based Methods|tree]] into the fitted function in order to update the [[Residual|residuals]]
- Each of these [[Tree-Based Methods|trees]] can be rather small, with just a few [[Terminal nodes represent the prediction regions in a decision tree|terminal nodes]] determined by the parameter $d$ in the algorithm [^1]
- By fitting small [[Tree-Based Methods|trees]] to the [[Residual|residuals]], we slowly improve $\hat{f}$ in areas where it does not perform well
- The #shrinkage-parameter $\lambda$ slows the process down even more, allowing more and differently-shaped trees to attack the residuals

[^1]:[[Boosting algorithm for regression trees]] 