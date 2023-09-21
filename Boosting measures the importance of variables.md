[[Boosting]] 

- For [[Bagging|bagged]]/[[Random Forests|random forest]] [[Regression|regression]] [[Tree-Based Methods|trees]], we record the total amount that the [[Residual Sum of Squares (RSS)|RSS]] is decreased due to splits over a given predictor, averaged over all $B$ [[Tree-Based Methods|trees]]
	- A large value indicates an important predictor
- Do a similar thing by averaging the total amount the [[Gini Index]] is decreased by splits over a given predictor, averaged over all $B$ [[Tree-Based Methods|trees]]