"""옛 앱 상세 페이지 7개(Tailwind 판)에서 내용만 뽑아 data/apps.json으로 저장한다. (개편 때 한 번 쓰는 도구)

실행: python3 scripts/extract_apps.py   (반드시 git의 옛 버전 HTML이 있을 때)
"""
import json
import re
import subprocess
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# id, 옛 파일, 메인 목록과 같은 짧은 분류
APPS = [
    ("pepick", "pepick.html", "수업 도구"),
    ("classpet", "classpet.html", "학급 경영"),
    ("dodgeball", "dodgeball.html", "경기 관리"),
    ("jumprope", "jumprope.html", "대회 관리"),
    ("baseball", "baseball.html", "경기 기록"),
    ("pe-mbti", "pe-mbti.html", "재미 · 진단"),
    ("edumole", "edumole.html", "게임 학습"),
]

EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿️]")


def text(s: str) -> str:
    """태그·이모지를 걷어 내고 공백을 정리한 글자만 남긴다."""
    s = re.sub(r"<[^>]+>", " ", s)
    s = EMOJI.sub("", unescape(s))
    return re.sub(r"\s+", " ", s).strip()


def section(html: str, heading: str) -> str:
    """<h2>heading</h2> 다음부터 다음 </section>까지."""
    m = re.search(r"<h2[^>]*>\s*" + re.escape(heading) + r"\s*</h2>(.*?)</section>", html, re.S)
    return m.group(1) if m else ""


def old_html(filename: str) -> str:
    # 개편 전 버전(main 브랜치)에서 읽는다 — 이미 새로 만든 파일을 다시 읽지 않도록
    return subprocess.run(["git", "show", f"main:{filename}"], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def extract(app_id: str, filename: str, short: str) -> dict:
    html = old_html(filename)
    hero = re.search(r"<h1[^>]*>(.*?)</h1>\s*<p[^>]*>(.*?)</p>", html, re.S)
    url = re.search(r'<a href="(https?://[^"]+)"[^>]*>\s*앱 실행하기', html)
    shots = re.findall(r'<img src="(images/screenshots/[^"]+)" alt="([^"]*)"', section(html, "주요 화면"))
    # 기능: <h3|h4>제목</..> 바로 뒤 <p>설명. EduMole처럼 "학생 기능" 같은 묶음 제목(h3 뒤에 목록)이 있으면 group으로 남긴다
    feats = []
    group = ""
    for m in re.finditer(r"<h([34])[^>]*>(.*?)</h\1>\s*(<p[^>]*>(.*?)</p>)?", section(html, "주요 기능"), re.S):
        if m.group(3):
            feats.append((group, m.group(2), m.group(4)))
        else:
            group = text(m.group(2))
    tech = re.findall(r'<p class="text-sm[^"]*mb-2">(.*?)</p>\s*<p class="font-semibold">(.*?)</p>', section(html, "기술 정보"), re.S)
    tech_map = {text(k): text(v) for k, v in tech}
    return {
        "id": app_id,
        "name": text(hero.group(1)),
        "category": short,
        "tagline": text(hero.group(2)),
        "url": url.group(1) if url else "",
        "logo": f"images/logos/{app_id}.png",
        "screenshots": [{"src": s, "alt": text(a)} for s, a in shots],
        "features": [{"group": g, "title": text(t), "desc": text(d)} for g, t, d in feats],
        "tech": {"stack": tech_map.get("사용 기술", ""), "platform": tech_map.get("배포 플랫폼", "")},
    }


if __name__ == "__main__":
    apps = [extract(*a) for a in APPS]
    out = ROOT / "data" / "apps.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(apps, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for a in apps:
        print(f"{a['id']:10} 화면 {len(a['screenshots'])} · 기능 {len(a['features'])} · {a['name']} · {a['url'] or '주소 없음'} · {a['tech']}")
