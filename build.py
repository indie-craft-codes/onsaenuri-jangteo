# -*- coding: utf-8 -*-
"""온새누리장터 공동구매 홍보물 - 페이지 데이터에서 index.html 생성"""

from photo_data import PHOTOS
from logo_data import LOGO_FULL, LOGO_MARK, LOGO_FULL_W, LOGO_FULL_H

# 책자 — 상품번호 앞 두 자리가 곧 공급사다 (01-xxx / 02-xxx)
BOOKLETS = [
    dict(code="01", title="한우 · 한돈 · 커피 · 아트"),
    dict(code="02", title="떡 · 전통 디저트"),
]
TOC_TITLE = "책자를 고르세요"
TOC_LEDE  = "공급사별로 나누어 담았습니다."

STORE_URL = "https://m.smartstore.naver.com/onsaynuri"   # 온새누리장터 스마트스토어

# 상품별 개별 링크. 상품번호 -> URL. 비어 있으면 스토어 홈(STORE_URL)으로 연결된다.
_P = "https://m.smartstore.naver.com/onsaynuri/products/"
PRODUCT_URLS = {
    "01-001":    _P + "13665434324",   # ILJO 시그니처 콜드브루 원액 1L (NOMAD BLEND)
    # "01-002" 제주유채꽃도새기 한돈3종세트 — 스토어에 등록된 상품 없음 (스토어 홈으로 연결)
    "01-003":    _P + "11787679996",   # 숙성&시즈닝[1.2kg] 정통 육가공 마이스터 한돈 왕돈마호크 400gx3팩
    "01-004":    _P + "11310868903",   # 초이스등급 명품 LA꽃갈비 선물세트 1.8kg
    # "01-005" 찐보리굴비 — 스토어에 없음 (현재 숨김)
    # "01-006" 매콤탱쭈꾸미 — 스토어에 없음 (현재 숨김)
    "01-007(A)": _P + "11225571767",   # 궁중레시피 명품본가 한우 떡갈비 선물세트 실속형
    "01-007(B)": _P + "11306281715",   # 궁중레시피 명품본가 한우떡갈비세트 고급형 1.36kg
    "01-007(C)": _P + "11306288666",   # 궁중레시피 명품본가 한우 떡갈비 선물세트 프리미엄형 1.7kg
    "01-008":    _P + "13208394554",   # 이중섭 판화 컬렉션 20종 실크스크린 아트에디션 4호 액자포함
}

