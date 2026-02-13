# PRD: 체육 교사 웹앱 포트폴리오 사이트

## 📋 프로젝트 개요

**목적**: 초등교사이자 개발자인 '근쌤'이 바이브 코딩으로 개발한 6개의 체육 교육 웹앱을 소개하는 포트폴리오 사이트

**타겟 사용자**:
- 동료 교사들
- 교육 기술에 관심 있는 교육자
- 포트폴리오 방문자

**기술 스택**:
- Vanilla JavaScript
- HTML5 + CSS3
- Tailwind CSS (스타일링)
- 데스크톱 우선 반응형 디자인

---

## 🎨 디자인 철학

**스타일**: 애플 스타일 미니멀리즘
- 깔끔한 흰색/회색 기반 색상 팔레트
- 넓은 여백과 명확한 타이포그래피
- 부드러운 그림자와 라운드 코너
- 세밀한 간격과 정렬

**주요 원칙**:
- 텍스트 줄바꿈 최소화 (단어 중간에서 끊기지 않도록)
- 완벽한 정렬과 일관된 간격
- 한 눈에 들어오는 정보 구조
- 과하지 않은 애니메이션

---

## 📐 사이트 구조

### 1. 메인 페이지 (`index.html`)

**구성 요소**:

1. **헤더 (Header)**
   - 로고/이름: "근쌤의 체육 웹앱"
   - 간단한 네비게이션 (Home, About, Apps)
   - 고정 헤더 (스크롤 시 투명도 변화)

2. **히어로 섹션 (Hero Section)**
   - 메인 타이틀: "체육 수업을 바꾸는 디지털 도구"
   - 서브 타이틀: "초등교사가 만든, 현장을 위한 웹앱"
   - 간단한 자기소개 (2-3줄)
     - "초등학교 체육 전담 교사"
     - "바이브 코딩으로 교육 현장의 문제를 해결합니다"
   - CTA 버튼: "웹앱 둘러보기" (앱 섹션으로 스크롤)

3. **앱 그리드 섹션 (Apps Grid)**
   - 섹션 타이틀: "개발한 웹앱들"
   - 6개 앱 카드 (2열 x 3행 그리드)
   - 각 카드 구성:
     - 앱 스크린샷 (목업 이미지)
     - 앱 이름
     - 한 줄 설명
     - "자세히 보기" 버튼 → 상세 페이지 링크

4. **푸터 (Footer)**
   - 버전 정보: "v1.0.0"
   - 제작 정보: "Made with ❤️ by 근쌤"
   - 제작 연도: "2025"
   - 간단한 링크 (GitHub, Blog 등 - 선택사항)

### 2. 상세 페이지 (6개 - 각 앱별)

**파일명**:
- `dodgeball.html`
- `jumprope.html`
- `pe-mbti.html`
- `classpet.html`
- `baseball.html`
- `pepick.html`

**구성 요소**:

1. **헤더** (메인과 동일)

2. **앱 소개 섹션**
   - 앱 이름 (큰 제목)
   - 한 줄 설명
   - 배지: "체육 수업 도구" / "학급 경영" 등 카테고리
   - "앱 실행하기" 버튼 (실제 앱 링크)

3. **스크린샷 갤러리**
   - 2-3개의 주요 화면 스크린샷
   - 캡션과 함께 표시

4. **주요 기능 섹션**
   - 아이콘 + 기능명 + 설명 (3-5개)
   - 깔끔한 리스트 형태

5. **기술 정보**
   - 사용 기술: React / Next.js / PWA 등
   - 배포 플랫폼: Vercel / Netlify
   - 개발 기간 (선택사항)

6. **다른 앱 보기**
   - 다른 5개 앱의 썸네일 링크
   - 수평 스크롤 카드

7. **푸터** (메인과 동일)

---

## 📱 웹앱 정보

### 1. DodgeballHub
- **URL**: https://dodgeball-app.vercel.app/teacher/dashboard
- **설명**: 초등학교 피구 경기를 쉽게 관리하는 교사용 시스템
- **주요 기능**:
  - 경기 일정 관리
  - 팀 구성 및 점수 기록
  - 대시보드로 한눈에 현황 파악
- **기술**: Next.js, React
- **카테고리**: 체육 경기 관리

### 2. 줄넘기 대회 매니저
- **URL**: https://jumprope-competition-manager.netlify.app/
- **설명**: 줄넘기 대회 운영을 위한 종합 관리 도구
- **주요 기능**:
  - 대회 일정 관리
  - 참가자 등록 및 기록
  - 실시간 순위 집계
- **기술**: React, Lucide Icons
- **카테고리**: 체육 대회 관리

### 3. 근쌤의 체육 시간 MBTI
- **URL**: http://pe-playground.com/
- **설명**: 체육 시간 성격 유형을 재미있게 진단하는 테스트
- **주요 기능**:
  - 오리지널 체육 MBTI 테스트
  - 동물농장 버전
  - 파워업 메뉴 버전
- **기술**: React
- **카테고리**: 재미/진단

### 4. 클래스펫
- **URL**: http://classpet.netlify.app/
- **설명**: 게이미피케이션을 활용한 학급 경영 도우미
- **주요 기능**:
  - 펫 농장 시스템
  - 칭찬 스티커 관리
  - 학생 감정 추적 (마음)
  - 시간표 관리
  - 통계 및 펫 도감
- **기술**: PWA, Service Worker
- **카테고리**: 학급 경영

### 5. 야구 경기 기록
- **URL**: https://baseball-firebase.vercel.app/
- **설명**: 발야구 경기의 점수와 기록을 실시간으로 관리
- **주요 기능**:
  - 실시간 점수 입력
  - 경기 기록 저장
  - 모바일 최적화 UI
