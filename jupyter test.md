```python
import pandas as pd
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
```

```python
def f(x):
    curve = np.sin(x) + np.cos(2*x) + np.cos(x) * np.sin(2*x)
    return curve

def make_curve():
    x = np.linspace(-4, 4, 1000)
    y = f(x)
    return x, y

def plot_curve():
    x, y = make_curve()
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.plot(x, y)
    ax.axvline(0, ls='--', color='black')
    ax.axhline(0, ls='--', color='black')
    plt.show()

plot_curve()
```
