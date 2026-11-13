# Neural Networks for Students 🧠

This repository is a small teaching project about how neural networks learn. It is written for classroom use and is
best explored step by step.

The main file is [`iat_demo.ipynb`](iat_demo.ipynb), a Jupyter notebook. If you are new to the topic, start there.
The notebook's text is in German; the code and the plots speak for themselves.

## What You Will See

The notebook builds up the main ideas behind neural networks in a simple order:

1. A straight line as a model
2. Error and residuals
3. Derivatives as a guide toward a better solution
4. Gradient descent
5. A computation graph with `micrograd`
6. Linear regression with one and two parameters
7. Classification with one neuron
8. Classification with a small neural network
9. A final step toward MNIST digit recognition

The goal is not just to use machine learning, but to understand what the model is doing.

## Setup 💻

Choose **one** of the three options. Option A is the easiest: everything is installed for you.

| Option | You need | Good for |
|---|---|---|
| **A. Dev container** (recommended) | VS Code, Docker Desktop | Your own laptop: same setup for everyone, no Python installation |
| **B. GitHub Codespaces** | A browser and a GitHub account | School computers, or if Docker doesn't run on your laptop |
| **C. Local Python** | Python 3.10+, Graphviz | If you already know Python environments |

### Option A: Dev container (recommended)

A dev container is a ready-made Linux environment that runs inside Docker. It already has Python 3.12, all the
packages and Graphviz installed. It's the same on Windows, macOS and Linux.

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and start it.
2. In VS Code, install the extension **Dev Containers** (by Microsoft).
3. Open this folder in VS Code: **File → Open Folder** → `IAT-nns-for-students`.
4. VS Code asks: *"Folder contains a Dev Container configuration file. Reopen folder to develop in a container?"*
   Click **Reopen in Container**. (Or press `Ctrl+Shift+P` / `Cmd+Shift+P` and run
   **Dev Containers: Reopen in Container**.)
5. Wait for the first build. It takes a few minutes, once. After that it starts in seconds.
6. Open [`iat_demo.ipynb`](iat_demo.ipynb). If VS Code asks for a kernel, choose **Python 3.12** (`/usr/local/bin/python`).

### Option B: GitHub Codespaces

The same dev container, running on GitHub's computers. You only need a browser.

1. Fork the lab repository on GitHub (see the [lab README](../README.md#3-get-your-own-copy-of-the-lab)).
2. On your fork: **Code → Codespaces → ⋯ → New with options**, and choose the configuration **IAT neural networks**.
3. Wait for the build, then open `iat_demo.ipynb`.

GitHub gives free monthly hours to personal accounts. Stop the codespace when you are done, so you don't use them up.

### Option C: Local Python

1. Install [Python 3.10 or newer](https://www.python.org/downloads/) and, in VS Code, the extensions **Python** and
   **Jupyter**.
2. Install **Graphviz** as system software. The Python package alone is not enough: the computation-graph drawings
   need the `dot` program.
   - macOS (with [Homebrew](https://brew.sh)): `brew install graphviz`
   - Windows: `winget install Graphviz.Graphviz`, or the installer from [graphviz.org](https://graphviz.org/download/).
     Restart VS Code afterwards.
   - Linux: `sudo apt install graphviz`
3. Open this folder in VS Code and a terminal in it (`` Ctrl+` ``). Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
   ```

4. Install the packages. This takes a few minutes, because PyTorch is big:

   ```bash
   pip install -r requirements.txt
   ```

5. In the notebook, choose the kernel from `.venv` (top right of the notebook window).

## Run the notebook 🚀

Open [`iat_demo.ipynb`](iat_demo.ipynb) and run the cells from top to bottom (**Run All**, or `Shift+Enter` cell by
cell). Most cells take a few seconds. The animation of the neural network learning (section 8) takes **about 6
minutes**, because it computes every frame first. It shows its progress ("Precomputing frame ..."). The whole
notebook takes about 9 minutes.

Many cells include animations and visualizations. These are there to help you build intuition:

- how a model makes predictions
- how error changes
- how parameters move during learning
- how a neural network separates classes

## The MNIST script 🔢

[`mnist-pytorch.py`](mnist-pytorch.py) trains a small PyTorch network to recognize handwritten digits from the MNIST
dataset. Think of it as the more advanced follow-up after the notebook. Run it in the terminal:

```bash
python mnist-pytorch.py              # 5 epochs, under a minute on most laptops
python mnist-pytorch.py --epochs 1   # a quick test run (about 95% correct already)
```

After each epoch it shows the digits it recognized best, and the ones it got most wrong. At the end, a window opens
where you can **draw your own digit** and watch the network guess.

In the dev container or Codespaces there is no screen for windows. There, the script saves the pictures to
`outputs/` instead and skips the drawing canvas. To draw digits, run the script with Option C on your own computer.

## If something goes wrong 🛠️

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | The packages are not installed for the Python you are using. Check the kernel (top right of the notebook). With Option C: activate `.venv` and run `pip install -r requirements.txt` again |
| `ExecutableNotFound` when drawing a graph | Graphviz system software is missing. See Option C, step 2, or use the dev container |
| A variable or function is missing | Notebooks depend on the order you run cells in. Run the earlier cells again, or use **Run All** |
| `pip install` fails while "building" numpy, scipy or torch | Your Python is too new or too old for a package. Use the dev container, or Python 3.12 |
| The dev container doesn't start | Is Docker Desktop running? Then try **Dev Containers: Rebuild Container** |

## Suggested Student Workflow

1. Open the notebook.
2. Run one section at a time.
3. Pause after each plot or animation and explain in your own words what changed.
4. Change a few values and see what happens.
5. Move to the MNIST script only after the notebook ideas make sense.

## Big Idea ✨

Neural networks are not magic. They are built from simple mathematical steps repeated many times. This notebook is
designed to make those steps visible.