PRODUCTS = [
    dict(no="01-001", cat="커피", kicker="ILJO 시그니처",
         name="콜드브루 원액 1L", sub="NOMAD BLEND",
         catch="필요할 때 언제든 꺼내 집, 사무실, 캠핑, 여행 어디에서나 갓 내린 듯한 깊은 풍미를 즐겨 보세요!",
         tag="깊은 풍미는 그대로, 보관은 더욱 자유롭게", shots=2),
    dict(no="01-002", cat="한돈", kicker="제주유채꽃도새기",
         name="한돈 3종 세트", sub="1.2kg",
         catch="유채꽃도새기의 깊은 풍미를 경험해 보세요!",
         tag="지방은 덜고, 맛은 살렸습니다.", shots=3,
         hide=True),   # 임시 숨김 — 스토어에 등록된 상품 없음. 이 줄만 지우면 다시 나온다
    dict(no="01-003", cat="한돈", kicker="정통 육가공 마이스터",
         name="한돈 왕돈마호크", sub="400g × 3팩 · 캠핑용",
         catch="100년 전통 독일 육가공 마이스터의 장인 정신이 깃든 시즈닝",
         tag="직접 간할 필요 없는 완벽한 맛 밸런스!", shots=3),
    dict(no="01-004", cat="소고기", kicker="초이스등급 명품",
         name="LA꽃갈비 선물세트", sub="1.8kg",
         catch="갈비살 중 가장 맛있는 꽃갈비살 부분만을 엄선하여 손질한 프리미엄 선물세트",
         tag="눈꽃처럼 퍼져있는 육즙 마블링, 뛰어난 육즙과 육향", shots=1),
    dict(no="01-005", cat="수산", kicker="영광 더굴비",
         name="찐보리굴비 5마리", sub="원산지 : 중국",
         catch="껍질은 바삭! 굴비살은 쫄깃~ 내장살은 씁쓸한 특유의 맛이 일품인 버릴 것 하나 없는 찐 보리굴비!",
         tag="찬 녹차물 또는 따뜻한 녹차물에 밥을 말아서 참기름을 가미한 고추장에 찍어 먹으면 색다른 별미입니다.", shots=2,
         hide=True),   # 임시 숨김 — 이 줄만 지우면 다시 나온다
    dict(no="01-006", cat="수산", kicker="매운맛 중독",
         name="숙성수제양념 매콤탱쭈꾸미", sub="500g + 500g · 떡사리 포함 · 2~3인",
         catch="신선하고 수율 좋은 최상급 쭈꾸미",
         tag="일주일 이상 숙성, 깊은 맛의 수제양념소스!", shots=3,
         hide=True),   # 임시 숨김 — 이 줄만 지우면 다시 나온다
    dict(no="01-007(A)", cat="한우", kicker="궁중레시피 · 명품본가",
         name="한우 떡갈비 선물세트", sub="실속형 · 1.02kg (170g × 6개입)",
         catch="화학적인 발색제를 사용하지 않고 우리땅 한우, 우리땅 한돈과 비법소스로만 전통의 맛을 구현합니다.",
         tag="입안에 가득차는 풍부한 식감", shots=1),
    dict(no="01-007(B)", cat="한우", kicker="궁중레시피 · 명품본가",
         name="한우 떡갈비 선물세트", sub="고급형 · 1.36kg (170g × 8개입)",
         catch="화학적인 발색제를 사용하지 않고 우리땅 한우, 우리땅 한돈과 비법소스로만 전통의 맛을 구현합니다.",
         tag="입안에 가득차는 풍부한 식감", shots=1),
    dict(no="01-007(C)", cat="한우", kicker="궁중레시피 · 명품본가",
         name="한우 떡갈비 선물세트", sub="프리미엄형 · 1.7kg (170g × 10개입)",
         catch="화학적인 발색제를 사용하지 않고 우리땅 한우, 우리땅 한돈과 비법소스로만 전통의 맛을 구현합니다.",
         tag="입안에 가득차는 풍부한 식감", shots=1),
    dict(no="01-008", cat="아트", kicker="",
         name="이중섭 판화 컬렉션 20종", sub="실크스크린 아트에디션 4호",
         catch="선과 색의 강도 속에 근원적 인간 감정과 한국적 정서를 담아낸다.",
         tag="2026, 이중섭 110주년 기념 ~ (액자포함)", shots=3),
    # ── 공급사 02 · 떡 · 전통 디저트 ──────────────────────────────
    dict(no="02-001(A)", cat="떡", kicker="더블치즈떡",
         name="더블치즈", sub="240g · 30g×8개",
         catch="모짜렐라 자연치즈가 듬뿍! 국산쌀로 만든 치즈떡",
         tag="기호에 맞게 시즈닝, 소스와 곁들이면 사먹는 간식 안부러운 떡구이 완성!", shots=2),
    dict(no="02-001(B)", cat="떡", kicker="더블치즈떡",
         name="더블고구마", sub="240g · 30g×8개",
         catch="달콤한 고구마앙금 듬뿍! 국산쌀로 만든 고구마떡",
         tag="기호에 맞게 시즈닝, 소스와 곁들이면 사먹는 간식 안부러운 떡구이 완성!", shots=1),
    dict(no="02-001(C)", cat="떡", kicker="더블치즈떡",
         name="더블옥수수", sub="240g · 30g×8개",
         catch="옥수수와 자연치즈 듬뿍! 국산쌀로 만든 옥수수떡",
         tag="기호에 맞게 시즈닝, 소스와 곁들이면 사먹는 간식 안부러운 떡구이 완성!", shots=1),
    dict(no="02-001(D)", cat="떡", kicker="더블치즈떡",
         name="용암더블", sub="240g · 30g×8개",
         catch="용암처럼 빨간치즈가 흐르는~! 용암더블치즈떡",
         tag="기호에 맞게 시즈닝, 소스와 곁들이면 사먹는 간식 안부러운 떡구이 완성!", shots=2),
    dict(no="02-002(A)", cat="떡", kicker="더블크림떡",
         name="치즈크림", sub="800g · 40g×20개",
         catch="쫀득한 찹쌀떡 속에 사르르 녹는 크림치즈 한 스푼",
         tag="식물성 크림으로 더 가볍게, 더 깔끔하게, 부담없이 즐기는 쫀득한 안심 디저트", shots=1),
    dict(no="02-002(B)", cat="떡", kicker="더블크림떡",
         name="옥수수크림", sub="800g · 40g×20개",
         catch="쫀득한 찹쌀떡 속에 생크림과 톡톡 씹히는 옥수수알",
         tag="식물성 크림으로 더 가볍게, 더 깔끔하게, 부담없이 즐기는 쫀득한 안심 디저트", shots=1),
    dict(no="02-002(C)", cat="떡", kicker="더블크림떡",
         name="티라미슈크림", sub="800g · 40g×20개",
         catch="한입 베어무는 순간 터지는 마스카포에 티라미슈크림",
         tag="식물성 크림으로 더 가볍게, 더 깔끔하게, 부담없이 즐기는 쫀득한 안심 디저트", shots=1),
    dict(no="02-002(D)", cat="떡", kicker="더블크림떡",
         name="초코크림", sub="800g · 40g×20개",
         catch="쫄깃한 찰떡 속에 생크림과 초코칩 한입 먹는 순간, 디저트로 딱 떠오르는 맛",
         tag="식물성 크림으로 더 가볍게, 더 깔끔하게, 부담없이 즐기는 쫀득한 안심 디저트", shots=2),
    dict(no="02-003", cat="떡", kicker="달콤한 팥앙금이 가득",
         name="콩쑥찰떡", sub="800g · 40g×20개",
         catch="어른들 선물, 가족과 함께 할 수 있는 간식으로 찰떡 궁합",
         tag="고소한 콩가루 옷을 입은 콩쑥 찰떡은 쑥향에 달콤한 팥 앙금이 더해져 남녀노소 모두가 좋아하는 인절미",
         shots=1),
    dict(no="02-004(A)", cat="떡", kicker="말랑말랑 전통",
         name="백절편", sub="1봉 1kg내 소포장",
         catch="티없이 맑은 절편! 보기만 해도 말랑함이 느껴지는 쌀떡",
         tag="농부가 쌀 농사부터 떡 제조까지 전통 방식으로 만든 절편", shots=1),
    dict(no="02-004(B)", cat="떡", kicker="말랑말랑 전통",
         name="쑥절편", sub="1봉 1kg내 소포장",
         catch="국산 쌀과 쑥으로 만든 향긋한 쑥절편",
         tag="농부가 쌀 농사부터 떡 제조까지 전통 방식으로 만든 절편", shots=1),
    dict(no="02-005(A)", cat="떡", kicker="설기 3종",
         name="단호박 호두설기", sub="1,020g · 60g×17개",
         catch="구수한 맛에 달콤함과 고소함을 더하는 단호박 호두설기",
         tag="국산 쌀과 단호박(수입산)으로 고운 색을 낸 떡, 설탕과 호두까지 더해져 달콤하고 고소한 맛",
         shots=1),
    dict(no="02-005(B)", cat="떡", kicker="설기 3종",
         name="쑥설기", sub="1,020g · 60g×17개",
         catch="쑥의 향긋함을 담은 포근포근 한 쑥설기",
         tag="국산 쑥과 국산 멥쌀로 만든 향긋한 쑥설기로 쑥향기 가득 품은 설기",
         shots=1),
    dict(no="02-005(C)", cat="떡", kicker="설기 3종",
         name="밤설기", sub="1,020g · 60g×17개",
         catch="멥쌀과 달콤한 밤이 들어간 포근포근 한 밤설기",
         tag="국산 쌀과 밤(수입산)으로 은은한 단맛을 낸 밤설기로 적당한 단맛으로 입맛 끌어당기는 떡",
         shots=1),
]

