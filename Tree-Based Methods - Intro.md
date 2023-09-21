* Here we describe tree methods for [[Regression]] and [[Classification]].
* These involve stratifying or segmenting the predictor space into a number of simple regions.
* Since the set of splitting rules used to segment the predictor space can be summarized in a tree, these types of approaches are known as **decision-tree methods**.

## 8.1.1 Pros and Cons
[[Decision trees are easy to understand, but do not perform competitively with other methods]]


## 8.1.2 The Basics of Decision Trees
* Can be applied to both [[Regression|regression]] and [[Classification|classification]] problems.
	* We first consider the case of [[Regression|regression]], then move on to [[Classification|classification]].
* In keeping with the [[Tree-Based Methods|tree]] analogy, the regions $R_1, R_2, \dots, R_J$ are called [[Terminal nodes represent the prediction regions in a decision tree|terminal nodes]] or **leaves** of the [[Tree-Based Methods|tree]].
* decision [[Tree-Based Methods|trees]] are usually drawn upside down, with the leaves at the bottom and the root at the top.
* The points along the [[Tree-Based Methods|tree]] where the predictor space is split are referred to as [[Internal nodes are the splits inside a decision tree before the terminal node|Internal Nodes]] of the [[Tree-Based Methods|tree]].

## 8.1.3 Details of the tree-building process
1. We divide the #predictor-space[^3]—that is, the set of possible values for $X_1$, $X_2$, ..., $X_p$—into $J$ distinct and non-overlapping regions, $R_1$, $R_2$, ..., $R_J$.
2. For every observation that falls into the region $R_j$, we make the same prediction, which is simply the **mean of the response values** for the training observations in $R_j$.

* In theory, the regions could have any shape.
    * However, we choose to divide the predictor space into high-dimensional rectangles, or boxes, for simplicity and for ease of interpretation of the resulting predictive model.
* The goal is to find boxes $R_1$, $R_2$, ..., $R_J$ that minimize the [[Residual Sum of Squares (RSS)|RSS]], given by

$$
\sum_{j=1}^J \sum_{i \in R_j} (y_i - \hat{y}_{R_j})^2
$$

where $\hat{y}_{R_j}$ is the mean response for the training observations within the $j$th box.

* Unfortunately, it is computationally infeasible to consider every possible partition of the feature space into $J$ boxes.
* For this reason, we take a top-down, #greedy approach that is known as #recursive-binary-splitting.
* The approach is **top-down** because it begins at the top of the [[Tree-Based Methods|tree]] (at which point all observations belong to a single region) and then successively splits the predictor space; each split is indicated via two new branches further down on the [[Tree-Based Methods|tree]].
* It is **greedy** because at each step of the [[Tree-Based Methods|tree]]-building process, the best split is made at that particular step, rather than looking ahead and picking a split that will lead to a better [[Tree-Based Methods|tree]] in some future step.

### Details - Continued

1. We first select the predictor $X_j$ and the cutpoint $s$ such that splitting the predictor space into the regions $\{X|X_j < s\}$ and $\{X|X_j \geq s\}$ leads to the greatest possible reduction in [[Residual Sum of Squares (RSS)|RSS]].
2. Next, we repeat the process, looking for the best predictor and best cutpoint in order to split the data further so as to minimize the [[Residual Sum of Squares (RSS)|RSS]] within each of the resulting regions.
3. However, this time, instead of splitting the entire predictor space, we split one of the two previously identified regions.
4. Again, we look to split one of the resulting regions further, so as to minimize the [[Residual Sum of Squares (RSS)|RSS]].
5. The process continues until a **stopping criterion** is reached.
   * For instance, we may continue until no region contains more than five observations.