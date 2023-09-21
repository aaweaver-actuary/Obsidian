

approaches are a little "ad-hoc":
1. **OVA** - #one-versus-all
   - Fit $K$ different 2-class [[Support Vector Classifier|support vector classifier]]  $\hat{f}_k(x)$, $k=1, \dots, K$; each class vs. the rest
   - Classify $x^*$ to the class for which $\hat{f}_k (x^*)$ is the largest 
   - Code the one class as 1, others as -1
2. **OVO** - #one-versus-one
   - Fit all $\binom{K}{2}$ pairwise classifiers $\hat{f}_{k\ell}(x)$
   - Classify $x^*$ to the class that wins the most pairwise competitions

which to choose?
if $K$ isn't too large to fit $\binom{K}{2}$ pairwise classifiers, use it
