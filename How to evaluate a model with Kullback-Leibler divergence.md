## Practical steps:

1. Obtain $P(x)$ by computing empirical probabilities from the test set.
2. Use the model to get $Q(x)$ for the same instances.
3. Calculate $D_{KL}(P||Q)$

- The lower the KL divergence, the better the model has fit the test data distribution.
- High values indicate poor fit and may suggest overfitting or underfitting.

- KL divergence can serve as an additional performance metric alongside others like AUC-ROC, RMSE, etc., to holistically evaluate your model's predictive power.
- Particularly useful when you care about the predicted probability distribution, not just the labels.

```python
import numpy as np
from scipy.stats import entropy

def kl_divergence(y_true, y_pred):
    # Calculate empirical probabilities
    unique, counts = np.unique(y_true, return_counts=True)
    p = counts / len(y_true)

    # Calculate model's predicted probabilities for these
	# unique labels
    q = np.mean(y_pred[np.isin(y_true, unique)], axis=0)

    # Compute KL divergence
    kl = entropy(p, q)

    return kl

# Example usage
y_true = np.array([0, 0, 1, 1, 1, 2, 2])  # True labels
y_pred = np.array([[0.7, 0.2, 0.1],       # Predicted probabilities for each class
                   [0.8, 0.1, 0.1],
                   [0.2, 0.7, 0.1],
                   [0.3, 0.6, 0.1],
                   [0.1, 0.7, 0.2],
                   [0.1, 0.3, 0.6],
                   [0.2, 0.2, 0.6]])

kl_result = kl_divergence(y_true, y_pred)
print(f"KL Divergence: {kl_result}")
```