def storebar(no=None):
    """원본 팜플릿의 3칸 표: 네이버 | 온새누리장터 | 바로가기"""
    href = PRODUCT_URLS.get(no) or STORE_URL
    return f'''<a class="storebar" href="{href}" target="_blank" rel="noopener">
              <span class="sb-l"><span class="nmark"><svg viewBox="0 0 24 24" aria-hidden="true"><rect width="24" height="24" rx="4.5" fill="#03C75A"/><path d="M14.2 12.3 9.9 6.2H6.2v11.6h3.6v-6.1l4.3 6.1h3.7V6.2h-3.6v6.1Z" fill="#fff"/></svg></span><i>네이버</i></span>
              <span class="sb-c">온새누리장터</span>
              <span class="sb-r">바로가기 <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg></span>
            </a>'''


def shots(n, no=None):
    """PHOTOS 의 사진을 앞에서부터 칸에 채우고, 남는 칸은 자리표시로 둔다."""
    ph = ('''                <figure class="shot"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.2" y="5.2" width="17.6" height="13.6" rx="2.2"/><circle cx="9" cy="10.2" r="1.6"/><path d="m4.4 17 4.4-4.2 3.3 3 3.1-2.6 4.4 3.8"/></svg><figcaption>사진 한컷</figcaption></figure>''')
    srcs = PHOTOS.get(no) or []
    cells = []
    for i in range(n):
        if i < len(srcs):
            cells.append(f'                <figure class="shot filled"><img src="{srcs[i]}" alt="" loading="lazy" draggable="false"></figure>')
        else:
            cells.append(ph)
    inner = "\n".join(cells)
    return f'''<div class="shots s{n}">
{inner}
              </div>'''


