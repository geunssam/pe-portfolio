# 근쌤의 체육 웹앱 포트폴리오

바이브 코딩으로 개발한 6개의 체육 교육 웹앱을 소개하는 포트폴리오 사이트입니다.

## 📱 포함된 웹앱

1. **DodgeballHub** - 피구 경기 관리 시스템
2. **줄넘기 대회 매니저** - 줄넘기 대회 운영 도구
3. **체육 시간 MBTI** - 체육 성격 유형 진단 테스트
4. **클래스펫** - 게이미피케이션 학급 경영 도우미
5. **야구 경기 기록** - 발야구 점수 관리 시스템
6. **PePick!** - 체육 수업 랜덤 선택 도구

## 🛠️ 기술 스택

- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **스타일링**: Tailwind CSS (CDN)
- **디자인**: Apple Style Minimalism
- **폰트**: Pretendard

## 📁 프로젝트 구조

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
│   └── main.js             # 메인 JavaScript
├── images/
│   ├── screenshots/        # 앱 스크린샷 (추가 예정)
│   └── mockups/            # 목업 이미지 (추가 예정)
└── assets/                 # 기타 에셋
```

## 🚀 로컬 실행 방법

1. 프로젝트 폴더를 엽니다
2. `index.html` 파일을 브라우저에서 실행합니다
3. 또는 로컬 서버를 실행합니다:
   ```bash
   # Python 3
   python3 -m http.server 8000

   # Node.js (http-server 사용)
   npx http-server
   ```

## 📸 스크린샷 추가하기

각 앱의 스크린샷을 추가하려면:

1. `images/screenshots/` 폴더에 스크린샷 저장
2. 각 상세 페이지의 "주요 화면" 섹션에서 이미지 경로 업데이트:

```html
<div class="bg-apple-secondary rounded-2xl aspect-video flex items-center justify-center">
    <img src="images/screenshots/앱이름-1.png" alt="스크린샷" class="w-full h-full object-cover rounded-2xl">
</div>
```

## 🎨 디자인 철학

- **미니멀리즘**: 깔끔한 흰색/회색 기반 애플 스타일
- **명확한 타이포그래피**: Pretendard 폰트 사용
- **부드러운 애니메이션**: 호버 효과와 페이드인 애니메이션
- **완벽한 정렬**: 세심한 간격과 레이아웃

## 📦 배포 방법

### Vercel
```bash
npm install -g vercel
vercel
```

### Netlify
1. Netlify에 로그인
2. 프로젝트 폴더를 드래그 앤 드롭
3. 배포 완료

### GitHub Pages
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin [your-repo-url]
git push -u origin main
```

Settings > Pages에서 main 브랜치 선택

## ✨ 주요 기능

- 반응형 디자인 (데스크톱 우선)
- 부드러운 스크롤 애니메이션
- Intersection Observer 기반 페이드인 효과
- 헤더 스크롤 효과
- 앱 카드 호버 효과

## 📝 라이선스

© 2025 근쌤. All rights reserved.

## 🔗 링크

- **DodgeballHub**: https://dodgeball-app.vercel.app/teacher/dashboard
- **줄넘기 대회 매니저**: https://jumprope-competition-manager.netlify.app/
- **체육 시간 MBTI**: http://pe-playground.com/
- **클래스펫**: http://classpet.netlify.app/
- **야구 경기 기록**: https://baseball-firebase.vercel.app/
- **PePick!**: http://pe-picker.netlify.app/

---

Made with ❤️ by 근쌤
