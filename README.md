# Universal AI Hackathon Codex Skills Kit

**특정 산업/과제에 종속되지 않는, 재사용 가능한 Codex Skill 10종.** Python/웹/최적화/머신러닝/데이터 분석 등 다양한 해커톤에 대응하도록 설계했습니다. 외부 의존성 없는 가벼운 지침 중심 패키지입니다.

> 주의: 이 패키지는 대회 문제와 데이터가 아직 없는 상태에서 만드는 **방법론/작업 지침**입니다. 해커톤의 규정·실제 평가기준은 제공 문서에서 확인해야 합니다.

## 스킬 목록

| 순서 | Skill 호출 | 용도 | 복사 가능한 예시 |
| --- | --- | --- | --- |
| 00 | `$hackathon-intake` | 대회 규정·환경·제약 점검 | [예시](.agents/skills/00-hackathon-intake/PROMPT_EXAMPLE.md) |
| 01 | `$readme-analysis` | README/요구사항 분석 | [예시](.agents/skills/01-readme-analysis/PROMPT_EXAMPLE.md) |
| 02 | `$dataset-audit` | 범용 데이터 구조·품질·1차 EDA | [예시](.agents/skills/02-dataset-audit/PROMPT_EXAMPLE.md) |
| 03 | `$problem-deep-dive` | 문제 중심 심층 분석 | [예시](.agents/skills/03-problem-deep-dive/PROMPT_EXAMPLE.md) |
| 04 | `$solution-design` | 해결 방식·알고리즘·아키텍처 설계 | [예시](.agents/skills/04-solution-design/PROMPT_EXAMPLE.md) |
| 05 | `$mvp-build` | P0 중심 MVP 구현·단계별 테스트 | [예시](.agents/skills/05-mvp-build/PROMPT_EXAMPLE.md) |
| 06 | `$verification` | 요구사항·테스트·성능 검증 | [예시](.agents/skills/06-verification/PROMPT_EXAMPLE.md) |
| 07 | `$demo-submission` | 데모·제출·평가 근거 준비 | [예시](.agents/skills/07-demo-submission/PROMPT_EXAMPLE.md) |
| 08 | `$debug-recovery` | 오류 재현·진단·복구 | [예시](.agents/skills/08-debug-recovery/PROMPT_EXAMPLE.md) |
| 09 | `$architecture-map` | 실제 프로젝트 구조·데이터 흐름 Mermaid 시각화 | [예시](.agents/skills/09-architecture-map/PROMPT_EXAMPLE.md) |

**추천 흐름:** 00 → 01 → 02 → 03 → 04 → 09 → 05 → 06 → 07. 오류가 나면 어느 단계에서든 08을 호출합니다. 데이터가 없으면 02의 '데이터 미제공' 결론을 기록하고 다음 단계로 이동합니다.

## 1. GitHub에 업로드하고 git clone 하기

ZIP은 GitHub가 자동으로 풀어주지 않습니다. **압축을 먼저 푼 다음 폴더와 파일 자체를 Git 저장소에 올려야** Codex가 Skill을 인식합니다.

### 새 저장소에 올릴 때 (PowerShell 예시)

1. GitHub에서 빈 **공개/비공개 저장소**를 만듭니다. 공개 제한은 대회 규정에 따르세요.
2. 로컬에서 아래처럼 기존 원격 저장소를 클론합니다(주소는 본인 저장소로 변경).
3. 압축을 풀어 나온 **내용물**(`.agents`, `AGENTS.md`, `README.md` 등)을 클론한 저장소 **최상위(root)**에 복사합니다. 숨김 폴더 `.agents`도 반드시 포함하세요.
4. 아래 명령으로 파일이 포함됐는지 확인하고 커밋/푸시합니다.

```powershell
git clone https://github.com/YOUR_ID/YOUR_REPO.git
cd YOUR_REPO
# 여기에 ZIP 해제 내용물 복사 (ZIP 파일 자체만 올리지 않기)
python tools/check_skills.py
python tools/show_workflow.py
git status
git add .agents AGENTS.md README.md QUICKSTART.md PROMPTS.md tools .gitignore
git commit -m "Add reusable Codex hackathon skills"
git push origin HEAD
```

대회장에서 사용할 때:

```powershell
git clone https://github.com/YOUR_ID/YOUR_REPO.git
cd YOUR_REPO
codex
```

