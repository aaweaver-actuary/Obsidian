[[k-fold Cross Validation]] and [[The Bootstrap]]

- in this section we discuss two resampling methods that are used to assess the performance of a predictive model: [[k-fold Cross Validation|cross validation]] and [[The Bootstrap|the bootstrap]]
- these methods refit a model of interest to samples formed from the training data, in order to obtain additional information about the fitted model
- for example, these methods can be used to estimate the [[Testing Error|test set prediction error]] estimates
        _ [[Standard Deviation|standard deviation]] and [[Bias|bias]] of the coefficient estimates
        _ the relative importance of each predictor
        _ the optimal value of the tuning parameter in a [[Regularization|penalized model]]
        _ the degree of non-linearity in a nonlinear model
        _ the possible presence of interactions in a linear model
        _ the types of observations that have the largest impact on the fitted model

# 5.3 More on prediction error estimates

- **best solution:** a large designated test set. However, this is not always possible/available
- some methods make a mathematical adjustment to the [[Training Error|training error]] rate in order to estimate the [[Testing Error|testing error]] rate
        _ these include the [[Mallow's Cp]], [[Akaike Information Criterion (AIC)|AIC]], [[Bayesian Information Criterion (BIC)|BIC]], and #adjusted-R2 statistics
        _ discussed later in the course
- here we instead consider a class of methods that estimate the [[Testing Error|testing set error]] by _holding out_ a subset of the training observations from the fitting process, and then applying the statistical learning method to those held out observations

# 5.4 validation set approach

- here we randomly divide the available set of samples into two parts: a training set and a validation set or hold-out set
- the model is fit on the training set, and the fitted model is used to predict the responses for the observations in the validation set
- the resulting [[Validation Error|validation error]] rate, typically assessed using [[Mean Squared Error (MSE)|MSE]] in the case of a quantitative response, or [[Misclassification Rate|misclassification rate]] in the case of a qualitative response, provides an estimate of the [[Testing Error|test error]] rate

## 5.4.1 Drawbacks of validation set approach

- the [[Validation Error|validation set error]] rate can be highly variable, depending on precisely which observations are included in the training set and which observations are included in the validation set
- in the validation set approach, only a subset of the observations, those that are included in the training set rather than in the validation set, are used to fit the model
	- this suggests that the [[Validation Error|validation error]] rate may tend to overestimate the [[Testing Error|test error]] rate for the model fit on the entire data set

# 5.5 [[k-fold Cross Validation]]

# 5.6 [[k-fold Cross Validation|Cross validation]] on [[Classification|classification]] problems

- the same ideas apply, but the [[Mean Squared Error (MSE)|MSE]] is replaced by the misclassification error rate
- we divide the data into $K$ roughly equal-sized parts $C_1, C_2, \dots, C_K$
- $C_k$ denotes the indices of the observations in the $k$th part
- $n_k$ is the number of observations in the $k$th part
        \* if $n$ is a multiple of $K$, then $n_k = n/K$ for all $k$
- compute:
    $$
    \text{CV}_{(K)} = \sum_{k=1}^K \frac{n_k}{n}\cdot \text{Err}_k
    $$
- where $\text{Err}_k = \sum_{i\in C_k} I(y_i \neq \hat{y}_i) / n_k$
- the estimated [[Standard Deviation|standard deviation]] of $\text{CV}_{(K)}$ is given by:
    $$
    \widehat{\text{SE}} (\text{CV}_{(K)}) = \sqrt{\sum_{k=1}^K \left( \text{Err}_k - \overline{\text{Err}}_{k} \right)^2/(K-1)}
    $$
- this is a useful estimate, but strictly speaking, not quite valid
	- the reason is that the $K$ parts overlap, so the errors $\text{Err}_k$ are not independent
	- this means that the formula does not take into account the [[Correlation|correlation]] between the [[Training Error|training]] and [[Testing Error|validation errors]]
	- this can be fixed by using [[The Bootstrap|the bootstrap]]
- [[k-fold Cross Validation|Cross validation]] explicitly separates the training and validation sets

# 5.7 cross validation: right and wrong

### example

- suppose we have $n = 100$ observations, and we have 5000 feature to choose from, and want to predict a binary response
        _ we decide to take the 100 features that show the most strong [[Correlation|correlation]] with the response
        _ throw away the remaining 4900 features
        \* fit a [[Logistic Regression|logistic regression]][^1] model using the 100 features

### the wrong way

- how to get an estimate of the test error?
        _ can we just use [[k-fold Cross Validation|cross validation]] on the 100 features?
            _ no! this is **wrong**
            * this would ignore the fact that we used the entire data set *including the response* to select the 100 features
            * this is itself a form of training and must be included in the cross validation process
        _ it is easy to simulate realistic data with the class labels independent of the outcome
            _ then true test error is 50%
            \* but cross validation on the 100 features will give an estimate of 0% error
- this error happens all the time and has been published in top journals

### the right way

- we must apply cross validation to the entire process of feature selection and model fitting
        _ before doing anything, randomly divide the data into $K$ equal-sized parts
        _ we can now do whatever we want on the other $K-1$ parts
            _ select the 100 features that are most correlated with the response
            _ fit a [[Logistic Regression|logistic regression]] model using the 100 features

[[The Bootstrap]]

[^1]: [[Logistic regression is linear regression on the log-odds]]
