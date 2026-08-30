# 온새누리장터 공동구매 안내

**https://onsaynuri.com**

온새누리장터 공동구매 상담용 홍보물 웹 버전 (13페이지, 슬라이드 전환).

- `index.html` — GitHub Pages 배포본 (완전한 HTML 문서, 자동 생성)
- `page.html` — 본문만 담긴 원본. 레이아웃·스타일·스크립트를 여기서 고친다.
- `build.py` — `PRODUCTS` 수정 후 `python3 build.py` 실행하면 `page.html` 의 페이지 부분과 `index.html` 전체를 갱신한다.
- `index-3d.html` — 3D 책 넘김 방식 시안 (미사용)

## 도메인

Cloudflare 에서 산 `onsaynuri.com` 을 GitHub Pages 에 연결했다.

- Cloudflare DNS: `@`, `www` 둘 다 CNAME -> `indie-craft-codes.github.io`, **프록시 끔(DNS 전용)**
- 저장소 루트의 `CNAME` 파일이 커스텀 도메인을 지정한다. 지우면 연결이 끊긴다.
- 인증서는 GitHub 이 Let's Encrypt 로 자동 발급/갱신. 프록시를 켜면 갱신이 막히므로
  켜야 한다면 Cloudflare SSL/TLS 를 `Full (strict)` 로 둘 것.

## 임시 숨김

`build.py` 의 상품 항목에 `hide=True` 를 붙이면 페이지에서 빠진다 (데이터는 남는다).
그 줄을 지우고 `python3 build.py` 하면 원래 자리로 돌아온다.

현재 숨김: `01-002 한돈3종세트`, `01-005 찐보리굴비`, `01-006 매콤탱쭈꾸미`
(셋 다 스토어에 등록된 상품이 없어서 뺐다)

## 링크

- `STORE_URL` — 스토어 홈. 모든 `바로가기` 버튼과 맺음말 QR 박스의 기본 링크.
- `PRODUCT_URLS` — 상품번호별 개별 링크. 채워 넣으면 그 상품 페이지의 버튼만 해당 주소로 바뀐다.

## 로고

`assets/logo-original.jpg` (160x160) 가 원본. `logo_data.py` 에 data URI 로 심어져 있고
`build.py` 가 표제부·맺음말에, `page.html` 상단바가 심볼만 쓴다.
더 높은 해상도나 벡터(AI/SVG) 파일이 생기면 `logo_data.py` 를 다시 만들면 된다.

## 상품 대표 이미지

`photo_data.py` 에 상품번호별 **목록**. 앞에서부터 사진 칸을 채우고 남는 칸은 자리표시로 남는다.
원본은 `assets/products/`. 칸 수는 `build.py` 의 `shots=N`.

- `01-001` 첫 장은 애니메이션 WebP. 원본 GIF 9.4MB(720px/120프레임)를
  440px·60프레임·q45 로 줄여 462KB. 원본은 `01-001-1-원본.gif`.
- 나머지는 정지 WebP (긴 변 520px, q78).

**주의**: 스토어 목록 HTML 에서 링크 주변 이미지를 긁으면 이웃 상품 것이 섞인다.
반드시 상품 페이지를 개별로 열어 `og:image` 를 읽을 것.

```
osascript -e 'tell application "Safari" to set URL of document 1 to "…/products/<id>"'
osascript -e 'tell application "Safari" to get source of document 1' | grep og:image
```
이미지는 `<url>?type=f640_640` 으로 받으면 640px. CDN(shop-phinf.pstatic.net)은 curl 로도 받아진다.

## 남은 자리표시

- 상품별 두 번째·세 번째 사진, QR코드 이미지

## 스토어 상품 목록 확인 방법

이 환경에서 curl / Playwright 로 스마트스토어에 접근하면 429 로 막힌다.
사용자 Safari 를 AppleScript 로 띄워 읽으면 정상 동작한다.

```
osascript -e 'tell application "Safari" to set URL of document 1 to "https://m.smartstore.naver.com/onsaynuri/category/ALL"'
osascript -e 'tell application "Safari" to get source of document 1' > out.html
```

스토어 내 검색: `https://m.smartstore.naver.com/onsaynuri/search?q=<검색어>`
