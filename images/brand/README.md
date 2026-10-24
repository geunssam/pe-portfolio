# 근쌤의 서재 브랜드 에셋

| 파일 | 크기 | 용도 |
| --- | --- | --- |
| `favicon.svg` | 512×512 · viewBox 512×512 | 브라우저 탭 아이콘. `icon-512.png`를 base64로 내장한 SVG입니다. |
| `favicon-16.png` | 16×16 px | 작은 브라우저 탭용 PNG 파비콘 |
| `favicon-32.png` | 32×32 px | PNG 파비콘 |
| `apple-touch-icon.png` | 180×180 px | iPhone·iPad 홈 화면 아이콘. 정사각형 배경은 `#F6F8FC`이며 모서리 처리는 기기에 맡깁니다. |
| `icon-512.png` | 512×512 px | 고해상도 아이콘·웹 앱 manifest용 |
| `og-image.png` | 1200×630 px | 카카오톡·슬랙 등의 링크 미리보기 |
| `brand-preview.png` | 1440×1320 px | 전체 확인용. 16·32px PNG의 실제 크기와 확대 표시를 함께 포함하며 사이트 연결은 불필요합니다. |
| `README.md` | 텍스트 | 파일 설명과 연결 예시 |

## HTML 연결 예시

사이트 루트의 HTML `<head>` 안에 추가합니다. HTML 파일은 이번 작업에서 수정하지 않았습니다.

```html
<link rel="icon" href="images/brand/icon-512.png" sizes="512x512" type="image/png">
<link rel="icon" href="images/brand/favicon-16.png" sizes="16x16" type="image/png">
<link rel="icon" href="images/brand/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="images/brand/favicon.svg" type="image/svg+xml" sizes="any">
<link rel="apple-touch-icon" href="images/brand/apple-touch-icon.png" sizes="180x180">

<meta property="og:image" content="https://YOUR-DOMAIN.example/images/brand/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
<meta property="og:image:alt" content="근쌤의 서재 — 읽고, 생각하고, 쓰거나 만듭니다.">
```

`YOUR-DOMAIN.example`은 실제 배포 도메인으로 바꿉니다. `og:image`에는 공개된 절대 URL을 사용합니다. 하위 경로의 HTML에서는 아이콘 경로도 해당 위치에 맞춥니다.

## 아이콘 구성

첫 화면과 같은 기존 캐릭터 `images/profile/geunssam-wave.png`를 얼굴·머리 중심으로 크게 잘라 사용했습니다. 원본 좌표의 `(70, -25)`부터 `(430, 335)`까지를 정사각형으로 잡아, 머리와 눈이 작은 크기에서도 보이도록 구성했습니다. 원본 바깥 영역은 투명하게 처리한 뒤 연한 하늘색 `#DCE7F8` 원 위에 배치했습니다.

`favicon-16.png`, `favicon-32.png`, `icon-512.png`와 SVG는 원형 바깥이 투명합니다. `apple-touch-icon.png`만 원 바깥을 포함한 정사각형 전체에 `#F6F8FC` 배경을 채웠습니다. 작은 PNG 두 장은 축소 후 눈과 머리 윤곽을 약하게 선명하게 처리했습니다. 아이콘에는 ‘근’ 글자나 M 세 줄 띠가 없습니다.

`og-image.png`는 변경하지 않았습니다. OG 이미지의 제목은 Apple SD Gothic Neo Heavy, 설명은 Medium으로 렌더링되어 PNG 자체에 포함되어 있습니다. `brand-preview.png` 상단의 기존 OG 미리보기도 유지했습니다. 외부 다운로드 없이 로컬 원본만 사용했습니다.
