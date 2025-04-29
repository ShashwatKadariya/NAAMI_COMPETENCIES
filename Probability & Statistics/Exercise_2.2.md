# 🎲 Exercise 2.2 – Efron Dice (?? Difficulty)

This exercise explores **non-transitive dice**, specifically a set of four dice where each die has a 2/3 chance of beating the next in a cycle.

---

## 🧾 Dice Definitions

Each die has the following faces:

- **Die A**: 4, 4, 4, 4, 0, 0
- **Die B**: 3, 3, 3, 3, 3, 3
- **Die C**: 6, 6, 2, 2, 2, 2
- **Die D**: 5, 5, 5, 1, 1, 1

The surprising result:

- A beats B with probability 2/3
- B beats C with probability 2/3
- C beats D with probability 2/3
- D beats A with probability 2/3

---

## A Beats B

- A rolls 4 (4/6): beats B’s 3 (6 times) → 4×6 = 24 wins
- A rolls 0 (2/6): loses to B’s 3 (0 wins)

**Total wins: 24/36 = 2/3**

---

## B Beats C

- C rolls 2 (4 times): B’s 3 beats 2 → 6×4 = 24 wins
- C rolls 6 (2 times): B’s 3 loses → 6×2 = 12 losses

**Total wins: 24/36 = 2/3**

---

## C Beats D

- C rolls 6 (2): beats all of D (6 outcomes) → 2×6 = 12
- C rolls 2 (4): beats only 1s (3/6) → 4×3 = 12

**Total wins: 12+12 = 24/36 = 2/3**

---

## D Beats A

- D rolls 5 (3): beats 4s and 0s → 3×6 = 18
- D rolls 1 (3): beats 0s only → 3×2 = 6

**Total wins: 18+6 = 24/36 = 2/3**

---

## Conclusion

Each die beats the next with probability 2/3:

\[
A \succ B,\quad B \succ C,\quad C \succ D,\quad D \succ A
\]

This violates transitivity and shows a classic **probabilistic cycle**, useful in **game theory** and **counter-intuition** examples.
