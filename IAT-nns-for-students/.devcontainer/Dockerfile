# Dev container for IAT-nns-for-students: Python 3.12, Graphviz, and CPU-only PyTorch.
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# Graphviz system software, needed to draw the computation graphs in the notebook.
# The base image lists a Yarn package source whose signing key has expired, which breaks apt-get update.
# This lab doesn't need Yarn, so that source is removed first.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends graphviz \
    && rm -rf /var/lib/apt/lists/*

# Python packages. The CPU index keeps PyTorch small: no GPU libraries (several GB) are downloaded.
# constraints.txt pins the exact versions that were tested together.
COPY requirements.txt .devcontainer/constraints.txt /tmp/pip/
RUN pip install --no-cache-dir --root-user-action=ignore \
        --extra-index-url https://download.pytorch.org/whl/cpu \
        -r /tmp/pip/requirements.txt -c /tmp/pip/constraints.txt \
    && rm -rf /tmp/pip
