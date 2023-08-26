

## #case-control-sampling and #logistic-regression

- In SA heart disease data, we have 160 cases and 302 controls, so $\tilde{\pi} = 0.346$, but the true $\pi$ is 0.5.
- With case-control sampling, we can estimate the #regression #coefficient's $\beta_j$ accurately, but the #intercept $\beta_0$ is #biased.
  - Note that this depends on our having defined the model correctly.
- we can correct the estimated #intercept by adding $\log(\tilde{\pi}/(1-\tilde{\pi}))$ to the estimated #intercept:
  $$
  \hat{\beta}_0^* = \hat{\beta}_0
  $$
$$
\begin{align}
\log & \frac{\tilde{\pi}}{1-\tilde{\pi}}=\\
\log &\frac{\pi}{1-\pi}
\end{align}
$$


- often cases are rare, so $\tilde{\pi}$ is small, and the #bias is large.
  - up to 5 times larger than the #standard-error of the #intercept estimate.
  - **THIS MEANS** that you will get similar results studying a 5:1 ratio of controls to cases as you would studying a 1:1 ratio of controls to cases?