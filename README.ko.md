# Gemma 4 MLX on Apple Silicon

이 문서는 Apple Silicon Mac에서 MLX로 Gemma 4 E2B를 실행하는 최소 구성 안내입니다.

영문 기본 문서는 [README.md](./README.md)에서 볼 수 있습니다.

## 왜 이 저장소는 MLX를 쓰는가

이 워크스페이스는 `Apple M1 / 8GB RAM / macOS` 기준으로 구성되었습니다. 이 환경에서는 Hugging Face `transformers`용 원본 체크포인트를 직접 올리는 것보다, Apple Silicon에 맞춘 MLX 4bit 체크포인트가 훨씬 현실적입니다.

참고 링크:

- Gemma 4 공식 소개: [Welcome Gemma 4: Frontier multimodal intelligence on device](https://huggingface.co/blog/gemma4)
- 원본 모델 계열: [`google/gemma-4-E2B-it`](https://hf.co/google/gemma-4-E2B-it)
- 이 저장소에서 사용하는 모델: [`mlx-community/gemma-4-e2b-it-4bit`](https://hf.co/mlx-community/gemma-4-e2b-it-4bit)
- 런타임 소스: [`ml-explore/mlx-lm`](https://github.com/ml-explore/mlx-lm)

## 빠른 시작

```bash
git clone git@github.com:ce-dric/gemma4-mlx.git
cd gemma4-mlx
./setup_env.sh
./run_gemma4.sh "서울을 한 문장으로 소개해줘."
```

## 파일 구성

- [`setup_env.sh`](./setup_env.sh): 가상환경 생성 및 의존성 설치
- [`run_gemma4.sh`](./run_gemma4.sh): 빠른 실행용 셸 래퍼
- [`run_gemma4.py`](./run_gemma4.py): Python 추론 실행기
- [`AGENT_CONTEXT.md`](./AGENT_CONTEXT.md): 에이전트용 영문 작업 문서

## 환경 설정

```bash
cd gemma4-mlx
./setup_env.sh
```

설치 내용:

- `.venv` 생성
- `pip`, `setuptools`, `wheel` 업그레이드
- `mlx-lm` 최신 GitHub 버전 설치

GitHub 버전을 쓰는 이유:

- 초기 PyPI 버전에서는 `ValueError: Model type gemma4 not supported.` 오류가 발생할 수 있었습니다.
- 최신 GitHub 버전은 `gemma4` 지원을 포함하고 있어 정상 로드가 가능했습니다.

## 실행 방법

기본 실행:

```bash
cd gemma4-mlx
./run_gemma4.sh "서울을 한 문장으로 소개해줘."
```

temperature를 높여 더 랜덤하게 실행:

```bash
cd gemma4-mlx
./run_gemma4.sh --temp 1.0 "서울을 한 문장으로 소개해줘."
```

temperature를 낮춰 더 안정적으로 실행:

```bash
cd gemma4-mlx
./run_gemma4.sh --temp 0.2 "서울을 한 문장으로 소개해줘."
```

## 메모

- 첫 실행 시 Hugging Face 캐시에 모델을 다운로드합니다.
- 캐시된 모델 크기는 약 `3.4GB`입니다.
- 이 구성은 Gemma 4의 thinking 채널을 제거하고 최종 답변 텍스트만 출력합니다.
- `--temp` 값이 높을수록 출력이 더 다양해지고, 낮을수록 반복 가능성이 높아집니다.
- 테스트한 장비에서는 피크 메모리가 약 `2.65GB` 수준이었습니다.
