# -*- coding: utf-8 -*-
"""구조 변경 목업 — 전체 플로우를 한 페이지에"""
import re, os
from logo_data import LOGO_MARK
import mockup_data as D

SRC = open('page.html', encoding='utf-8').read()
CSS = SRC[SRC.index('<style>')+7 : SRC.index('</style>')]

LIFT = [".eyebrow", ".eyebrow .ln", ".pno", "h2.t", ".eyebrow + h2.t", ".kicker-p", ".pspec",
        ".body", ".catch", ".catch::before", ".catch::after",
        ".shots", ".shots.s1", ".shots.s2", ".shots.s3", ".shot", ".shot svg", ".shot figcaption",
        ".tagline", ".storebar", ".sb-l", ".storebar .nmark", ".storebar .nmark svg",
        ".sb-l i", ".sb-c", ".sb-r", ".sb-r svg",
        ".folio", ".folio .num", ".folio .fl", ".logoplate", ".logoplate img",
        ".cover", ".cover .pg", ".cover .hair", ".cover .kicker", ".cover h1", ".cover .title2",
        ".cover .cover-msg", ".cover .foot", ".cover .storebar", ".cover .sb-l i",
        ".cover .sb-c", ".cover .sb-r"]

def rule_of(sel):
    m = re.search(r'(?:^|\n)' + re.escape(sel) + r'\s*\{(.*?)\}', CSS, re.S)
    return m.group(1).strip() if m else None

lifted = []
for sel in LIFT:
    b = rule_of(sel)
    if b: lifted.append(".ui " + sel + "{ " + b + " }")
    else: print("!! 없음:", sel)
DEMO = "\n".join(lifted)

CHEV = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>')
NMARK = ('<span class="nmark"><svg viewBox="0 0 24 24" aria-hidden="true">'
         '<rect width="24" height="24" rx="4.5" fill="#03C75A"/>'
         '<path d="M14.2 12.3 9.9 6.2H6.2v11.6h3.6v-6.1l4.3 6.1h3.7V6.2h-3.6v6.1Z" fill="#fff"/></svg></span>')
SHOT = ('<figure class="shot"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<rect x="3.2" y="5.2" width="17.6" height="13.6" rx="2.2"/><circle cx="9" cy="10.2" r="1.6"/>'
        '<path d="m4.4 17 4.4-4.2 3.3 3 3.1-2.6 4.4 3.8"/></svg><figcaption>사진 한컷</figcaption></figure>')

def storebar():
    return (f'<a class="storebar" href="#">{{}}<span class="sb-c">온새누리장터</span>'
            f'<span class="sb-r">바로가기 {CHEV}</span></a>').format(
            f'<span class="sb-l">{NMARK}<i>네이버</i></span>')

def toc_row(s, n_visible):
    return f'''<a class="toc-item" href="#">
          <span class="tn">{s['code']}</span>
          <span class="tt"><b>{s['group']}</b><i>공급사 <span class="ph">이름</span> · 상품 {n_visible}종</i></span>
          {CHEV}
        </a>'''

n01 = sum(1 for i in D.S01['items'] if not i[3])
n02 = sum(1 for i in D.S02['items'] if not i[3])

ENTRY = f'''<div class="ui"><article class="slide toc">
      <div class="pg">
        <div class="eyebrow"><span>CONTENTS</span><i class="ln"></i></div>
        <h2 class="t">책자를 고르세요</h2>
        <p class="lede">공급사별로 나누어 담았습니다.</p>
        <div class="body">
          <div class="toc-list">
            {toc_row(D.S01, n01)}
            {toc_row(D.S02, n02)}
          </div>
        </div>
        <div class="folio"><span>온새누리장터</span><span class="fl"></span><span>공동구매 상담용 안내</span></div>
      </div>
    </article></div>'''