- **기술**: Firebase, 모바일 최적화
- **카테고리**: 체육 경기 관리

### 6. PePick!
- **URL**: http://pe-picker.netlify.app/
- **설명**: 체육 수업에 필요한 랜덤 선택 도구 모음
- **주요 기능**:
  - 술래뽑기 (술래/천사 선정, 타이머)
  - 모둠뽑기 (랜덤 그룹 배정)
  - 학급 관리 (학생 명단, CSV 연동)
- **기술**: React v2.0.0
- **카테고리**: 체육 수업 도구

---

## 🎯 개발 우선순위

### Phase 1: 기본 구조 (95% 완성도)
1. ✅ 프로젝트 폴더 구조 생성
2. ✅ 메인 페이지 HTML 구조
3. ✅ Tailwind CSS 설정
4. ✅ 헤더 + 히어로 섹션
5. ✅ 앱 그리드 (6개 카드)
6. ✅ 푸터
7. ✅ 기본 라우팅 (Vanilla JS)

### Phase 2: 상세 페이지 (각 앱별)
8. ✅ 상세 페이지 템플릿 생성
9. ✅ 6개 앱 정보 입력
10. ✅ 스크린샷 준비 영역
11. ✅ 기능 설명 섹션
12. ✅ 다른 앱 추천 섹션

### Phase 3: 스타일링 & 인터랙션
13. ✅ 애플 스타일 디자인 적용
14. ✅ 호버 효과 및 애니메이션
15. ✅ 부드러운 스크롤
16. ✅ 반응형 조정 (데스크톱 우선)

### Phase 4: 마무리
17. ✅ 크로스 브라우저 테스트
18. ✅ 성능 최적화
19. ✅ 실제 스크린샷 추가 (사용자 제공)
20. ✅ 배포 준비

---

## 📁 파일 구조

```
pe-portfolio/
├── index.html              # 메인 페이지
├── dodgeball.html          # 피구 앱 상세
├── jumprope.html           # 줄넘기 앱 상세
├── pe-mbti.html            # MBTI 앱 상세
├── classpet.html           # 클래스펫 상세
├── baseball.html           # 야구 앱 상세
├── pepick.html             # PePick 상세
├── css/
│   └── style.css           # 커스텀 스타일
├── js/
│   ├── main.js             # 메인 로직
│   ├── router.js           # 페이지 라우팅
│   └── animations.js       # 애니메이션 효과
├── images/
│   ├── screenshots/        # 앱 스크린샷
│   │   ├── dodgeball-1.png
│   │   ├── dodgeball-2.png
│   │   └── ...
│   └── mockups/            # 목업 이미지
└── assets/
    └── favicon.ico
```

---

## 🎨 색상 팔레트 (애플 스타일)

```css
/* Primary Colors */
--primary-bg: #FFFFFF;
--secondary-bg: #F5F5F7;
--tertiary-bg: #E8E8ED;

/* Text Colors */
--text-primary: #1D1D1F;
--text-secondary: #6E6E73;
--text-tertiary: #86868B;

/* Accent Colors */
--accent-blue: #0071E3;
--accent-hover: #0077ED;

/* Borders & Shadows */
--border-light: #D2D2D7;
--shadow-sm: rgba(0, 0, 0, 0.05);
--shadow-md: rgba(0, 0, 0, 0.1);
--shadow-lg: rgba(0, 0, 0, 0.15);
```

---

## 📏 타이포그래피

```css
/* Font Family */
--font-korean: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* Font Sizes */
--text-xs: 12px;
--text-sm: 14px;
--text-base: 16px;
--text-lg: 18px;
--text-xl: 20px;
--text-2xl: 24px;
--text-3xl: 32px;
--text-4xl: 48px;
--text-5xl: 64px;

/* Font Weights */
--weight-regular: 400;
--weight-medium: 500;
--weight-semibold: 600;
--weight-bold: 700;
```

---

## ✨ 인터랙션 & 애니메이션

1. **헤더 스크롤 효과**
   - 스크롤 시 배경 투명도 증가
   - 부드러운 그림자 추가

2. **앱 카드 호버**
   - 살짝 위로 이동 (translateY: -8px)
   - 그림자 강도 증가
   - 부드러운 transition (0.3s ease)

3. **버튼 효과**
   - 호버 시 배경색 변화
   - 클릭 시 scale(0.98) 효과

4. **스크롤 애니메이션**
   - Intersection Observer 사용
   - 요소가 뷰포트에 들어올 때 fade-in

5. **페이지 전환**
   - 부드러운 fade 효과
   - 스크롤 위치 초기화

---

## 🚀 배포 계획

**선택지**:
1. Vercel (권장)
2. Netlify
3. GitHub Pages

**도메인**:
- 추후 결정 (pe-apps.com, teacher-wongeun.com 등)

---

## ✅ 완성 기준

1. **기능**
   - ✅ 메인 페이지에서 6개 앱 카드 표시
   - ✅ 각 앱 상세 페이지로 이동
   - ✅ 실제 앱으로 연결되는 링크 작동
   - ✅ 부드러운 스크롤 및 네비게이션

2. **디자인**
   - ✅ 애플 스타일 미니멀 디자인 구현
   - ✅ 완벽한 텍스트 정렬 (줄바꿈 없음)
   - ✅ 일관된 간격과 여백
   - ✅ 세련된 호버 효과

3. **성능**
   - ✅ 빠른 로딩 속도
   - ✅ 부드러운 애니메이션
   - ✅ 크로스 브라우저 호환

4. **사용자 경험**
   - ✅ 직관적인 네비게이션
   - ✅ 명확한 정보 전달
   - ✅ 모바일에서도 기본 작동

---

**작성일**: 2025-02-12
**버전**: 1.0
**작성자**: Claude Code with 근쌤
