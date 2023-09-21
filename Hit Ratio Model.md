[[Small Business]] [[Predictive Modeling]]
## 2023-08-16
- is there a #survival-curve that can be implemented over the whole dataset?
	- eg over time as a quote just sits out there how likely is it to be accepted?

- binary target - hit/not hit
- several of the predictors in the dataset won't be available at the time this model runs
    - try to isolate/find variables that aren't going to depend on whether or not there has been a quote/policy written
    - use econ data from fred
        - decision to purchase is at least partly a function of the general economic environment
        - or maybe economic factors influence the price they are willing to pay?
- using [[XGBoost]] [^1](probably) assuming it performs the best
    - if there is a [[Time series|time series]] structure could benefit from [[Neural Networks|neural network]]?
    - also have `lightgbm` and `catboost` available, as well as `pytorch` and `pyro` [[Pyro]]

## 2023/08/16

- working on class structure for data processing
- maybe just make sure `s_fmt` gets calculated and binary is good to go??
- I think this part is finished
    - now I just need the workflow for univariate analysis

## 2023/08/17
[[EDA should be consistent based on the type of predictor and target]]
[[Metrics should be focused on the ultimate aim of the model]]

- got >99.5% #roc-auc on the `cancer` dataset
	- used degree-5 polynomial transform
		- + log transform
		- + power transform
		- + discretizer
	- fit all 100K features to a univatiate [[Logistic Regression|logistic regression]] model
	- kept the 100 features with best [[k-fold Cross Validation|cross validation]] [[Mean Squared Error (MSE)|MSE]] 
	- fit [[XGBoost]] model
	- got feature importance from [[XGBoost]] after #grid-search 
	- this left ~15 or so variables remaining from original 100K
	- bada bing bada boom
[[Models do not perform well unless they perform well on unseen data]]

### 2023/08/16
- [[featuretools likes data to be split into many connected tables]] 

[[Meeting with Dan P - 23-08-18]]

[[PyTorch code to fit an embedding to BOP classification codes]]



[^1]: [[Boosting]] [[Boosting measures the importance of variables]] 