COVER = f'''<div class="ui"><article class="slide cover">
      <div class="pg">
        <div>
          <div class="logoplate" style="width:6em"><img src="{LOGO_MARK}" alt="온새누리(주)"></div>
          <div class="hair"></div>
          <div class="kicker">Onsaenuri Jangteo</div>
          <h1>온새누리장터<br>이야기</h1>
          <div class="title2">정성을 담아,<br>건강한 일상을 전합니다.</div>
        </div>
        <div>
          <p class="cover-msg">온새누리장터를 찾아주시는 고객님께 진심으로 감사드립니다.<br>좋은 상품을 정성껏 선별하고, 정직하게 전하겠습니다.</p>
          {storebar()}
          <div class="hair"></div>
          <div class="foot"><span>공동구매 상담용 안내</span><span>2026</span></div>
        </div>
      </div>
    </article></div>'''

s = D.SAMPLE_02
PROD = f'''<div class="ui"><article class="slide">
      <div class="pg">
        <div class="eyebrow"><span>{s['cat']}</span><i class="ln"></i><span class="pno">{s['no']}</span></div>
        <div class="kicker-p">{s['kicker']}</div>
        <h2 class="t">{s['name']}</h2>
        <div class="pspec">{s['spec']}</div>
        <div class="body">
          <p class="catch">{s['catch']}</p>
          <div class="shots s{s['shots']}">{SHOT*s['shots']}</div>
          <p class="tagline">{s['tag']}</p>
          {storebar()}
        </div>
        <div class="folio"><span>{s['cat']}</span><span class="fl"></span><span class="num">04</span></div>
      </div>
    </article></div>'''

def strip(s, start_at=3):
    cards = ['<div class="pcard fixed"><span class="pn">01</span><span class="pt">표지</span></div>',
             '<div class="pcard fixed"><span class="pn">02</span><span class="pt">인사말</span></div>']
    n = start_at
    for no, name, spec, hide in s['items']:
        if hide:
            cards.append(f'<div class="pcard off"><span class="pn">—</span><span class="pt">{name}</span><span class="ps">{no} · 숨김</span></div>')
            continue
        cards.append(f'<div class="pcard"><span class="pn">{n:02d}</span><span class="pt">{name}</span><span class="ps">{no} · {spec}</span></div>')
        n += 1
    cards.append(f'<div class="pcard fixed"><span class="pn">{n:02d}</span><span class="pt">맺음말</span></div>')
    return "\n".join(cards), n

st01, tot01 = strip(D.S01)
st02, tot02 = strip(D.S02)

open('_mockup_parts.py','w',encoding='utf-8').write("")
import json
json.dump(dict(DEMO=DEMO, ENTRY=ENTRY, COVER=COVER, PROD=PROD,
               ST01=st01, ST02=st02, TOT01=tot01, TOT02=tot02,
               N01=n01, N02=n02, LOGO=LOGO_MARK),
          open('_mockup.json','w',encoding='utf-8'), ensure_ascii=False)
print(f"01 책자 {tot01}장 (상품 {n01}) / 02 책자 {tot02}장 (상품 {n02})")

# ---- 조립 ----
body = open('mockup-body.html', encoding='utf-8').read()
for k, v in [('__DEMO__', DEMO), ('__LOGO__', LOGO_MARK), ('__ENTRY__', ENTRY),
             ('__COVER__', COVER), ('__PROD__', PROD), ('__ST01__', st01), ('__ST02__', st02),
             ('__TOT01__', str(tot01)), ('__TOT02__', str(tot02))]:
    body = body.replace(k, v)

open('mockup-page.html', 'w', encoding='utf-8').write(body)
h, _, rest = body.partition('</style>')
open('mockup.html', 'w', encoding='utf-8').write(f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="온새누리장터 책자 구조 변경안 — 공급사 2곳">
<meta name="theme-color" content="#0E5C4F" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0D100F" media="(prefers-color-scheme: dark)">
<link rel="icon" href="favicon.ico" sizes="any">
{h.strip()}
</style>
</head>
<body>
{rest.strip()}
</body>
</html>
''')
os.remove('_mockup.json'); os.remove('_mockup_parts.py')
print("mockup.html:", round(os.path.getsize('mockup.html')/1024,1), "KB")
