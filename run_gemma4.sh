#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"
. "$SCRIPT_DIR/.venv/bin/activate"

python "$SCRIPT_DIR/run_gemma4.py" "$@"
