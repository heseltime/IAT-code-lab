---
title: Neural network
type: concept
sources: [iat-nns-notebook-outline, iat-nns-readme]
updated: 2026-11-13
---

# Neural network

A neural network is many simple units (neurons) connected in layers. It learns the same way as the straight line in
the notebook: with a [loss function](loss-function.md) and [gradient descent](gradient-descent.md).

> "Neural networks are not magic. They are built from simple mathematical steps repeated many times."
> — README of `IAT-nns-for-students`

## How it works

**One neuron** *(general knowledge)*: multiply each input by a weight, add them up, add a bias, and put the result
through a non-linear function (for example `tanh`). Without the last step, a neuron is just
[linear regression](linear-regression.md).

The notebook first trains **a single neuron** to classify points into two groups. Then it trains **a whole network**
on the same kind of task. It shows the training as an animation: you can watch the border between the classes move.
This demo is adapted from a template by Andrej Karpathy.

The last step is **MNIST**: recognising handwritten digits (0–9) with PyTorch, in a separate script.

## Related

- [Gradient descent](gradient-descent.md): trains the network.
- [Computation graph](computation-graph.md): computes the derivatives for all weights.
- *(General knowledge:)* large language models, like the one that maintains this wiki, are also neural networks,
  only much bigger.

## Sources

- [IAT neural networks notebook outline](../sources/iat-nns-notebook-outline.md): steps 7, 8 and 9.
- [IAT neural networks README](../sources/iat-nns-readme.md): steps 7–9 and the "Big Idea".
