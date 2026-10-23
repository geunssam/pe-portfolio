# 근쌤 활동 소개 사이트 개편 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `pe-portfolio`를 "체육 웹앱 모음"에서 「햇살 드는 서재」 디자인의 근쌤 활동 소개 사이트로 바꾼다.

**Architecture:** 빌드 없는 정적 사이트(HTML + CSS + 바닐라 JS). 메인 `index.html`은 손으로 쓰고, 앱 상세 7쪽은 `data/apps.json` 한 곳의 내용으로 `scripts/build_detail_pages.py`가 만들어 낸다(만든 HTML도 저장소에 커밋 — 배포 때 빌드 불필요).

**Tech Stack:** HTML5, CSS(사용자 정의 속성), 바닐라 JS, Python 3 표준 라이브러리(상세 페이지 생성·점검), Google Fonts(Gothic A1 · IBM Plex Sans KR · IBM Plex Mono).

**Spec:** `docs/superpowers/specs/2026-10-24-portfolio-redesign-design.md`

## Global Constraints

- 색: 바탕 `#F6F8FC`, 글씨 `#0E1E46`, 보조 글씨 `#56627D`, 선 `#DFE5EF`, 하늘 `#3D7BE0`, 노을 `#F2A65A`, M 세 줄 `#5CB4E6` · `#1E3F95` · `#E2261C`.
- 글꼴: 제목 Gothic A1 900, 본문 IBM Plex Sans KR, 표시·숫자 IBM Plex Mono.
- 카드 대신 얇은 선 목록. 진한 상자는 한 화면에 최대 하나. 이모지·01/02/03 장식 금지.
- 화면마다 큰 문장 하나 + 작은 글 한 줄 이하.
- 확인 안 된 숫자 금지. 쓰는 숫자는 "체육 웹앱 7개"뿐.
- 링크: 브런치 `https://brunch.co.kr/@zoomwk`, 유튜브 `https://www.youtube.com/@geunssam`. 인스타그램 없음. 연락 버튼 = 브런치 링크.
- 강의 네 줄: "NotebookLM · Gemini", "Claude · ChatGPT", "Codex · Claude Code 바이브코딩", "학교 AX 전환". 출강처 한 줄: "지식샘터 · 창비교육 선도교사 연수 · 학교 출강".
- 상세 페이지 주소 7개 유지: `pepick.html classpet.html dodgeball.html jumprope.html pe-mbti.html baseball.html edumole.html`.
- `prefers-reduced-motion: reduce`면 움직임 전부 끔. 콘텐츠는 처음부터 보이는 상태(opacity 0으로 숨겨 두고 기다리지 않음).
- 테스트 코드는 근쌤 요청 시에만 (CLAUDE.md) → 확인은 `scripts/check_site.py` 점검 스크립트 + 헤드리스 크롬 캡처로 한다.

## Review Focus

- 휴대폰 너비 375px에서 가로 스크롤이 생기지 않아야 한다 → Task 4 캡처 점검.
- JS가 꺼지거나 실패해도 메뉴 4개와 앱 7개가 모두 보여야 한다(펼치기는 JS로 "접는" 방식) → Task 2.
- 앱 로고·스크린샷 경로가 하나라도 깨지면 안 된다 → `check_site.py`가 모든 `src`/`href` 로컬 파일 존재 확인.
- 외부 링크(앱 실행, 브런치, 유튜브)는 새 탭 + `rel="noopener noreferrer"` → `check_site.py`.
- 앱 상세 페이지 내용(기능 설명·스크린샷)이 옮기다 빠지면 안 된다 → Task 3에서 옛 페이지와 개수 비교.

---

### Task 1: 브랜치 · 디자인 기본 파일

**Files:**
- Modify: `.gitignore` (`.superpowers/` 추가)
- Create: `images/profile/geunssam-wave.png` (← `~/Desktop/geunssam-video-studio/ai7030-intro/public/char/hires-wave.png`)
- Create: `css/tokens.css` (Global Constraints의 색·글꼴을 `--paper --ink --soft --hair --sky --sun --m-light --m-dark --m-red --f-display --f-body --f-mono`로), `css/base.css` (리셋, 본문 글꼴, `.stripe` M 세 줄 띠, `.wrap` 폭 1100px + 옆 여백 `max(20px, env(safe-area-inset-*))`, `.list` 얇은 선 목록, `.btn`, 노을빛 배경)

- [ ] `git checkout -b redesign/seojae`
- [ ] 위 파일 작성
- [ ] Commit: `chore: 서재 디자인 기본 색·글꼴 파일 추가`

### Task 2: 메인 페이지

**Files:**
- Rewrite: `index.html` — 섹션 id: `#top`(첫 화면) `#made`(만든 것) `#writing`(쓴 글) `#lectures`(강의) `#contact`(함께 일하기)
- Create: `css/home.css`
- Rewrite: `js/main.js` — `initMenu()`(휴대폰 메뉴 패널 열고 닫기, Esc로 닫기), `initAppList()`(앱 목록 5번째부터 접고 "7개 모두 보기"로 펼침 — JS 없으면 전부 보임), `initReveal()`(IntersectionObserver로 `.is-in` 붙여 살짝 떠오르게, 기본 상태는 보임)

- [ ] 섹션별 문구는 Spec 4장 표와 Global Constraints 그대로. 쓴 글 3편은 `brunch.co.kr/@zoomwk`에서 가져온 실제 제목·주소.
- [ ] 헤드리스 크롬으로 375px·1280px 캡처해 눈으로 확인
- [ ] Commit: `feat: 메인 페이지를 근쌤의 서재 디자인으로 개편`

### Task 3: 앱 상세 페이지 7개

**Files:**
- Create: `data/apps.json` — 옛 7쪽에서 뽑은 `[{id, name, category, tagline, url, logo, screenshots:[{src, alt}], features:[{title, desc}], tech:{stack, platform}}]` (이모지 제외)
- Create: `scripts/extract_apps.py` (한 번 쓰는 추출기, 옛 HTML → apps.json), `scripts/build_detail_pages.py` (`apps.json` → 7개 HTML)
- Create: `css/detail.css`
- Rewrite: 7개 상세 HTML (생성물)

- [ ] 추출 후 각 앱의 스크린샷 수·기능 수가 옛 페이지와 같은지 출력해서 확인
- [ ] 상세 구성: "← 근쌤" · 분류 · 앱 이름 · 한 줄 소개 · 앱 실행하기 버튼 · 스크린샷 가로 스크롤 줄 · 기능 목록(선 나눔, 제목 + 한 줄) · 사용 기술 한 줄 · 다른 앱(로고 + 이름 한 줄 목록)
- [ ] Commit: `feat: 앱 상세 페이지를 데이터 기반으로 다시 생성`

### Task 4: 점검 · 정리

**Files:**
- Create: `scripts/check_site.py` — 모든 HTML의 로컬 `src`/`href` 파일 존재, 외부 링크 `target="_blank" rel="noopener noreferrer"`, 금지 요소(이모지, `cdn.tailwindcss.com`, `style.css` 참조) 없음, 상세 페이지 7개 존재를 점검하고 문제 개수를 출력(0이면 통과)
- Modify: `README.md` (구조·페이지 만드는 법 갱신)

- [ ] `python3 scripts/check_site.py` → `0 problems`
- [ ] 375px·1280px 캡처(메인 + 상세 1쪽), 가로 스크롤 없음 확인
- [ ] `css/style.css`는 더 이상 안 쓰지만 **지우지 않고** 근쌤 확인을 받는다
- [ ] Commit: `chore: 사이트 점검 스크립트와 README 갱신`
