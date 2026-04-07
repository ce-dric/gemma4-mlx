# Gemma 4 MLX on Apple Silicon

Minimal local setup for running Gemma 4 E2B on Apple Silicon Macs with MLX.

For Korean documentation, see [README.ko.md](/Users/cedric/Documents/gemma/README.ko.md).

## Why this repo uses MLX

This workspace targets `Apple M1 / 8GB RAM / macOS`. In that environment, the Apple-optimized MLX 4-bit checkpoint is much more practical than loading the original Hugging Face `transformers` checkpoint directly.

References:

- Gemma 4 announcement: [Welcome Gemma 4: Frontier multimodal intelligence on device](https://huggingface.co/blog/gemma4)
- Original model family: [`google/gemma-4-E2B-it`](https://hf.co/google/gemma-4-E2B-it)
- Runtime-friendly model used here: [`mlx-community/gemma-4-e2b-it-4bit`](https://hf.co/mlx-community/gemma-4-e2b-it-4bit)
- Runtime source: [`ml-explore/mlx-lm`](https://github.com/ml-explore/mlx-lm)

## Quick Start

```bash
cd /Users/cedric/Documents/gemma
./setup_env.sh
./run_gemma4.sh "Describe Seoul in one sentence."
```

## Files

- [`setup_env.sh`](/Users/cedric/Documents/gemma/setup_env.sh): creates the virtual environment and installs dependencies
- [`run_gemma4.sh`](/Users/cedric/Documents/gemma/run_gemma4.sh): shell wrapper for quick execution
- [`run_gemma4.py`](/Users/cedric/Documents/gemma/run_gemma4.py): Python entry point for inference
- [`README.ko.md`](/Users/cedric/Documents/gemma/README.ko.md): Korean version of this guide
- [`AGENT_CONTEXT.md`](/Users/cedric/Documents/gemma/AGENT_CONTEXT.md): agent-facing workspace notes

## Environment Setup

```bash
cd /Users/cedric/Documents/gemma
./setup_env.sh
```

What it does:

- creates `.venv`
- upgrades `pip`, `setuptools`, and `wheel`
- installs the latest `mlx-lm` directly from GitHub

Why install from GitHub instead of PyPI:

- an earlier PyPI build failed with `ValueError: Model type gemma4 not supported.`
- the latest GitHub version included `gemma4` support and loaded successfully

## Running the Model

Default run:

```bash
cd /Users/cedric/Documents/gemma
./run_gemma4.sh "Introduce yourself in one sentence."
```

Run with a custom temperature:

```bash
cd /Users/cedric/Documents/gemma
./run_gemma4.sh --temp 1.0 "Describe Seoul in one sentence."
```

Run with a lower temperature for more stable output:

```bash
cd /Users/cedric/Documents/gemma
./run_gemma4.sh --temp 0.2 "Describe Seoul in one sentence."
```

## Notes

- The first run downloads the model into the Hugging Face cache.
- The cached model is roughly `3.4GB`.
- This setup strips the Gemma 4 thinking channel from the printed output and only returns the final answer text.
- Higher `--temp` values produce more varied output. Lower values are more repeatable.
- On the tested machine, peak memory was around `2.65GB`.
