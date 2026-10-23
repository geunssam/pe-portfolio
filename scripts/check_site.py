"""사이트 점검: 깨진 파일 경로, 새 탭 링크 규칙, 남은 옛 흔적을 찾아 개수를 알려 준다.

실행: python3 scripts/check_site.py   → 마지막 줄이 "0 problems"면 통과
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DETAIL = ["pepick", "classpet", "dodgeball", "jumprope", "pe-mbti", "baseball", "edumole"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
FORBIDDEN = ["cdn.tailwindcss.com", "css/style.css", "apple-blue"]


def check_page(path: Path) -> list:
    html = path.read_text(encoding="utf-8")
    problems = []

    # 1) 로컬 파일 경로(src, href)가 실제로 있는지
    for attr, ref in re.findall(r'\b(src|href)="([^"]+)"', html):
        if re.match(r"(https?:|mailto:|#|data:)", ref):
            continue
        target = (ROOT / ref.split("#")[0]).resolve()
        if not target.exists():
            problems.append(f"없는 파일: {ref}")

    # 2) 바깥 링크는 새 탭 + noopener
    for tag in re.findall(r"<a\b[^>]*href=\"https?://[^\"]+\"[^>]*>", html):
        if 'target="_blank"' not in tag or 'rel="noopener noreferrer"' not in tag:
            problems.append(f"새 탭 규칙 빠짐: {tag[:80]}")

    # 3) 옛 디자인 흔적·이모지
    for word in FORBIDDEN:
        if word in html:
            problems.append(f"옛 흔적: {word}")
    if EMOJI.search(html):
        problems.append(f"이모지: {EMOJI.search(html).group()}")
    return problems


def main() -> int:
    total = 0
    pages = [ROOT / "index.html"] + [ROOT / f"{d}.html" for d in DETAIL]
    for page in pages:
        if not page.exists():
            print(f"{page.name}: 페이지 없음")
            total += 1
            continue
        for p in check_page(page):
            print(f"{page.name}: {p}")
            total += 1
    print(f"{total} problems")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
