# Agent Context: Gemma 4 Workspace

이 문서는 이 폴더를 읽는 에이전트가 빠르게 문맥을 파악하도록 돕기 위한 운영 메모입니다.

## 목적

이 워크스페이스는 Apple Silicon Mac에서 `Gemma 4 E2B` 계열 모델을 재현 가능하게 실행하는 최소 예제입니다.

## 현재 선택한 모델과 이유

- 사용 모델: `mlx-community/gemma-4-e2b-it-4bit`
- 원본 비교 모델: `google/gemma-4-E2B-it`
- 이유: 현재 머신이 `Apple M1 / 8GB RAM`이라 원본 `transformers` 체크포인트보다 `MLX` 4bit 버전이 더 적합함

## 핵심 제약

- 이 폴더의 기본 목표는 Apple Silicon 로컬 실행입니다.
- 대형 모델 확장은 기본 목표가 아닙니다.
- 문서와 스크립트는 재현성과 단순성을 우선합니다.

## 이미 확인한 사실

- Hugging Face Gemma 4 블로그는 2026-04-02 게시물입니다.
- 초기 `mlx-lm` 설치판에서는 `ValueError: Model type gemma4 not supported.` 오류가 발생했습니다.
- `git+https://github.com/ml-explore/mlx-lm.git`로 설치 후 `gemma4` 지원이 확인되었습니다.
- `run_gemma4.py`로 thinking 채널을 제외한 답변 출력이 가능합니다.

## 주요 파일

- [`README.md`](/Users/cedric/Documents/gemma/README.md): 사용자용 개요 및 사용법
- [`setup_env.sh`](/Users/cedric/Documents/gemma/setup_env.sh): 환경 구성 스크립트
- [`run_gemma4.sh`](/Users/cedric/Documents/gemma/run_gemma4.sh): 빠른 실행 스크립트
- [`run_gemma4.py`](/Users/cedric/Documents/gemma/run_gemma4.py): Python 실행기

## 작업 원칙

- 경로는 가능하면 현재 폴더 기준으로 상대적으로 계산합니다.
- Apple Silicon 로컬 실행 흐름을 깨지 않는 변경을 우선합니다.
- 새 문서를 추가할 때는 `README.md`와 연결합니다.
- `transformers` 원본 경로를 추가하더라도, 현재 기본 경로는 `MLX` 유지가 안전합니다.

## 다음에 확장할 수 있는 주제

- `transformers` 기반 비교 실행 예제 추가
- 메모리/속도 비교 문서 추가
- HF 토큰 설정과 캐시 위치 제어 문서화
- 멀티모달 입력 예제 추가
