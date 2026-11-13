---
title: Computation graph
type: concept
sources: [iat-nns-notebook-outline, iat-nns-readme]
updated: 2026-11-13
---

# Computation graph

A computation graph is a drawing of a calculation. Each box is a number or an operation (like `+` or `·`), and the
arrows show which result feeds into which.

## How it works

The notebook draws the graph of the [linear regression](linear-regression.md) loss. First it uses one data point, so
the structure is easy to see, and then three data points, so the graph gets bigger.

*(General knowledge:)* the graph is useful because the computer can walk it **backwards**, from the loss to each
parameter, and compute every derivative on the way. This is called **backpropagation**. `micrograd`, a tiny
library by Andrej Karpathy, does exactly this. Big libraries such as PyTorch work the same way, only with much
larger graphs.

The notebook checks the graph's derivatives with a calculation by hand, to show that
[gradient descent](gradient-descent.md) really works.

To draw the graphs you need Graphviz installed as system software, not only the Python package (see the README of
`IAT-nns-for-students`).

## Related

- [Gradient descent](gradient-descent.md): uses the derivatives from the graph.
- [Neural network](neural-network.md): its graph is the same idea, only bigger.

## Sources

- [IAT neural networks notebook outline](../sources/iat-nns-notebook-outline.md): step 5.
- [IAT neural networks README](../sources/iat-nns-readme.md): step 5 and the Graphviz setup.
