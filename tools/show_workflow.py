#!/usr/bin/env python3
"""Print the local Codex hackathon workflow; uses only Python stdlib."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGES = [
    ('00', 'hackathon-intake', '환경/규정 점검'),
    ('01', 'readme-analysis', 'README/요구사항 분석'),
    ('02', 'dataset-audit', '범용 데이터 분석'),
    ('03', 'problem-deep-dive', '문제별 심층 분석'),
    ('04', 'solution-design', '해결 알고리즘 설계'),
    ('09', 'architecture-map', '실제 아키텍처 시각화'),
    ('05', 'mvp-build', 'MVP 구현'),
    ('06', 'verification', '요구사항/성능 검증'),
    ('07', 'demo-submission', '데모/제출 점검'),
]

def main():
    print('\nCodex Hackathon Skills Workflow (repo-local)\n')
    for i, (num, name, title) in enumerate(STAGES):
        skill_file = ROOT / '.agents' / 'skills' / f'{num}-{name}' / 'SKILL.md'
        state = 'OK' if skill_file.is_file() else 'MISSING'
        print(f' {num}  ${name:<21} {title} [{state}]')
        if i != len(STAGES) - 1:
            print('      |')
            print('      v')
    print('\n  On failure: $debug-recovery')
    print('  Architecture example: ARCHITECTURE.md')
    print('  Prompt examples: PROMPTS.md')
    print('  Run: python tools/check_skills.py\n')

if __name__ == '__main__':
    main()
