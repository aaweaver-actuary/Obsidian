- Let $\hat{y_i} = \hat{\beta}_0 + \hat{\beta}_1 x_i$ be the #prediction of $y_i$ based on the $i$th value of $X$.
    * then $e_i = y_i - \hat{y}_i$ represents the $i$th #residual
* We define the residual sum of squares #RSS as
    $$\text{RSS} = e_1^2 + e_2^2 + \cdots + e_n^2$$
    * $\text{RSS}$ is a measure of the lack of fit of the model to the data
    * $\text{RSS}$ should be as small as possible
* We can equivalently define #RSS as
$$\text{RSS} = (y_1 - \hat{\beta}_0 - \hat{\beta}_1x_1)^2 + (y_2 - \hat{\beta}_0 - \hat{\beta}_1x_2)^2 + \cdots + (y_n - \hat{\beta}_0 - \hat{\beta}_1x_n)^2$$
* The #least-squares approach chooses $\hat{\beta}_0$ and $\hat{\beta}_1$ to minimize the RSS.
* The minimizers are given by the **least squares coefficient estimates**:
$$
\hat{\beta}_1 = \frac{\sum_{i=1}^n (x_i-\bar{x})(y_i-\bar{y})}{\sum_{i=1}^n (x_i-\bar{x})^2}
$$
$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}
$$
* where $\bar{y} = \frac{1}{n}\sum_{i=1}^n y_i$ and $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$ are the #sample-means.