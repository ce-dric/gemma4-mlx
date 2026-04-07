#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3가 필요합니다."
  exit 1
fi

python3 -m venv .venv
. .venv/bin/activate

python -m pip install -U pip setuptools wheel
python -m pip install -U "git+https://github.com/ml-explore/mlx-lm.git"

echo
echo "환경 설정이 완료되었습니다."
echo "실행 예시:"
echo "  cd $SCRIPT_DIR"
echo "  ./run_gemma4.sh '서울을 한 문장으로 소개해줘.'"
