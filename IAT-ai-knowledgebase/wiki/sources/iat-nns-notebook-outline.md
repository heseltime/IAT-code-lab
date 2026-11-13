---
title: IAT neural networks notebook outline
type: source
sources: [iat-nns-notebook-outline]
updated: 2026-11-13
---

# IAT neural networks notebook outline

- **Raw file:** [`raw/iat-nns-notebook-outline.md`](../../raw/iat-nns-notebook-outline.md)
- **What it is:** the text (Markdown) cells of `iat_demo.ipynb`, the teaching notebook in `IAT-nns-for-students`.
  The code and the animations are not part of this source.
- **Author / origin:** IAT Coding Lab
- **Language:** German (translated here)
- **Added:** 2026-11-13

## Summary

The notebook is a script ("Drehbuch") for a 1.5-hour introduction to neural networks. It starts with the simplest
possible model, a straight line with one parameter, and builds up step by step: an error function, the derivative as
the direction to the minimum, gradient descent with `micrograd`, a drawing of the computation graph, a model with two
parameters, a single neuron that classifies points, and finally a whole neural network. The last step, recognising
handwritten digits (MNIST), is a separate script. The neural-network demo is adapted from a template by Andrej
Karpathy.

## Key points

1. Linear regression with one parameter (the slope of the line) → [linear regression](../concepts/linear-regression.md)
2. The sum of the (squared) residuals as the error function → [loss function](../concepts/loss-function.md)
3. The derivative as the direction towards the minimum → [gradient descent](../concepts/gradient-descent.md)
4. `micrograd` for linear regression: change the parameter β₁ in the direction of the negative derivative (gradient)
   → [gradient descent](../concepts/gradient-descent.md)
5. A drawing of the computation graph, first with one data point, then with three. Each time, a calculation by hand
   checks that gradient descent works → [computation graph](../concepts/computation-graph.md)
6. Linear regression with two parameters, again trained by gradient descent
7. Classification with a single neuron → [neural network](../concepts/neural-network.md)
8. Classification with a whole neural network: data, model, error function, training
   → [neural network](../concepts/neural-network.md)
9. MNIST classification in a separate script

## Questions this source raises

- The outline says "sum of the residuals", but the section heading says "sum of the **squared** residuals". See
  [open questions](../open-questions.md#q1-residuals-or-squared-residuals).
- The notebook points to the MNIST script at `/opt/pytorch-env/IAT-MNIST/mnist-pytorch.py`. See
  [open questions](../open-questions.md#q2-where-is-the-mnist-script).
