### #logisitc-regression vs #linear-discriminant-analysis 

- for a two-class problem, one can show that for #linear-discriminant-analysis[^1] [^2]

  $$
  \begin{align}
  \log \left( \frac{p_1(x)}{1-p_1(x)} \right) =& \log \left( \frac{p_1(x)}{p_2(x)} \right) \\
  =& c_0 + c_1 x_1 + \dots + c_p x_p
  \end{align}
  $$

- so #linear-discriminant-analysis has the same form as #logistic-regression[^3]
- the difference is how the #parameter's are estimated
  - #logistic-regression uses the #conditional #likelihood based on $p(y|x)$
    - known as #discriminative-learning in a #machine-learning context
  - #linear-discriminant-analysis estimates the #parameter's by maximizing the #full-likelihood of the #parameter's given the data
    - known as #generative-learning in a #machine-learning context
  - in practice results are often very similar
- #linear-discriminant-analysis is more #stable when $n$ is small and the classes are #well-separated 
  - #logistic-regression can be #unstable in this case
- #linear-discriminant-analysis is more popular when $p$ is large and/or $n$ is small
  - #logistic-regression can easily #overfit 
- _footnote:_ #logistic-regression can also fit #quadratic #decision-boundaries by explicitly including #quadratic terms in the model

[^1]: [[Linear discriminant analysis when p=1]]
[^2]: [[Linear discriminant analysis when p is bigger than 1]]
[^3]: [[Logistic regression is linear regression on the log-odds]]