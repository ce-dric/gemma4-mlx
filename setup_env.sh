#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required."
  exit 1
fi

python3 -m venv .venv
. .venv/bin/activate

python -m pip install -U pip setuptools wheel
python -m pip install -U "git+https://github.com/ml-explore/mlx-lm.git"

echo
echo "Environment setup is complete."
echo "Example run:"
echo "  cd $SCRIPT_DIR"
echo "  ./run_gemma4.sh 'Describe Seoul in one sentence.'"
