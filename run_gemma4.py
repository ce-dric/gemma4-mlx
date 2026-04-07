#!/usr/bin/env python3
import argparse
import re

from mlx_lm import generate, load
from mlx_lm.sample_utils import make_sampler


MODEL_ID = "mlx-community/gemma-4-e2b-it-4bit"


def extract_content(text: str) -> str:
    text = re.sub(r"<\|channel>thought.*?<channel\|>", "", text, flags=re.S)
    text = text.replace("<|channel>final\n", "")
    text = text.replace("<turn|>", "")
    return text.strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Gemma 4 E2B IT on Apple Silicon via MLX.")
    parser.add_argument("prompt", nargs="*", help="Prompt text to send to the model.")
    parser.add_argument(
        "--temp",
        type=float,
        default=0.8,
        help="Sampling temperature. Higher values produce more varied outputs.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=128,
        help="Maximum number of tokens to generate.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    prompt = " ".join(args.prompt).strip() or "Introduce yourself in one sentence in Korean."
    model, tokenizer = load(MODEL_ID)
    messages = [{"role": "user", "content": prompt}]
    rendered_prompt = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    raw = generate(
        model,
        tokenizer,
        prompt=rendered_prompt,
        sampler=make_sampler(temp=args.temp),
        max_tokens=args.max_tokens,
        verbose=False,
    )
    print(extract_content(raw))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
