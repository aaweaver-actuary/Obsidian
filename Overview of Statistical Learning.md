## 2.1 Linear Regression

## 2.2 Nearest Neighbors
* #nearest-neighbors can be pretty good for small $p$
  * eg $p \le 4$ and large $N$
  * will discuss clever/smoother versions (kernel, spline smoothing) later
* NN methods can be really bad when $p$ is large
  * #curse-of-dimensionality
    * NN tend to be far away in very high dimensions

## 2.3 Parametric & structured models
* the **linear** model is an example of a **parametric** model:
  * $f_L(X) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p$
* a linear model is specified in terms of $p+1$ parameters $\beta_0, \dots, \beta_p$
* estimate the parameters by fitting the model to the training data
* although it is almost never correct, a #linear-model often serves as a good and interpretable approximation to the unknown true function $f(X)$

## 2.4 Trade-offs:
[[Trade-offs in statistical learning]]

## 2.5 Assessing Model Accuracy

We fit $\hat{f}(x)$ to some training data $\text{Tr}=\{ x_i, y_i\}_{i=1}^N$ and we want to see how well $\hat{f}(x)$ performs on a test data set $\text{Te}=\{ x_i, y_i\}_{i=1}^N$:  

* we could compute the **average squared prediction error** on the *training data*:  
	* $\text{MSE}_{\text{Tr}}=\frac{1}{N}\sum_{i=1}^N(y_i-\hat{f}(x_i))^2$
	- this may be biased towards models that are too flexible/overfit the data  

* instead, we should compute the average squared prediction error on the *test data*:  
    * $\text{MSE}_{\text{Te}}=\frac{1}{N}\sum_{i=1}^N(y_i-\hat{f}(x_i))^2$
    * this may be #bias'ed towards models that are too inflexible/underfit the data

## 2.6 Bias-variance trade-off

[[Bias-variance trade-off in statistical learning]]

## 2.7 Classification problems

* here the response variable $Y$ is qualitative
    * e.g. $Y$ is #binary (e.g. spam/not spam)
    * e.g. digit class is one of 0,1,2,...,9

* our goal:
    * build a classifier $C(X)$ that assigns a class label from $\mathcal{G}$ to each observation $X$
    * assess the uncertainty associated with that prediction
    * understand the roles of the different predictors among $X_1, X_2, ..., X_p$

### 2.7.1 Bayes optimal classifier
[[the Bayes optimal classifier is the one that assigns each observation to the most likely class, given its predictor values]]

## 2.8 Classification details
* usually we measure the performance of $\hat{C}$ using the **misclassification error rate**:  
    * $\text{Err}_{\text{Te}} = \text{Ave}_{i\in \text{Te}} I(y_i \neq \hat{C}(x_i))$
    * the Bayes classifier has the lowest possible error rate, called the **Bayes error rate**.
        * only true when the Bayes classifier is known, which is usually not the case.

* later in the course:
    * SVM's build structured models for $C$ that attempt to minimize the error rate.
    * we will also build structured models for $p_k(x)$, such as logistic regression and generalized additive models.

## 2.9 Summary
* **k-nearest neighbors** is a simple and effective method for classification.
    * in about 1/3 of the problems we will encounter, it will be about as accurate as the best methods.

