#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"
. "$SCRIPT_DIR/.venv/bin/activate"

PROMPT="${*:-한국어로 자기소개를 한 문장으로 해줘.}"

python "$SCRIPT_DIR/run_gemma4.py" "$PROMPT"
