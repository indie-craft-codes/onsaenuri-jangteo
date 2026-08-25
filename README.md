# 온새누리장터 공동구매 안내

온새누리장터 공동구매 상담용 홍보물 웹 버전 (13페이지, 슬라이드 전환).

- `index.html` — GitHub Pages 배포본 (완전한 HTML 문서, 자동 생성)
- `page.html` — 본문만 담긴 원본. 레이아웃·스타일·스크립트를 여기서 고친다.
- `build.py` — `PRODUCTS` 수정 후 `python3 build.py` 실행하면 `page.html` 의 페이지 부분과 `index.html` 전체를 갱신한다.
- `index-3d.html` — 3D 책 넘김 방식 시안 (미사용)

## 임시 숨김

`build.py` 의 상품 항목에 `hide=True` 를 붙이면 페이지에서 빠진다 (데이터는 남는다).
그 줄을 지우고 `python3 build.py` 하면 원래 자리로 돌아온다.

현재 숨김: `01-005 찐보리굴비`, `01-006 매콤탱쭈꾸미`

## 링크

- `STORE_URL` — 스토어 홈. 모든 `바로가기` 버튼과 맺음말 QR 박스의 기본 링크.
- `PRODUCT_URLS` — 상품번호별 개별 링크. 채워 넣으면 그 상품 페이지의 버튼만 해당 주소로 바뀐다.

## 남은 자리표시

- 상품 사진, 로고, QR코드 이미지
- `01-002 제주유채꽃도새기 한돈3종세트` — 스토어에 등록된 상품이 없어 스토어 홈으로 연결됨

## 스토어 상품 목록 확인 방법

이 환경에서 curl / Playwright 로 스마트스토어에 접근하면 429 로 막힌다.
사용자 Safari 를 AppleScript 로 띄워 읽으면 정상 동작한다.

```
osascript -e 'tell application "Safari" to set URL of document 1 to "https://m.smartstore.naver.com/onsaynuri/category/ALL"'
osascript -e 'tell application "Safari" to get source of document 1' > out.html
```

스토어 내 검색: `https://m.smartstore.naver.com/onsaynuri/search?q=<검색어>`
