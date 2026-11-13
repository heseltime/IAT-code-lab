# Open questions

Things the sources don't answer yet, or where they disagree. When a question is answered, move it to **Answered**
with a link to the page or source that answers it.

## Open

### <a id="q1-residuals-or-squared-residuals"></a>Q1: Residuals or squared residuals?

The [notebook outline](sources/iat-nns-notebook-outline.md) says "sum of the residuals" (*Summe der Residuen*), but
the section heading says "sum of the squared residuals" (*Summe der Residuenquadrate*). The
[loss function](concepts/loss-function.md) page uses the squared version.
**To check:** the code cell of that section in `iat_demo.ipynb`.

### <a id="q2-where-is-the-mnist-script"></a>Q2: Where is the MNIST script?

The sources disagree:

- The [notebook outline](sources/iat-nns-notebook-outline.md) says `/opt/pytorch-env/IAT-MNIST/mnist-pytorch.py`.
- The [README](sources/iat-nns-readme.md) links `IAT/mnist-pytorch.py` and `IAT/iat_demo.ipynb`.
- In the repository today, both files are at the top level: `mnist-pytorch.py` and `iat_demo.ipynb`.

**To check:** fix the README and the last notebook cell in `IAT-nns-for-students`, then ingest the new README.

## Answered

None yet.
