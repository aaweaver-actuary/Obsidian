[[Survival Analysis]]

- Closely related to the [[Cox Proportional Hazards Model]][^1]
- Analogous to the #t-test, but for survival data
- Looking at two [[Kaplan-Meier]] curves
    - Suppose it looks like females survive longer than males
    - But sample size relatively small, so you want to know whether the difference is significant or not
    - Normally would look at a #t-test for this sort of thing, but [[Censored Data|censored]] data presents a [[Bias|bias]] issue

## Notation

- We let
    - $d_1 < d_2 < \cdots < d_K$ be the unique death times among the non [[Censored Data|censored]] patients
    - $r_k$ - number of patients at risk at time $d_k$
        - $r_{1k}, r_{2k}$ - number of patients from groups 1 and 2 who are at risk at time $d_k$
        - Note $r_k = r_{1k} + r_{2k}$
    - $q_k$ - number of patients who died at time $d_k$
        - $q_{1k}, q_{2k}$ - number of patients from groups 1 and 2 who died at time $d_k$
        - Note $q_k = q_{1k} + q_{2k}$

|           | Group 1         | Group 2         | Total     |
| --------- | --------------- | --------------- | --------- |
| Died      | $q_{1k}$        | $q_{2k}$        | $q_k$     |
| Survived  | $r_{1k}-q_{1k}$ | $r_{2k}-q_{2k}$ | $r_k-q_k$ |
| **Total** | $r_{1k}$        | $r_{2k}$        | $r_k$     |

- At each time of death $d_k$, we create a $2 \times 2$ table of counts for the form shown above
- if the death times are unique (eg no two individuals die at the same time), the one of $q_{1k}$ and $q_{2k}$ are 1 and the other is 0

[[Log Rank Test Statistic]]


[^1]: [[Cox Proportional Hazards Model]]
