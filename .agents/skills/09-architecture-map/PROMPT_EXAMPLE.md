# 예시: 실제 해커톤 프로젝트 아키텍처를 그림으로 보기

Codex 입력창에 아래 내용을 복사:

```text
$architecture-map

지금 IDE에서 열어 둔 해커톤 프로젝트의 README와 실제 파일 구조를 분석해 줘.
현재 구현된 구조(As-is)와 앞으로 구현할 추천 구조(To-be)를 구분해서,
1) 시스템 컴포넌트 아키텍처
2) 데이터 입력→검증→처리→출력 흐름도
3) 사용자 요청부터 결과까지의 시퀀스 다이어그램(해당할 때만)
을 Mermaid로 보여줘.
각 구성요소마다 관련 코드 경로와 확인 근거를 붙여 줘.
존재하지 않는 API/DB/AI 기능은 반드시 '제안'이라고 표시해 줘.

나중에 IDE Markdown 미리보기로 확인할 수 있도록 docs/ARCHITECTURE.md를 생성해 줘.
기존 소스코드와 원본 데이터는 변경하지 마.
```

> Mermaid 미리보기: VS Code에서 `docs/ARCHITECTURE.md` 열기 → `Ctrl+Shift+V`.
> 터미널에서 텍스트만 보려면 `Get-Content docs/ARCHITECTURE.md -Encoding UTF8`.