def product_page(p, folio):
    kicker_html = f'            <div class="kicker-p">{p["kicker"]}</div>\n' if p["kicker"] else ""
    return f'''        <article class="slide" data-title="{p['name']}">
          <div class="pg">
            <div class="eyebrow"><span>{p['cat']}</span><i class="ln"></i><span class="pno">{p['no']}</span></div>
{kicker_html}            <h2 class="t">{p['name']}</h2>
            <div class="pspec">{p['sub']}</div>
            <div class="body">
              <p class="catch">{p['catch']}</p>
              {shots(p['shots'], p['no'])}
              <p class="tagline">{p['tag']}</p>
              {storebar(p['no'])}
            </div>
            <div class="folio"><span>{p['cat']}</span><span class="fl"></span><span class="num">{folio:02d}</span></div>
          </div>
        </article>'''

COVER = f'''        <article class="slide cover" data-title="표제부">
          <div class="pg">
            <div>
              <div class="logoplate"><img src="{LOGO_FULL}" width="{LOGO_FULL_W}" height="{LOGO_FULL_H}" alt="온새누리(주)" draggable="false"></div>
              <div class="hair"></div>
              <div class="kicker">Onsaenuri Jangteo</div>
              <h1>온새누리장터<br>이야기</h1>
              <div class="title2">정성을 담아,<br>건강한 일상을 전합니다.</div>
            </div>
            <div>
              <p class="cover-msg">온새누리장터를 찾아주시는 고객님께 진심으로 감사드립니다.<br>좋은 상품을 정성껏 선별하고, 정직하게 전하겠습니다.</p>
              ''' + storebar() + '''
              <div class="hair"></div>
              <div class="foot"><span>공동구매 상담용 안내</span><span>2026</span></div>
            </div>
          </div>
        </article>'''

GREETING = '''        <article class="slide" data-title="인사말">
          <div class="pg">
            <div class="eyebrow"><span>인사말</span><i class="ln"></i></div>
            <h2 class="t">반갑습니다!</h2>
            <div class="body">
              <div class="creed">
                <span>정성을 더하고,</span>
                <span>믿음을 나누고,</span>
                <span>행복은 함께합니다.</span>
              </div>
              <div class="grow"></div>
              ''' + storebar() + '''
            </div>
            <div class="folio"><span>인사말</span><span class="fl"></span><span class="num">02</span></div>
          </div>
        </article>'''

CLOSING = f'''        <article class="slide backcov" data-title="맺음말">
          <div class="pg">
            <div>
              <div class="logoplate"><img src="{LOGO_FULL}" width="{LOGO_FULL_W}" height="{LOGO_FULL_H}" alt="온새누리(주)" draggable="false"></div>
              <h2 class="thanks">Thank You!</h2>
              <p class="thanks-ko">온새누리장터와 함께해 주셔서<br>감사합니다.</p>
              <p class="thanks-q">&ldquo;좋은 인연, 좋은 상품으로 이어가겠습니다.&rdquo;</p>
            </div>
            <div class="contact">
              <div class="kv">
                <div><b>유통판매원</b><span>온새누리 주식회사</span></div>
                <div><b>공동구매 상담</b><span><a href="tel:050319497403">0503-1949-7403</a></span></div>
                <div><b>E-Mail</b><span><a href="mailto:onc870223@naver.com">onc870223@naver.com</a></span></div>
              </div>
              <a class="qr" href="{STORE_URL}" target="_blank" rel="noopener">
                <svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
                  <rect x="4" y="4" width="11" height="11" rx="1.5"/><rect x="25" y="4" width="11" height="11" rx="1.5"/><rect x="4" y="25" width="11" height="11" rx="1.5"/>
                  <rect x="8" y="8" width="3" height="3" fill="currentColor" stroke="none"/><rect x="29" y="8" width="3" height="3" fill="currentColor" stroke="none"/><rect x="8" y="29" width="3" height="3" fill="currentColor" stroke="none"/>
                  <path d="M25 25h4v4h-4zM32 25h4M25 32h4v4M32 32h4"/>
                </svg>
                <span>스마트스토어<br>바로가기</span>
              </a>
            </div>
          </div>
        </article>'''

