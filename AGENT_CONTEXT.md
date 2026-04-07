# Agent Context: Gemma 4 MLX Workspace

This document gives future agents a compact overview of the workspace.

## Purpose

This repository is a minimal, reproducible setup for running Gemma 4 E2B locally on Apple Silicon Macs using MLX.

## Current Model Choice

- Primary model: `mlx-community/gemma-4-e2b-it-4bit`
- Original reference model: `google/gemma-4-E2B-it`
- Rationale: the target machine was `Apple M1 / 8GB RAM`, so the MLX 4-bit checkpoint is a safer default than the original `transformers` checkpoint

## Confirmed Facts

- The referenced Hugging Face Gemma 4 blog post was published on `2026-04-02`.
- An earlier `mlx-lm` build failed with `ValueError: Model type gemma4 not supported.`
- Installing `mlx-lm` from `git+https://github.com/ml-explore/mlx-lm.git` resolved that issue.
- `run_gemma4.py` removes the Gemma 4 thinking channel and prints only the final response content.
- The default runtime path in this repository is MLX, not Hugging Face `transformers`.

## Repository Files

- [`README.md`](/Users/cedric/Documents/gemma/README.md): primary English documentation
- [`README.ko.md`](/Users/cedric/Documents/gemma/README.ko.md): Korean documentation
- [`setup_env.sh`](/Users/cedric/Documents/gemma/setup_env.sh): environment bootstrap script
- [`run_gemma4.sh`](/Users/cedric/Documents/gemma/run_gemma4.sh): shell entry point
- [`run_gemma4.py`](/Users/cedric/Documents/gemma/run_gemma4.py): Python inference entry point

## Working Rules

- Prefer relative path handling inside scripts.
- Preserve the Apple Silicon + MLX local workflow unless the task explicitly asks for another runtime.
- Keep the English README as the primary entry point and link out to the Korean version as needed.
- If adding documentation, update the English README first.
- If adding alternative runtimes, keep the current MLX path intact unless the task explicitly replaces it.

## Likely Future Extensions

- Add a `transformers` comparison example
- Add benchmark notes for latency and memory
- Add HF token setup guidance
- Add multimodal prompt examples
