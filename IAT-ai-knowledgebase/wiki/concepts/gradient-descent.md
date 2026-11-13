---
title: Gradient descent
type: concept
sources: [iat-nns-notebook-outline, iat-nns-readme]
updated: 2026-11-13
---

# Gradient descent

Gradient descent is how a model learns: change each parameter a little bit in the direction that makes the
[loss](loss-function.md) smaller, and repeat many times.

## How it works

The **derivative** of the loss tells you which way is "downhill". The notebook calls it "the direction to the
minimum" (*Ableitung als Richtung zum Minimum*). The README calls derivatives "a guide toward a better solution".

For one parameter β₁, one step is *(general knowledge)*:

```
β₁_new = β₁ − learning_rate · (derivative of the loss with respect to β₁)
```

The minus sign is the important part: we move **against** the derivative, in the "negative gradient" direction. The
**learning rate** is a small number that sets the step size.

With more than one parameter, the list of all derivatives is called the **gradient**. The notebook uses the
`micrograd` library to compute it automatically, with a [computation graph](computation-graph.md). It also checks
the result with a calculation by hand.

The same method trains every model in the notebook: the line with one parameter, the line with two parameters, a
single neuron and a whole [neural network](neural-network.md).

## Related

- [Loss function](loss-function.md): the number that gradient descent makes smaller.
- [Computation graph](computation-graph.md): how the derivatives are computed.

## Sources

- [IAT neural networks notebook outline](../sources/iat-nns-notebook-outline.md): steps 3, 4, 6, 7 and 8.
- [IAT neural networks README](../sources/iat-nns-readme.md): steps 3 and 4.
