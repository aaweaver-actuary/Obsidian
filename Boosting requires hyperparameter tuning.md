#boosting #statistical-learning 

1. The number of #trees $B$
   - Unlike [[Bagging|bagging]] and [[Random forests|random forests]], [[Boosting|boosting]] can #overfit if $B$ is too large.
   - This #overfitting tends to occur slowly if at all.
   - We use cross validation to select $B$ ([[Use cross validation to select hyperparameters]])
2. The #shrinkage-parameter $\lambda > 0$ 
   - $\lambda$ is a small positive number
   - $\lambda$ controls the rate at which #boosting learns
   - typical values are 0.01 or 0.001, but the right choice can depend on the problem
   - Very small $\lambda$ can require using a very large value of $B$ in order to achieve good performance
3. The number of splits $d$ in each #tree
   - controls the complexity of the #boosted #ensemble
   - a typical #hyperparameter grid would search $d=1,2,4,8$ ([[Use cross validation to select hyperparameters]])
   - often $d=1$ works well
	   - in this case each #tree is a #stump, consisting of a single split and resulting in an #additive-model
   - more generally, $d$ is the *interaction depth*, and controls the #interaction order of the #boosted model
	   - since $d$ splits can involve at most $d$ variables