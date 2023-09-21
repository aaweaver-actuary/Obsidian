[Wikipedia](https://en.wikipedia.org/wiki/Mallows%27s_Cp)

Used to assess the fit of [[Regression|regression]] models fit using [[Ordinary Least Squares (OLS)|OLS]].

- Small value of Mallow's Cp means the model is relatively precise
- Equivalent to [[Akaike Information Criterion (AIC)|AIC]] in the special case of [[Gaussian]] [[Linear Regression|linear regression]]

### Limitations:
1. $C_p$ approximation is only valid for large sample sizes
2. $C_p$ cannot handle complex collections of models 

### Calculation:

Note: this is a simpler version that gives somewhat different results but the overall same order. See the Wikipedia article
$$
C_p= \frac{1}{n} \left(\text{RSS} + 2p\hat{\sigma}^2\right)
$$
