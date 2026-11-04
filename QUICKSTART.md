# 빠른 시작 (Codex + GitHub)

## 사용 순서

1. ZIP을 압축 해제하고 `.agents/skills/` 폴더가 보이는지 확인합니다.
2. 기존 해커톤 프로젝트 저장소 **루트**에 10개 스킬 폴더를 복사하거나, 이 패키지 자체를 새 저장소로 올립니다.
3. Codex CLI/IDE를 **스킬이 있는 저장소에서** 엽니다.
4. README/대회규정을 받은 직후 `$hackathon-intake` 또는 `$readme-analysis`를 호출합니다.
5. 데이터를 받으면 `$dataset-audit` → `$problem-deep-dive`를 호출합니다.
6. 해결할 문제를 정했으면 `$solution-design` → `$architecture-map` → `$mvp-build` → `$verification`로 진행합니다.
7. 제출 전 `$demo-submission`, 오류 발생 시 `$debug-recovery`를 사용합니다.

## 첫 호출 예시

```text
$readme-analysis
현재 폴더의 README 및 과제 지침을 분석하고 P0/P1/P2 요구사항과 근거, 실행 방법을 정리해 줘. 코드는 수정하지 마.
```

**각 Skill 폴더에 해당 Skill 전용 예시 프롬프트가 있습니다.** 복사하기 편한 통합본은 `PROMPTS.md`입니다.

## git clone 후 동작 점검

```powershell
# 현재 저장소 루트에서
python tools/check_skills.py
# 터미널에서 전체 흐름 확인
python tools/show_workflow.py
# Skill 폴더 확인
Get-ChildItem .agents/skills -Directory
```

공개 GitHub에 올리기 전에 대회 데이터, API 키, 비공개 자료를 커밋하지 않았는지 확인하세요. 다른 사람의 README/AGENTS 지침이 있는 기존 프로젝트에서는 덮어쓰기보다 병합을 권장합니다.

## IDE에서 아키텍처 확인 (Mermaid)

1. `ARCHITECTURE.md`를 열면 Skill 흐름도와 범용 시스템 예시를 볼 수 있습니다.
2. 실제 과제 프로젝트에서는 Codex 대화창에 `$architecture-map`를 입력하고 `docs/ARCHITECTURE.md` 생성을 요청하세요.
3. VS Code에서 Markdown 파일을 연 후 `Ctrl+Shift+V`로 미리보기 합니다.
4. 미리보기가 없는 IDE에서는 `Get-Content docs/ARCHITECTURE.md -Encoding UTF8`로 Mermaid 소스를 확인합니다.

주의: `git clone`은 파일을 내려받는 동작이며 Skill을 **실행**하는 명령은 아닙니다. `codex` CLI 또는 IDE Codex 대화창에서 `$skill-name`을 호출하세요.
