# syntax=docker/dockerfile:1.7
# Bundle environment.
#
# Built from the pinned harness tree that travels with this repository, never from the upstream
# docker/Dockerfile. The upstream file clones a moving branch at build time and pulls again after
# installation, so it cannot produce a stable digest, and a bundle whose image cannot be pinned by digest
# cannot be graded reproducibly.
#
# This image provisions the substrate and carries no bundle byte. That is a correctness requirement, not a
# size optimisation. The image digest is recorded in harness.image inside the run specification, which is
# itself part of the bundle bytes the canonical hash covers. An image that baked the bundle in would have
# to be built before the digest existed and would therefore always contain a different bundle than the one
# that names it, which makes the CLOSURE IDENTITY atom unprovable by construction: the scanned components
# could never equal the shipped and executed components. Keeping the substrate and the task separate breaks
# that cycle. Harbor mounts the task tree at runtime.
#
# The private boundary is therefore enforced by the mount configuration and proven by the leak gate over
# the assembled agent-visible surface, never by image layers. Under requirements/dataset-spec.md section
# 2.6 the run specification never reaches the agent-visible surface in full, because it carries the
# perturbation parameters and the closure anchors. It must be mounted into the verifier environment only.
#
# The base is pinned by digest rather than by tag. The platform is pinned to linux/amd64 because the
# declared device profile is one NVIDIA H100 and an arm64 image would pin something that cannot run the
# graded task, which is worse than no pin at all.

FROM --platform=linux/amd64 nvidia/cuda:12.9.0-cudnn-devel-ubuntu20.04@sha256:51a67d1f78e6d8973fbfb2c6effb6686f9d2c67f06dc6f840dce8ce975e238d0

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=120 \
    PIP_RETRIES=10 \
    VERITY_BUNDLE_ROOT=/bundle \
    VERITY_HARNESS_ROOT=/harness \
    VERITY_SUBMISSION_DIR=/submission \
    VERITY_RESULTS_ROOT=/logs/runs \
    VERITY_OUTPUT_DIR=/logs/verifier \
    VERITY_NETWORK_EVIDENCE=/logs/env/network_probe.log \
    VERITY_DATA_DIR=/data/cifar

# The harness declares a Python 3.11 floor and this base is Ubuntu 20.04, which ships 3.8.
#
# The interpreter is built from source rather than installed from a distribution package, because the
# deadsnakes PPA has dropped focal: querying Launchpad for published sources in that series returns zero
# entries, while jammy still carries 3.11 through 3.15. Installing from it here would fail at build time.
# The alternative, moving to a 22.04 or 24.04 base, would change the operating system away from the
# substrate requirements/project.md records for this harness, which is a larger deviation than this one.
#
# The one deliberate divergence from the upstream container is that --enable-optimizations is omitted.
# Profile-guided optimisation roughly triples an already slow cross-architecture emulated build and
# affects only interpreter performance. It cannot move a graded quantity here: the budget axis is training
# examples consumed, which is a function of the frozen bytes, and the wall-clock axis is declared absent
# for this bundle. The exact patch version is captured by the image digest either way.
ARG PYTHON_VERSION=3.11.10
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential ca-certificates curl git wget xz-utils zlib1g-dev \
        libbz2-dev libffi-dev liblzma-dev libncursesw5-dev libreadline-dev \
        libsqlite3-dev libssl-dev libxml2-dev libxmlsec1-dev tk-dev uuid-dev \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL "https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz" -o /tmp/python.tgz \
    && tar -xzf /tmp/python.tgz -C /tmp \
    && cd "/tmp/Python-${PYTHON_VERSION}" \
    && ./configure --prefix=/usr/local --with-ensurepip=install --enable-shared \
         LDFLAGS=-Wl,-rpath,/usr/local/lib \
    && make -j"$(nproc)" \
    && make altinstall \
    && cd / && rm -rf /tmp/python.tgz "/tmp/Python-${PYTHON_VERSION}" \
    && ln -sf /usr/local/bin/python3.11 /usr/local/bin/python3 \
    && ln -sf /usr/local/bin/pip3.11 /usr/local/bin/pip3 \
    && python3 --version

# The pinned harness tree, copied in rather than cloned. The build context carries only this tree.
COPY harness /harness

# pytorch_gpu because the run specification pins the pytorch framework and the device profile is a GPU.
# pytest because the compiled rubric tests are reached through the verifier entry point.
#
# SETUPTOOLS_SCM_PRETEND_VERSION is required, not cosmetic. algoperf declares dynamic = ["version"] and
# resolves it through setuptools_scm, which reads version-control metadata. The vendored tree is a git
# submodule whose .git is a pointer file, it carries no tags, and algoperf/_version.py is generated rather
# than committed, so nothing inside the build context can supply a version and the install fails outright
# without this. The value is the vendored release recorded in requirements/project.md.
ENV SETUPTOOLS_SCM_PRETEND_VERSION=1.0.0

# Split into separate layers and backed by a build cache mount, both for reliability rather than tidiness.
# The dependency closure here is several gigabytes of framework wheels, and a single truncated transfer
# fails the whole step. With the download cache discarded between attempts, every retry re-fetches
# everything and the probability of completing falls as the closure grows. The cache mount persists
# downloaded wheels across attempts so a retry resumes, and the split means a failure in the framework
# install does not repeat the interpreter tooling step above it.
RUN --mount=type=cache,target=/root/.cache/pip \
    python3 -m pip install --upgrade pip setuptools wheel

RUN --mount=type=cache,target=/root/.cache/pip \
    python3 -m pip install -e "/harness[pytorch_gpu]"

RUN --mount=type=cache,target=/root/.cache/pip \
    python3 -m pip install pytest

# Do not unpin. tensorflow-metadata is an unpinned transitive dependency, and >=1.21.0 ships protobuf
# gencode incompatible with the protobuf 5.29.6 runtime tensorflow 2.19.0 constrains, leaving
# tensorflow_datasets with no attribute named load. It fails at the first training batch, not at build.
RUN --mount=type=cache,target=/root/.cache/pip \
    python3 -m pip install "tensorflow-metadata==1.17.2"

# The import check is load-bearing. Without it the build can succeed and hand back a digest for an image
# that cannot run the harness, which is worse than a failed build because it pins something unusable.
# The second line exercises the data path, which the first deliberately does not reach.
RUN python3 -c "import algoperf, submission_runner; print('algoperf', algoperf.__version__)"
# The dataset, staged by the fragment the workload profile declares. There was no staging line here at
# all: the template was copied to every bundle, so an unconditional COPY would have staged the wrong
# dataset into every other one. A per-workload fragment is the only shape that is correct for all of them.
FROM verity-algoperf:ship-data-cifar

# The data-path check, also from the profile. This line used to validate the mnist TFDS builder on every
# bundle of every workload, because the one .replace() the emitter performed rewrote "/data/mnist" and
# this string is not that string.
RUN python3 -c "import os; assert os.path.isdir('/data/cifar'); print('cifar data present')"

# Runtime mount points. The bundle tree, the submission, the logs, and the dataset are all mounted.
RUN mkdir -p /bundle /verifier /submission /logs/runs /logs/verifier /logs/env /data/cifar \
    && chmod -R a-w /harness

# The seed submission, at the path instruction.md sends the agent to. Without this the instruction tells
# the agent to improve an algorithm that is not there, which is a harder task than the one described and
# leaves seed_metric anchoring a scale against a submission nobody was handed.
COPY submission_stub/submission.py /submission/submission.py

WORKDIR /submission
