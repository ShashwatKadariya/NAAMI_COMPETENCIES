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

## 📊 Types of Probability Distributions

In machine learning and statistics, different types of distributions model different kinds of data. Distributions can be broadly categorized into **discrete** and **continuous** types.

---

### 🔢 Discrete Distributions

#### 1. **Bernoulli Distribution**

- Models: A single trial with two outcomes (e.g., success/failure)
- Parameter: \( p \in [0, 1] \)
- PMF:
  ```
  P(X = x) = p^x (1 - p)^{1 - x}, where x ∈ {0,1}
  ```
- Example: Coin toss

#### 2. **Binomial Distribution**

- Models: Number of successes in \( n \) independent Bernoulli trials
- Parameters: \( n \) (number of trials), \( p \) (success probability)
- PMF:
  ```
  P(X = k) = C(n, k) * p^k * (1 - p)^{n - k}
  ```
- Example: Number of heads in 10 coin tosses

#### 3. **Poisson Distribution**

- Models: Number of events in a fixed interval of time/space
- Parameter: \( \lambda \) (average rate)
- PMF:
  ```
  P(X = k) = (λ^k * e^{-λ}) / k!
  ```
- Example: Number of emails received per hour

---

### 📈 Continuous Distributions

#### 4. **Uniform Distribution (Continuous)**

- Models: All outcomes are equally likely within an interval \([a, b]\)
- PDF:
  ```
  f(x) = 1 / (b - a), for x in [a, b]
  ```
- Example: Random number between 0 and 1

#### 5. **Normal (Gaussian) Distribution**

- Models: Symmetric, bell-shaped distribution around a mean
- Parameters: \( \mu \) (mean), \( \sigma^2 \) (variance)
- PDF:
  ```
  f(x) = (1 / √(2πσ²)) * exp(- (x - μ)² / (2σ²))
  ```
- Example: Height, exam scores

#### 6. **Exponential Distribution**

- Models: Time between events in a Poisson process
- Parameter: \( \lambda \)
- PDF:
  ```
  f(x) = λ * e^{-λx}, for x ≥ 0
  ```
- Example: Time between arrivals at a bus stop

---

### Summary Table

| Distribution | Type       | Use Case                         | Parameters          |
| ------------ | ---------- | -------------------------------- | ------------------- |
| Bernoulli    | Discrete   | Binary outcomes                  | \( p \)             |
| Binomial     | Discrete   | Number of successes              | \( n, p \)          |
| Poisson      | Discrete   | Count events over time           | \( \lambda \)       |
| Uniform      | Continuous | Equal likelihood over interval   | \( a, b \)          |
| Normal       | Continuous | Natural phenomena, central limit | \( \mu, \sigma^2 \) |
| Exponential  | Continuous | Time until event                 | \( \lambda \)       |

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
