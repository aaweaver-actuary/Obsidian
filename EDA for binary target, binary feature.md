#eda #binary-target #binary-feature

## #descriptive-statistics
1. average target rate for both classes of the feature
2. summarize cross-tab ( #confusion-matrix )

## #visualizations
1. Plot #bar-charts to show the distribution of both classes for each #binary-feature
   ([[Binary classification training data should be balanced]])
2. Draw #mosaic-plots to represent the relationship between the #binary-feature and the #binary-target variable.
3. 

## #association-measures

1. Compute [[Point-Biserial Correlation]] to measure the relationship between #binary-feature and #binary-target.
2. Conduct [[Chi-Squared tests for independence]] between each #binary-feature and #binary-target.

- **Information Value & WoE (Weight of Evidence)**
    
    - Calculate Information Value to gauge predictive power.
    - Compute WoE to understand the relationship between the feature and the target.
- **ANOVA (Analysis of Variance)**
    
    - Apply to evaluate the significance of the relationship between binary features and the target.
- **Machine Learning Metrics (optional)**
    
    - Utilize AUC-ROC, Precision, Recall, F1-Score by training simple models on each feature to evaluate their predictive power.
- **Multicollinearity Checks**
    
    - Check for high correlations between binary features if considering multiple features simultaneously.
- **Sensitivity Analysis (optional)**
    
    - Run models with and without the feature and compare performance metrics to see if the feature is adding value.
- **Automated Reporting**
    
    - Consolidate results in a dashboard or a report with visuals and key statistics.