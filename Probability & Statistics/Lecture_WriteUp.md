# 📚 Short Write-Up: Key Concepts in Probability and Statistics for Machine Learning

## Probability and Statistics in ML

In machine learning, probability provides a formal framework for reasoning about uncertainty, while statistics helps us infer patterns from data. Data is often modeled as the outcome of a random process, enabling the application of probabilistic tools for prediction and inference.

---

## Prediction with Uncertainty

Unlike deterministic systems, ML models produce **probabilistic outputs**, capturing **uncertainty** in predictions. This is vital in applications where understanding the **confidence** of predictions is as important as the predictions themselves (e.g., medical diagnosis, autonomous driving).

---

## Random Variables & Distributions

A **random variable (RV)** is a quantity with an uncertain outcome:

- **Discrete RV**: e.g., number of heads in 3 coin tosses.
- **Continuous RV**: e.g., height of individuals.

Each RV is associated with a distribution:

- **PMF (Probability Mass Function)** for discrete RVs:
  ```
  P(X = x)
  ```
- **PDF (Probability Density Function)** for continuous RVs:
  ```
  f(x) such that P(a ≤ X ≤ b) = ∫[a to b] f(x) dx
  ```

---

## Joint Distribution

The **joint distribution** of two or more RVs describes the probability of their outcomes **occurring together**:

```
P(X = x, Y = y)
```

Or for continuous:

```
f(x, y)
```

---

## Marginal Probability

The **marginal** is the probability of a subset of variables, obtained by summing (discrete) or integrating (continuous) over the others:

- Discrete:
  ```
  P(X = x) = ∑ P(X = x, Y = y)
  ```
- Continuous:
  ```
  f_X(x) = ∫ f(x, y) dy
  ```

---

## Multivariate Gaussian Distribution

A generalization of the normal distribution to multiple variables. Defined by:

- **Mean vector** μ
- **Covariance matrix** Σ

Probability density function:

```
f(x) = (1 / ((2π)^(k/2) |Σ|^(1/2))) * exp( -0.5 * (x - μ)^T Σ⁻¹ (x - μ) )
```

---

## Marginal in Multivariate Gaussian

Any subset of a multivariate Gaussian is also Gaussian. The **marginal** distribution is obtained by selecting the corresponding subvector of **μ** and submatrix of **Σ**.

---

## Conditional Probability

The probability of an event **A given B**:

```
P(A | B) = P(A, B) / P(B)
```

(assuming P(B) > 0)

---

## Chain Rule

Breaks down joint probability into conditionals:

```
P(A, B, C) = P(A) * P(B | A) * P(C | A, B)
```

---

## Expectation, Independence, Variance

- **Expectation**:  
  Discrete:

  ```
  E[X] = ∑ x * P(X = x)
  ```

  Continuous:

  ```
  E[X] = ∫ x * f(x) dx
  ```

- **Variance**:

  ```
  Var(X) = E[(X - E[X])²]
  ```

- **Independence**:
  ```
  P(A, B) = P(A) * P(B)
  ```

---

## Covariance and Covariance Matrix

- **Covariance**:

  ```
  Cov(X, Y) = E[(X - μ_X)(Y - μ_Y)]
  ```

- **Covariance Matrix (Σ)**:  
  For vector X = [X₁, X₂, ..., Xₙ]ᵗ:
  ```
  Σᵢⱼ = Cov(Xᵢ, Xⱼ)
  ```

---

## Correlation, Empirical Mean & Covariance

- **Correlation** (standardized covariance):

  ```
  Corr(X, Y) = Cov(X, Y) / (σ_X * σ_Y)
  ```

- **Empirical Mean** (from data):

  ```
  μ̂ = (1/n) ∑ xᵢ
  ```

- **Empirical Covariance**:
  ```
  Σ̂ = (1/n) ∑ (xᵢ - μ̂)(xᵢ - μ̂)ᵗ
  ```