# hide=True 인 상품은 페이지에서 빠진다 (데이터는 위에 그대로 남음)
def visible_of(code):
    return [p for p in PRODUCTS if p["no"].startswith(code + "-") and not p.get("hide")]

HIDDEN = [p for p in PRODUCTS if p.get("hide")]

CHEV = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>')


def toc_slide():
    """진입부 — 책자 선택. 책자마다 한 벌씩 들어간다(표지에서 오른쪽으로 밀면 여기로)."""
    rows = []
    for b in BOOKLETS:
        n = len(visible_of(b["code"]))
        rows.append(
            f'            <a class="toc-item" href="#{b["code"]}">\n'
            f'              <span class="tn">{b["code"]}</span>\n'
            f'              <span class="tt"><b>{b["title"]}</b><i>상품 {n}종</i></span>\n'
            f'              {CHEV}\n'
            f'            </a>')
    inner = "\n".join(rows)
    return (
        '        <article class="slide toc" data-title="목차">\n'
        '          <div class="pg">\n'
        '            <div class="eyebrow"><span>CONTENTS</span><i class="ln"></i></div>\n'
        f'            <h2 class="t">{TOC_TITLE}</h2>\n'
        f'            <p class="lede">{TOC_LEDE}</p>\n'
        '            <div class="body">\n'
        '              <div class="toc-list">\n'
        f'{inner}\n'
        '              </div>\n'
        '            </div>\n'
        '            <div class="folio"><span>온새누리장터</span><span class="fl"></span>'
        '<span>공동구매 상담용 안내</span></div>\n'
        '          </div>\n'
        '        </article>')


tracks, counts = [], []
for b in BOOKLETS:
    slides = []
    if len(BOOKLETS) > 1:          # 책자가 하나면 진입부를 만들지 않는다
        slides.append(toc_slide())
    slides += [COVER, GREETING]
    vis = visible_of(b["code"])
    for n, p in enumerate(vis):
        slides.append(product_page(p, n + 3))
    slides.append(CLOSING)
    pages = len(slides) - (1 if len(BOOKLETS) > 1 else 0)
    counts.append((b, len(vis), pages))
    tracks.append(
        f'    <div class="track" data-booklet="{b["code"]}" data-title="{b["title"]}">\n'
        + "\n".join(slides) + '\n    </div>')

BODY = "\n".join(tracks)

# 1) page.html — 본문만 (Artifact 배포용). TRACKS 사이만 교체하고 나머지는 유지.
HEAD_MARK = '    <!-- TRACKS -->'
TAIL_MARK = '    <!-- /TRACKS -->'
doc = open('page.html', encoding='utf-8').read()
head = doc.split(HEAD_MARK)[0] + HEAD_MARK + "\n"
tail = TAIL_MARK + doc.split(TAIL_MARK)[1]
page = head + BODY + "\n" + tail
open('page.html', 'w', encoding='utf-8').write(page)

# 2) index.html — 완전한 HTML 문서 (GitHub Pages 배포용)
total = sum(c[1] for c in counts)
desc = f"온새누리장터 공동구매 상담용 안내 — 책자 {len(BOOKLETS)}권 · 상품 {total}종"
page = page.replace('<meta charset="utf-8">\n', '')
h, _, rest = page.partition('</style>')
doc_head = h.strip() + "\n</style>"
doc_body = rest.strip()
HTML = (
'<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
f'<meta name="description" content="{desc}">\n'
'<meta name="theme-color" content="#0E5C4F" media="(prefers-color-scheme: light)">\n'
'<meta name="theme-color" content="#0D100F" media="(prefers-color-scheme: dark)">\n'
'<meta property="og:title" content="온새누리장터 공동구매 안내">\n'
f'<meta property="og:description" content="{desc}">\n'
'<meta property="og:type" content="website">\n'
'<link rel="icon" href="favicon.ico" sizes="any">\n'
'<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">\n'
'<link rel="icon" type="image/png" sizes="512x512" href="icon-512.png">\n'
'<link rel="apple-touch-icon" href="apple-touch-icon.png">\n'
f'{doc_head}\n</head>\n<body>\n{doc_body}\n</body>\n</html>\n')
open('index.html', 'w', encoding='utf-8').write(HTML)

for b, nvis, pages in counts:
    print(f'  {b["code"]} {b["title"]:22s} 상품 {nvis:2d}종 · {pages}장')
if HIDDEN:
    print("  숨김:", ", ".join(f'{p["no"]} {p["name"]}' for p in HIDDEN))
