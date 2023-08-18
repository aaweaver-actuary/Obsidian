* compute the #residual-standard-error  #RSE, which is an estimate of the #standard-deviation of $\epsilon$:
$$
\text{RSE} = \sqrt{\frac{1}{n-2}\text{RSS}} = \sqrt{\frac{1}{n-2}\sum_{i=1}^n (y_i-\hat{y}_i)^2}
$$
* where the #residual-sum-of-squares #RSS  is $\text{RSS} = \sum_{i=1}^n (y_i-\hat{y}_i)^2$.
* #R-squared, or fraction of variance explained by the model, is defined as
$$
R^2 = \frac{\text{TSS}-\text{RSS}}{\text{TSS}} = 1 - \frac{\text{RSS}}{\text{TSS}}
$$
* where the #total-sum-of-squares #TSS is $\text{TSS} = \sum_{i=1}^n (y_i-\bar{y})^2$.
* it can be shown that in this simple #linear-regression setting that $R^2 = \text{cor}(x,y)^2 = r^2$:

$$

\sqrt{R^2} = \text{cor}(x,y) = r = \frac{\sum_{i=1}^n (x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_{i=1}^n (x_i-\bar{x})^2\sum_{i=1}^n (y_i-\bar{y})^2}}

$$