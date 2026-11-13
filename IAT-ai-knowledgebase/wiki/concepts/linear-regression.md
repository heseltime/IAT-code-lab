---
title: Linear regression
type: concept
sources: [iat-nns-notebook-outline, iat-nns-readme]
updated: 2026-11-13
---

# Linear regression

Linear regression fits a straight line through data points. It is the first and simplest model in the IAT notebook.

## How it works

The notebook starts with a line that has **one parameter**: its slope, called β₁ (beta one). The model is
*(general knowledge)*:

```
prediction = β₁ · x
```

"Learning" means finding the β₁ for which the line is closest to the data. How close it is, is measured by a
[loss function](loss-function.md). The value of β₁ is improved step by step with
[gradient descent](gradient-descent.md).

Later the notebook uses **two parameters**. Usually these are the slope and the point where the line crosses the
y-axis *(general knowledge)*: `prediction = β₀ + β₁ · x`. The training works the same way.

## Related

- [Loss function](loss-function.md): measures how far the line is from the data.
- [Gradient descent](gradient-descent.md): the method that improves β₁.
- [Neural network](neural-network.md): a single neuron is a line with an extra function on top.

## Sources

- [IAT neural networks notebook outline](../sources/iat-nns-notebook-outline.md): steps 1, 4 and 6.
- [IAT neural networks README](../sources/iat-nns-readme.md): "A straight line as a model" is step 1.
