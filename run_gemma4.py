#!/usr/bin/env python3
import re
import sys

from mlx_lm import generate, load


MODEL_ID = "mlx-community/gemma-4-e2b-it-4bit"


def extract_content(text: str) -> str:
    text = re.sub(r"<\|channel>thought.*?<channel\|>", "", text, flags=re.S)
    text = text.replace("<|channel>final\n", "")
    text = text.replace("<turn|>", "")
    return text.strip()


def main() -> int:
    prompt = " ".join(sys.argv[1:]).strip() or "한국어로 자기소개를 한 문장으로 해줘."
    model, tokenizer = load(MODEL_ID)
    messages = [{"role": "user", "content": prompt}]
    rendered_prompt = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    raw = generate(model, tokenizer, prompt=rendered_prompt, max_tokens=128, verbose=False)
    print(extract_content(raw))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
