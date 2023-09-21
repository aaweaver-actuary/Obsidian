
* the **bootstrap** is a flexible and powerful statistical tool that can be used to quantify the uncertainty associated with a given estimator or statistical learning method
* for example, it can provide an estimate of the standard error of a coefficient, or a confidence interval for that coefficient

## 5.8.1 More about the bootstrap
* in more complex data situations, figuring out the appropriate way to generate bootstrap samples can require some thought
* for example, if the data are time series, we can't simply sample the observations with replacement
    * the data are not independent
    * we expect the value at time $t$ to be correlated to the value at time $t-1$
    * we can use **block bootstrap** to deal with this
        * we divide the data into blocks of consecutive observations
        * we then sample blocks with replacement
    * ultimately we have to sample things that are uncorrelated

## 5.8.2 Other uses of the bootstrap
* primarily used to find standard errors of an estimator
* also provides approximate confidence intervals for a population parameter
    * take the 2.5th and 97.5th percentiles of the bootstrap distribution to obtain a 95% confidence interval
    * this is called the **percentile method**
* **interpretation of a confidence interval:** if we were to repeat the data collection and analysis 100 times, then 95 of the resulting confidence intervals would contain the true unknown value of the parameter

## 5.8.3 Can the bootstrap estimate prediction error?
* in cross validation, each of the $K$ validation folds is distinct from the other $K-1$ folds used for training: **they are non-overlapping**
    * this is critical to the success of cross validation
* to estimate prediction error using the bootstrap, we could think about using each bootstrap dataset as our training set, and the original observations as our test set
    * but this is **wrong**
* each bootstrap sample has significant overlap with the original data
    * about 2/3 of the original data are in each bootstrap sample
    * this means that the bootstrap estimate of prediction error will be far too optimistic

### 5.8.3.1 Removing the overlap
* can partly fix this problem by only using the predictions for those observations that did not (*by chance*) occur in the current bootstrap sample
* this is called the **out-of-bag** (OOB) error estimate
* this gets complicated, and in the end, [[k-fold Cross Validation|cross validation]] provides a simpler, more direct approach to estimating the [[Testing Error|test error]] rate
* **the view of the authors:** for this particular problem, [[The Bootstrap|the bootstrap]] is not the best approach
    * [[k-fold Cross Validation|Cross validation]] is a better technique for estimating the [[Testing Error|test error]] rate