# Gemma 4 on Apple Silicon

이 폴더는 `Gemma 4 E2B`를 Apple Silicon Mac에서 `MLX`로 실행하기 위한 최소 재현 환경입니다.

대상 환경:

- macOS on Apple Silicon
- Python 3
- Hugging Face에서 공개된 Gemma 4 계열 모델 사용

이 저장소에서 사용하는 기본 모델:

- Hugging Face 공식 소개 글: [Welcome Gemma 4: Frontier multimodal intelligence on device](https://huggingface.co/blog/gemma4)
- 실행 모델: [`mlx-community/gemma-4-e2b-it-4bit`](https://hf.co/mlx-community/gemma-4-e2b-it-4bit)
- 원본 모델 계열: [`google/gemma-4-E2B-it`](https://hf.co/google/gemma-4-E2B-it)

## 왜 MLX 버전을 쓰는가

이번 작업 환경은 `Apple M1 / RAM 8GB / macOS`였습니다.

이 환경에서는 Hugging Face `transformers`용 원본 체크포인트보다 Apple Silicon용 `MLX` 4bit 변환본이 훨씬 현실적입니다.

이유:

- `MLX`는 Apple Silicon에 맞게 최적화된 런타임입니다.
- `4bit` 양자화 모델이라 메모리 부담이 더 낮습니다.
- 실제 실행 시 이 환경에서 피크 메모리가 약 `2.65GB` 수준으로 확인되었습니다.

## 빠른 시작

```bash
cd /Users/cedric/Documents/gemma
./setup_env.sh
./run_gemma4.sh "서울을 한 문장으로 소개해줘."
```

## 파일 구성

- [`setup_env.sh`](/Users/cedric/Documents/gemma/setup_env.sh): 가상환경 생성 및 런타임 설치
- [`run_gemma4.sh`](/Users/cedric/Documents/gemma/run_gemma4.sh): 빠른 실행용 쉘 스크립트
- [`run_gemma4.py`](/Users/cedric/Documents/gemma/run_gemma4.py): 실제 추론 실행기
- [`AGENT_CONTEXT.md`](/Users/cedric/Documents/gemma/AGENT_CONTEXT.md): 에이전트용 컨텍스트 문서

## 환경 설정 방법

### 1. Python 확인

```bash
python3 --version
```

### 2. 가상환경 생성 및 의존성 설치

```bash
cd /Users/cedric/Documents/gemma
./setup_env.sh
```

설치 내용:

- `.venv` 생성
- `pip`, `setuptools`, `wheel` 업그레이드
- `mlx-lm` 최신 GitHub 버전 설치

참고:

- PyPI의 특정 시점 버전에서는 `gemma4` 아키텍처를 아직 모를 수 있습니다.
- 실제로 `mlx-lm 0.31.1`에서는 `ValueError: Model type gemma4 not supported.`가 발생했습니다.
- 그래서 `git+https://github.com/ml-explore/mlx-lm.git`로 설치했습니다.

## 수행 방법

### 쉘 스크립트로 실행

```bash
cd /Users/cedric/Documents/gemma
./run_gemma4.sh "서울을 한 문장으로 소개해줘."
```

### Python 실행기로 직접 실행

```bash
cd /Users/cedric/Documents/gemma
. .venv/bin/activate
python run_gemma4.py "한국어로 자기소개를 한 문장으로 해줘."
```

## 시도 방법과 해결 방법

### 처음 시도한 방법

- Hugging Face 공식 Gemma 4 블로그에서 모델 계열과 런타임 지원 범위를 확인했습니다.
- `google/gemma-4-E2B-it` 원본 계열과 Apple용 대안을 비교했습니다.
- 현재 머신이 `Apple M1 / RAM 8GB`라서 `MLX` 4bit 체크포인트를 우선 선택했습니다.

### 실제로 부딪힌 문제

첫 실행 때 모델 다운로드는 성공했지만, 런타임이 다음 오류로 중단됐습니다.

```text
ValueError: Model type gemma4 not supported.
```

### 해결 방법

- `mlx-lm`를 PyPI 최신판 대신 GitHub 최신 소스판으로 업그레이드했습니다.
- 그 뒤 `gemma4` 아키텍처 모듈이 포함된 것을 확인했습니다.
- 다시 실행해서 실제 생성 결과를 확인했습니다.

## 기타 팁

- 첫 실행은 모델 다운로드 때문에 오래 걸릴 수 있습니다.
- 현재 캐시 크기는 약 `3.4G`입니다.
- 인증 없이 받아도 되지만, `HF_TOKEN`을 설정하면 속도나 rate limit 측면에서 유리할 수 있습니다.
- Gemma 4는 응답 포맷에 `thinking` 채널이 같이 섞일 수 있습니다.
- [`run_gemma4.py`](/Users/cedric/Documents/gemma/run_gemma4.py)는 그중 실제 답변 부분만 뽑아서 출력하도록 정리해 둔 버전입니다.
- 더 큰 모델은 이 머신 메모리에서 비현실적일 수 있으므로, 작은 모델이나 더 강한 머신을 권장합니다.

## 참고 링크

- [Gemma 4 공식 블로그](https://huggingface.co/blog/gemma4)
- [`google/gemma-4-E2B-it`](https://hf.co/google/gemma-4-E2B-it)
- [`mlx-community/gemma-4-e2b-it-4bit`](https://hf.co/mlx-community/gemma-4-e2b-it-4bit)
- [`ml-explore/mlx-lm`](https://github.com/ml-explore/mlx-lm)
