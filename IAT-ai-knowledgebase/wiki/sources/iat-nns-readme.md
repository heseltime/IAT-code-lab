---
title: IAT neural networks README
type: source
sources: [iat-nns-readme]
updated: 2026-11-13
---

# IAT neural networks README

- **Raw file:** [`raw/iat-nns-readme.md`](../../raw/iat-nns-readme.md)
- **What it is:** the README of the `IAT-nns-for-students` repository: what the notebook teaches and how to set it up
- **Author / origin:** IAT Coding Lab
- **Language:** English
- **Added:** 2026-11-13

## Summary

`IAT-nns-for-students` is a small teaching project about how neural networks learn. The main file is a Jupyter
notebook. It builds up the ideas in nine steps, from a straight line to MNIST digit recognition. The README says the
goal is "not just to use machine learning, but to understand what the model is doing". Most of the README is a setup
guide for VS Code: a Python virtual environment, `pip install -r requirements.txt`, and Graphviz as system software
for the computation-graph drawings. Its big idea: "Neural networks are not magic. They are built from simple
mathematical steps repeated many times."

## Key points

- The nine steps are the same as in the [notebook outline](iat-nns-notebook-outline.md), in English.
- Step 3 calls derivatives "a guide toward a better solution" → [gradient descent](../concepts/gradient-descent.md)
- The computation graph is drawn with `micrograd` and Graphviz → [computation graph](../concepts/computation-graph.md)
- Suggested workflow: run one section at a time, explain each plot in your own words, change values and watch what
  happens, and do the MNIST script last.
- Tools: Python, Jupyter, NumPy, Matplotlib, scikit-learn, PyTorch, Graphviz and `micrograd`.

## Questions this source raises

- The README links to `IAT/iat_demo.ipynb` and `IAT/mnist-pytorch.py`, and says to open a folder called
  `teaching`. See [open questions](../open-questions.md#q2-where-is-the-mnist-script).
