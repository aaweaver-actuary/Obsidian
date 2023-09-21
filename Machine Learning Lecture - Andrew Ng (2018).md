### [[Linear Regression]]

When designing an algorithm:

1. how do represent [[Machine Learning Hypothesis|hypothesis]] $h$?
   $\rightarrow h_{\theta}(x) = \theta_0 + \theta_1x$
   more generally $h_{\theta}(x) = \sum_{j=0}^p \theta_jx_j$, where $x_0=1$ is a dummy variable
    - $\theta$ - parameters
    - $m$ - number of training examples
    - $\left(x^{(i)}, y^{(i)}\right)$ - $i$th training example
    - $n$ - number of features for the learning problem
        - $x$ and $\theta$ are $(n+1)$-dimensional
2. Want to choose $\theta$ such that $h_{\theta}(x) \approx y$
    - minimize$$
      J(\theta) = \frac{1}{2}\sum*{j=1}^m \left[h*{\theta}\left( x^{(i)}, y^{(i)}\right) - y_i\right]
        $$
        $J(\theta)$ is the [[Loss Functions|cost function]]

 - turns out that [[Squared Error Loss Function|squared error]] implies [[Gaussian|Gaussian distribution]] in a [[Generalized linear models generalize linear regression to work on different types of responses|GLM]] context

### [[Gradient Descent]]

- start with initial $\theta = \vec{0}$ and refine
- at each step, find direction that decreases [[Gradient Vector|gradient]] the most and take a small step in that direction
- Algorithm:
	1. Update $\theta_{j}:$
 $$
 \theta_{j} := \theta_{j} - \alpha \frac{\partial}{\partial \theta_j} J(\theta)
 $$
	 - $\alpha$ - learning rate
 