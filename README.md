# 조치원 새내12길 14 1층 업종 분석

- `jochiwon_report.html`: 상권 분석 보고서
- `scripts/`: 소상공인시장진흥공단 상가정보 API(data.go.kr 15012005) 집계 스크립트

## 사용법
인증키는 환경변수 `SK`로 전달합니다. 키를 파일에 저장하지 마세요.

    SK=<발급키> python scripts/fetch_stores.py 127.298659 36.602172 300 r300.json
    python -X utf8 scripts/aggregate.py <r300.json, r500.json이 있는 폴더>
