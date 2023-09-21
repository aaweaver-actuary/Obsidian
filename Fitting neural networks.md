[[Deep Learning]] 

For even a simple [[Neural Networks|neural network]] this is complicated. Want to learn #weight's and [[Bias|biases]] based on minimizing [[Total Sum of Squares (TSS)|total sum of squares]]:
$$
\min_{\{w_k \}_1^K, \beta} \frac{1}{2}\sum_{i=1}^n \left( y_i - f(x_i)\right)^2 \hspace{18em}
$$
where
$$
f(x_i) = \beta_0 + \sum_{k=1}^K \beta_k g\left( w_{k0} + \sum_{j=1}^p w_{kj} x_{ij}\right)
$$
This problem turns out to be very difficult, because of the [[Non-convex objective function]]

Can fit with [[Gradient Descent]]

[[Gradients and Backpropagation]]

[[Tricks of the trade in gradient descent]]


