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

## 남은 자리표시

- 네이버 스마트스토어 주소 → `build.py` 의 `STORE_URL`
- 상품 사진 24칸 (`사진 한컷`), 로고, QR코드
