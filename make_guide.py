# -*- coding: utf-8 -*-
"""UI 가이드 생성 — page.html 의 실제 CSS 를 그대로 떼어와 예시를 렌더한다."""
import re, os
from logo_data import LOGO_MARK

SRC = open('page.html', encoding='utf-8').read()
CSS = SRC[SRC.index('<style>')+7 : SRC.index('</style>')]

# 예시로 보여줄 컴포넌트의 실제 규칙을 page.html 에서 그대로 떼어온다
LIFT = [
 ".eyebrow", ".eyebrow .ln", ".pno", ".eyebrow + h2.t", ".kicker-p", "h2.t", ".pspec",
 ".catch", ".catch::before", ".catch::after",
 ".shots", ".shots.s1", ".shots.s2", ".shots.s3",
 ".shot", ".shot svg", ".shot.filled", ".shot.filled img", ".shot figcaption",
 ".tagline",
 ".storebar", ".storebar:hover", ".sb-l", ".storebar .nmark", ".storebar .nmark svg",
 ".sb-l i", ".sb-c", ".sb-r", ".sb-r svg",
 ".folio", ".folio .num", ".folio .fl",
 ".creed", ".creed span:last-child", ".note",
 ".kv", ".kv div", ".kv b", ".kv span",
 ".logoplate", ".logoplate img",
 ".cover", ".cover .hair", ".cover .kicker", ".cover h1", ".cover .title2",
 ".cover .cover-msg", ".cover .storebar", ".cover .sb-l i", ".cover .sb-c",
 ".cover .sb-r", ".cover .foot",
 ".backcov", ".backcov .hair", ".backcov .thanks", ".backcov .thanks-ko",
 ".backcov .thanks-q", ".backcov .kv b", ".backcov .kv span",
 ".backcov .qr", ".backcov .qr svg", ".backcov .qr span", ".backcov .note",
 ".nav", ".nav:hover:not(:disabled)", ".nav:disabled", ".nav svg",
 ".dots", ".dot", ".dot:hover", ".dot.on", ".counter",
]

def rule_of(sel):
    pat = re.compile(r'(?:^|\n)' + re.escape(sel) + r'\s*\{(.*?)\}', re.S)
    m = pat.search(CSS)
    return m.group(1).strip() if m else None

lifted, missing = [], []
for sel in LIFT:
    body = rule_of(sel)
    if body is None:
        missing.append(sel); continue
    scoped = ", ".join(".ui " + s.strip() for s in sel.split(","))
    lifted.append(f"{scoped}{{ {body} }}")
DEMO_CSS = "\n".join(lifted)
if missing:
    print("!! 못 찾은 셀렉터:", missing)

open('_demo.css', 'w', encoding='utf-8').write(DEMO_CSS)
print("떼어온 규칙:", len(lifted), "개")

# ---- 조립 ----
body = open('ui-guide-body.html', encoding='utf-8').read()
body = body.replace('__DEMO_CSS__', DEMO_CSS).replace('__LOGO__', LOGO_MARK)

# 1) Artifact 용 (본문만)
open('ui-guide-page.html', 'w', encoding='utf-8').write(body)

# 2) GitHub Pages 용 (완전한 문서)
h, _, rest = body.partition('</style>')
open('ui-guide.html', 'w', encoding='utf-8').write(f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="온새누리장터 안내 페이지의 색·서체·부품과 운영 규칙">
<meta name="theme-color" content="#0E5C4F" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0D100F" media="(prefers-color-scheme: dark)">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
{h.strip()}
</style>
</head>
<body>
{rest.strip()}
</body>
</html>
''')
os.remove('_demo.css')
print("ui-guide.html:", round(os.path.getsize('ui-guide.html')/1024,1), "KB")
