"""data/apps.json → 앱 상세 페이지 7개(pepick.html 등)를 만든다.

앱 설명을 고치고 싶으면 data/apps.json을 고친 뒤 다시 실행:
    python3 scripts/build_detail_pages.py
"""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXT = 'target="_blank" rel="noopener noreferrer"'

HEAD = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{name} · 근쌤의 서재</title>
  <meta name="description" content="{tagline}">
  <meta name="theme-color" content="#F6F8FC">
  <meta property="og:title" content="{name} · 근쌤의 서재">
  <meta property="og:description" content="{tagline}">
  <meta property="og:image" content="https://geunssam-library.netlify.app/images/brand/og-image.png">
  <link rel="icon" href="images/brand/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="images/brand/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="images/brand/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gothic+A1:wght@400;700;900&family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap">
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/detail.css">
</head>
<body class="sunlight">
"""


def features_html(features: list) -> str:
    """기능 목록. group이 있으면(EduMole) 묶음마다 작은 제목을 단다."""
    groups: dict = {}
    for f in features:
        groups.setdefault(f.get("group", ""), []).append(f)
    out = []
    for group, items in groups.items():
        if group:
            out.append(f'<h3 class="feature-group">{escape(group)}</h3>')
        rows = "".join(
            f'<li class="feature"><b>{escape(f["title"])}</b><span>{escape(f["desc"])}</span></li>' for f in items
        )
        out.append(f'<ul class="list features">{rows}</ul>')
    return "\n        ".join(out)


def page(app: dict, apps: list) -> str:
    shots = "".join(
        f'<figure class="shot"><img src="{escape(s["src"])}" alt="{escape(s["alt"])}" loading="lazy"></figure>'
        for s in app["screenshots"]
    )
    tech = " · ".join(v for v in (app["tech"].get("stack"), app["tech"].get("platform")) if v)
    others = "".join(
        f'<li><a class="row" href="{o["id"]}.html"><img src="{escape(o["logo"])}" alt=""><span class="row-name">{escape(o["name"])}</span><span class="row-meta">{escape(o["category"])}</span></a></li>'
        for o in apps if o["id"] != app["id"]
    )
    launch = (
        f'<a class="btn" href="{escape(app["url"])}" {EXT}>앱 실행하기 →</a>' if app["url"] else ""
    )
    return HEAD.format(name=escape(app["name"]), tagline=escape(app["tagline"])) + f"""
  <header class="topbar">
    <div class="wrap topbar-inner">
      <a class="brand" href="index.html#made">← 근쌤</a>
    </div>
  </header>

  <main>
    <section class="detail-hero">
      <div class="wrap detail-hero-inner">
        <img class="app-logo" src="{escape(app["logo"])}" alt="" width="72" height="72">
        <p class="detail-category">{escape(app["category"])}</p>
        <h1 class="detail-title">{escape(app["name"])}</h1>
        <p class="detail-tagline">{escape(app["tagline"])}</p>
        <div class="stripe" aria-hidden="true"><i></i><i></i><i></i></div>
        {launch}
      </div>
    </section>

    <section class="detail-block" aria-label="주요 화면">
      <div class="shots" tabindex="0">{shots}</div>
    </section>

    <section class="detail-block">
      <div class="wrap detail-grid">
        <h2 class="detail-h2">주요 기능</h2>
        <div class="detail-col">
        {features_html(app["features"])}
        <p class="small tech">만든 도구 · {escape(tech)}</p>
        </div>
      </div>
    </section>

    <section class="detail-block">
      <div class="wrap detail-grid">
        <h2 class="detail-h2">다른 앱</h2>
        <ul class="list detail-col">{others}</ul>
      </div>
    </section>
  </main>

  <footer class="wrap footer">© 근쌤의 서재</footer>
</body>
</html>
"""


if __name__ == "__main__":
    apps = json.loads((ROOT / "data" / "apps.json").read_text(encoding="utf-8"))
    for app in apps:
        (ROOT / f"{app['id']}.html").write_text(page(app, apps), encoding="utf-8")
        print(f"{app['id']}.html")
