# 근쌤의 서재

초등 체육 교사이자 바이브 코더 근쌤의 활동 소개 사이트.
**읽고, 생각하고, 쓰거나 만듭니다.** — 만든 앱, 쓴 글, 강의, 연락처를 한 화면에 하나씩 보여 줍니다.

디자인: 「햇살 드는 서재」 — 밝은 바탕, 남색 글씨, 오른쪽 위 노을빛, BMW M 세 줄 띠.
설계 문서: `docs/superpowers/specs/2026-10-24-portfolio-redesign-design.md`

## 구조

```
pe-portfolio/
├── index.html                 # 메인 (첫 화면 → 만든 것 → 쓴 글 → 강의 → 연락)
├── pepick.html … edumole.html # 앱 상세 7쪽 (scripts/build_detail_pages.py가 만듦 — 직접 고치지 말 것)
├── data/apps.json             # 앱 상세 내용 (이름·소개·화면·기능·주소)
├── css/
│   ├── tokens.css             # 색·글꼴·간격 값
│   ├── base.css               # 모든 페이지 공통 모양
│   ├── home.css               # 메인 페이지
│   └── detail.css             # 앱 상세 페이지
├── js/main.js                 # 휴대폰 메뉴, 앱 목록 펼치기, 스크롤 등장
├── images/
│   ├── profile/               # 근쌤 캐릭터
│   ├── logos/                 # 앱 로고
│   └── screenshots/           # 앱 화면
└── scripts/
    ├── build_detail_pages.py  # apps.json → 상세 7쪽
    ├── check_site.py          # 깨진 경로·링크 규칙 점검
    └── extract_apps.py        # (개편 때 한 번 씀) 옛 상세 페이지 → apps.json
```

## 자주 하는 일

- **앱 설명 고치기**: `data/apps.json` 수정 → `python3 scripts/build_detail_pages.py`
- **새 앱 추가**: `apps.json`에 항목 추가, `images/logos/<id>.png` 넣기, `index.html`의 「만든 것」 목록에 한 줄 추가 → 상세 페이지 다시 만들기
- **점검**: `python3 scripts/check_site.py` → `0 problems`면 통과
- **미리 보기**: `python3 -m http.server 5178` 후 http://localhost:5178

빌드 과정 없는 정적 사이트라 폴더째 Netlify에 올리면 됩니다.
