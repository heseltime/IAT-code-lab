---
title: Loss function
type: concept
sources: [iat-nns-notebook-outline, iat-nns-readme]
updated: 2026-11-13
---

# Loss function

A loss function (also: error function, German *Fehlerfunktion*) gives one number that says how wrong a model is. Small
is good. Training a model means making this number as small as possible.

## How it works

A **residual** is the distance between a data point and the model's prediction for it. The notebook adds the
residuals of all points into one number.

The notebook **squares** each residual before adding them up (heading: "Summe der Residuenquadrate", the sum of
squared residuals). *(General knowledge:)* squaring does two things. A point above the line and a point below the
line can't cancel each other out, and large errors count much more than small ones.

```
loss = (y₁ − prediction₁)² + (y₂ − prediction₂)² + …
```

**To verify:** the outline at the top of the notebook only says "sum of the residuals". See
[open questions](../open-questions.md#q1-residuals-or-squared-residuals).

The notebook shows the model and the loss function side by side in an animation: when the line gets better, the loss
goes down.

## Related

- [Linear regression](linear-regression.md): the model whose error is measured.
- [Gradient descent](gradient-descent.md): uses the derivative of the loss to improve the model.

## Sources

- [IAT neural networks notebook outline](../sources/iat-nns-notebook-outline.md): step 2.
- [IAT neural networks README](../sources/iat-nns-readme.md): "Error and residuals" is step 2.