Codex 대화창에서 `$readme-analysis` 등 원하는 Skill을 부르세요. Codex CLI가 없는 환경이면 제공된 IDE Codex 확장에서 **클론한 저장소를 프로젝트로 열어** 사용하세요. Codex가 Skill 변경을 바로 감지하지 못할 경우 다시 시작하세요.

### 이미 코드가 있는 저장소에 추가할 때

`.agents/skills/`의 각 Skill 폴더를 **기존 저장소 루트의** `.agents/skills/`에 복사하세요. 기존 `README.md`, `AGENTS.md`, `.gitignore`가 있다면 무조건 덮어쓰지 말고 내용만 병합하세요. `tools/check_skills.py`는 선택적으로 복사할 수 있습니다.

**중요:** 스킬을 프로젝트 바깥의 다른 폴더에 두거나 ZIP 한 개만 업로드하면 자동 검색되지 않을 수 있습니다. Codex를 실행하는 작업 디렉터리/저장소 루트에서 `.agents/skills/`가 발견되게 배치하세요.

## 2. 빠르게 시작하기

1. `QUICKSTART.md`에서 한 번에 따라하는 방법을 확인합니다.
2. `PROMPTS.md` 또는 개별 `PROMPT_EXAMPLE.md`에서 명령을 복사합니다.
3. README 분석 결과를 검토한 뒤, 데이터 분석 Skill로 넘어갑니다.
4. 분석 단계(00~04)에서는 기존 코드나 원본 데이터가 수정되지 않도록 합니다.
5. 구현은 P0를 먼저, 검증은 실제 실행 결과만 기록합니다.

## 3. 아키텍처 그림을 IDE에서 보기

- `ARCHITECTURE.md`: 이 Skill 패키지의 동작 흐름과 **범용 예시 시스템/데이터 아키텍처**(실제 구현이라고 주장하지 않음).
- `python tools/show_workflow.py`: PowerShell/IDE 터미널에서 단계별 스킬과 연결 순서를 텍스트로 확인.
- `$architecture-map`: 실제 과제 저장소를 분석한 뒤 Mermaid 다이어그램을 작성. 명시적으로 요청하면 `docs/ARCHITECTURE.md`에 저장.
- VS Code에서 `.md` 파일을 열고 **Ctrl+Shift+V** 를 눌러 다이어그램 미리보기.

## 4. 폴더 구성

```text
.
├─ .agents/
│  └─ skills/
│     ├─ 00-hackathon-intake/
│     │  ├─ SKILL.md
│     │  └─ PROMPT_EXAMPLE.md
│     ├─ 01-readme-analysis/
│     ├─ 02-dataset-audit/
│     │  └─ scripts/profile_csv.py  # 읽기 전용 CSV/TSV 간이 분석
│     ├─ 03-problem-deep-dive/
│     ├─ 04-solution-design/
│     ├─ 05-mvp-build/
│     ├─ 06-verification/
│     ├─ 07-demo-submission/
│     ├─ 08-debug-recovery/
│     └─ 09-architecture-map/
├─ ARCHITECTURE.md          # Mermaid로 보는 전체 Skill·범용 시스템 구조
├─ AGENTS.md               # 프로젝트 전체 기본 규칙
├─ PROMPTS.md              # 프롬프트 모음
├─ QUICKSTART.md            # 빠른 시작·업로드 방법
├─ tools/check_skills.py    # 폴더/메타데이터 자체 점검
├─ tools/show_workflow.py   # 터미널용 Skill 흐름도
└─ .gitignore
```

## 5. 스킬과 프롬프트의 차이

- **`SKILL.md`**: Codex가 필요할 때 읽는 재사용 **작업 절차**.
- **`PROMPT_EXAMPLE.md`**: 사용자가 지금 어떤 작업을 시작할지 알려주는 **1회성 호출 예시**.
- **`AGENTS.md`**: 스킬을 쓰지 않는 작업에도 적용되는 이 프로젝트의 **기본 규칙**.
- **`PROMPTS.md`**: 복사 편의용 전체 예시 프롬프트 모음.

## 6. 유의사항

- 제공 데이터의 공개/반출 여부, 외부 라이브러리·AI 모델 허용 여부는 해커톤별 공식 규정이 우선입니다.
- 예시 프롬프트의 `$...` 호출은 Codex가 해당 스킬을 인식하는 환경에서 사용하세요.
- 데이터 프로파일러는 모든 데이터 분석을 대신하지 않습니다. 실제 과제의 KPI·원인·알고리즘 판단에는 단계 03~04가 필요합니다.
- 결과 수치와 '테스트 통과'는 실제 실행 결과가 있을 때만 기재합니다.
