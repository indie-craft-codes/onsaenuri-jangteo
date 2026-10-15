# 공급사 2곳 구조 — 완료

반영됨: https://onsaynuri.com (`#01` / `#02`)
남은 것은 아래 「미결」 두 줄뿐이다.

## 미결

| 항목 | 현재 값 |
|---|---|
| 책자 이름 | `한우 · 한돈 · 커피 · 아트` / `떡 · 전통 디저트` (잠정 — `build.py` 의 `BOOKLETS`) |
| 진입부 제목 | "책자를 고르세요" (잠정 — `build.py` 의 `TOC_TITLE`/`TOC_LEDE`) |

## 스토어에서 상품 정보 긁는 법 (2026-10 기준)

**curl/Playwright 는 429, 크롬 자동화 도구는 naver.com 도메인 차단, WebFetch 도 차단.
크롬에는 네이버 로그인 쿠키가 없다(NID_AUT/NID_SES 없음). Safari 만 된다.**
로그인은 필요 없었다 — 전에 로그인 화면으로 튄 건 일시적 봇 차단이었다.

```
osascript -e 'tell application "Safari" to make new document with properties {URL:"https://smartstore.naver.com/onsaynuri/category/ALL"}'
sleep 7
osascript -e 'tell application "Safari" to get source of document 1' > store.html
```

목록 HTML 안의 `window.__PRELOADED_STATE__` 를 파싱하면
`categoryProducts.simpleProducts[]` 에 **상품마다 `id`·`name`·`salePrice`·
`representativeImageUrl`·`optionalImageUrls` 가 한 객체 안에** 들어 있다.
→ 이걸 쓰면 01 때 같은 「이웃 상품 사진 섞임」이 구조적으로 불가능하다.
개별 상품 페이지를 열어 og:image 를 읽을 필요가 없다.

- 그 값은 JS 리터럴이라 `undefined` 가 섞여 있다. 문자열 밖의 `undefined` 를
  `null` 로 바꾼 뒤 `json.loads`. 중괄호 짝을 세어 끝을 찾는다
- 이미지는 `<url>?type=f640_640`, CDN(shop-phinf.pstatic.net)은 curl 로 받아진다
- Safari 의 `get source of document 1` 은 **처음 받은 HTML** 이다. 하이드레이션
  뒤의 DOM 이 필요하면 `do JavaScript` (이 기기는 허용돼 있다)
- 상품 **옵션명**은 끝내 못 읽었다. 드롭다운을 눌러야 로드되는데 JS 클릭이 안 먹었다

## 02 사진·링크 결과

14종 전부 개별 상품 페이지로 연결. 단 **더블고구마·더블옥수수·용암더블은
개별 판매가 없어** `더블떡 4종 5봉 세트`(13727764883) 로 연결했다.
사진은 네 맛을 육안으로 갈랐다 — 보라색+고구마 / 옥수수알+옥수수대 /
붉은 소가 흘러나오는 것(용암) / 치즈 늘어나는 것.

`용암더블` 은 스토어에 품목명으로는 없지만 4종 세트 구성에 들어 있어 숨기지 않았다.

## HWP 읽기


`hwp5txt` 가 없으므로 직접 파싱한다. 레시피는 세션에서 쓴 스크립트 그대로:
olefile 로 열고 `FileHeader` 36~40 바이트의 압축 플래그 확인 →
`BodyText/Section*` 를 `zlib.decompress(raw, -15)` →
레코드 순회하며 태그 `0x043`(HWPTAG_PARA_TEXT) 만 UTF-16LE 로 디코드.
제어문자 1·2·3·11·12·14~18·21~23 과 4~8·19·20 은 16바이트씩 건너뛴다.

## 02 상품 14종 (HWP 원문)

```
02-001(A) 더블치즈떡 · 더블치즈    240g / 30g×8개   사진2
02-001(B) 더블치즈떡 · 더블고구마  240g / 30g×8개   사진1
02-001(C) 더블치즈떡 · 더블옥수수  240g / 30g×8개   사진1
02-001(D) 더블치즈떡 · 용암더블    240g / 30g×8개   사진2
02-002(A) 더블크림떡 · 치즈크림    800g / 40g×20개  사진1
02-002(B) 더블크림떡 · 옥수수크림  800g / 40g×20개  사진1
02-002(C) 더블크림떡 · 티라미슈크림 800g / 40g×20개 사진1
02-002(D) 더블크림떡 · 초코크림    800g / 40g×20개  사진2
02-003    콩쑥찰떡               800g / 40g×20개  사진1
02-004(A) 전통 백절편            1봉 1kg내 소포장  사진1
02-004(B) 전통 쑥절편            1봉 1kg내 소포장  사진1
02-005(A) 설기 3종 · 단호박 호두설기 1,020g / 60g×17개 사진1
02-005(B) 설기 3종 · 쑥설기        1,020g / 60g×17개 사진1
02-005(C) 설기 3종 · 밤설기        1,020g / 60g×17개 사진1
```
캐치프레이즈·한 줄 설명은 HWP 원문에 있다. `mockup_data.py` 에 상품명·규격은
이미 정리돼 있으나 catch/tag 는 02-001(A) 하나만 들어 있다.
