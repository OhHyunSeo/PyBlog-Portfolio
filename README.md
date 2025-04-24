<h1 align="center">📝 PyBlog Portfolio</h1>
<p align="center">
  <b>🔥 Django 기반 블로그 + 게시판 통합 포트폴리오</b><br>
  사용자 인증, 댓글, 태그, 마크다운까지 갖춘 풀스택 웹 프로젝트입니다.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-4.2-success?logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-DB-%2307405e?logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black">
</p>

---

## 🚀 소개

**PyBlog Portfolio**는 블로그 + 게시판 + 댓글 시스템이 통합된 Django 웹 포트폴리오입니다.  
Markdown 기반 게시글, 태그 시스템, 사용자 프로필, 관리자 페이지 등 다양한 기능이 포함되어 있으며  
실제 배포나 포트폴리오 제출에도 적합한 구조를 갖추고 있습니다.

---

## 🔧 주요 기능

- 🖊️ 블로그 글 작성, 수정, 삭제 (마크다운 지원)
- 🗂️ 게시판 및 댓글 기능
- 📌 태그 기반 검색 및 필터링
- 👤 사용자 인증 (회원가입/로그인/프로필)
- 📁 이미지 업로드 (미디어 관리)
- 📊 Django Admin을 통한 콘텐츠 관리

---

## 📁 프로젝트 구조 (요약)

```
📁 PyBlog-Portfolio-master/
├── accounts/    # 사용자 인증, 프로필
├── blog/        # 블로그 기능 (글, 태그, 마크다운)
├── board/       # 게시판 기능
├── comments/    # 댓글 기능
├── config/      # Django 설정
├── media/       # 업로드 이미지
├── db.sqlite3   # SQLite DB
└── manage.py
```

---

## ⚙️ 실행 방법

### 1. 클론 및 가상환경 설정

```bash
git clone https://github.com/yourusername/pyblog-portfolio.git
cd pyblog-portfolio
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. 마이그레이션 및 서버 실행

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

접속: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---



## 🖼️ 예시 화면

> 게시글, 태그 필터링, 마크다운 렌더링, 댓글 기능 등을 포함한 다양한 UI를 제공합니다.  
> `/media/` 폴더에 이미지가 포함되어 있습니다. README에 직접 이미지 링크 삽입 가능!

---



<p align="center"><i>Made with ❤️ by Django & Markdown</i></p>
