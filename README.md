# Django 기반 SNS 프로젝트

이 프로젝트는 Django를 기반으로 한 SNS(소셜 네트워크 서비스)입니다.  
아래와 같은 핵심 기능을 포함하고 있습니다:

- 회원가입 및 로그인
- 게시글 작성
- 댓글 기능
- 좋아요 기능
- 팔로우 기능
- 뉴스 피드

클린 아키텍처를 지향하며, 확장성과 유지보수가 쉬운 RESTful API 구현을 목표로 개발하고 있습니다.

---

## 📌 FastAPI → Django 전환

해당 프로젝트는 원래 [FastAPI](https://github.com/kikiru328/TIL/tree/main/FastAPI) 기반으로 시작하여,  
게시글 작성 및 피드 기능 등 일부 핵심 기능을 구현한 바 있습니다.

하지만 Django의 기능을 더 깊이 있게 학습하고, F-Lab의 커리큘럼에 맞춰보기 위해  
백엔드 프레임워크를 FastAPI에서 Django로 전환하게 되었습니다.

FastAPI 버전은 참고용으로 남겨두었으며, 아키텍처나 기능 비교 시 활용하고자 합니다.

---

## 🛠 기술 스택

- **백엔드 프레임워크**: Django, Django REST Framework  
- **인증 방식**: JWT  
- **데이터베이스**: MySQL   
- **버전 관리**: Git, GitHub

---

## 🎯 프로젝트 목표

- 실제 SNS 서비스 수준의 백엔드 기능 구현
- RESTful API 설계 및 테스트 경험 축적
- 클린 아키텍처 및 서비스 레이어 분리 적용
- Git을 활용한 협업 및 코드 리뷰 실습

---

## 🔗 참고

- FastAPI 초기 버전: [FastAPI SNS Project Repo](https://github.com/kikiru328/TIL/tree/main/FastAPI)
- Django REST Framework 공식 문서: [Django Rest Framework](https://www.django-rest-framework.org/)
- Django 추가 학습 강의: [NomadCoder: Django](https://nomadcoders.co/airbnb-clone/lobby)

---

## 🙋‍♂️ 작성자

- GitHub: [kikiru328](https://github.com/kikiru328)  
- 본 프로젝트는 F-Lab 멘토링 프로그램을 통해 개발 중입니다.
