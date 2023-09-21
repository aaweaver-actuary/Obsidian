[[Survival Analysis]] #roc-auc

- This is an appealing method for assessing a fitted [[Cox Proportional Hazards Model]] on a test set
- For each observation we calculate the estimated risk score $$
  \hat{\eta}_i = \hat{\beta}_1 x_{i1} + \cdots + \hat{\beta}_p x_{ip}, \space \text{ for } i=1, 2, \dots, n \hspace{8em}
  $$Using the estimated [[Cox Proportional Hazards Model]] coefficients
- Then the #Harrell-concordance-index or #C-index computes the proportion of observation pairs for which $\hat{\eta}_{i'} > \hat{\eta}_i$ and $y_{i'} > y_i$: $$
C = \frac{\sum_{i, i': y_i > y_{i'}} I(\hat{\eta}_{i'} > \hat{\eta}_i) \cdot \delta_{i'}}{\sum_{i, i': y_i > y_{i'}}\delta_{i'}} \hspace{13em}
$$$\rightarrow$ This is the proportion of pairs for which the model gets the order of the operations right, eg the relative [[Survival Time|survival time]]

