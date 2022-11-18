# Django CRUD

## 1. 가상환경 및 Django 설치

   ### 1. 가상환경 생성 및 실행
    * 가상환경 폴더를 `.gitignore`로 설정 해둔다.

    ```bash
      $ python -m venv venv
      $ source venv/Scripts/activate
      (venv) $
    ```

 
  ### 2. Django 설치 및 기록(requirements.txt)
    ```
    $ pip install django==3.2.13
    $ pip freeze > requirements.txt
    ```

## 2. Django 프로젝트 설치
  ```
  $ django-admin startproject 프로젝트명 .
  서버실행 $ python manage.py runserver
  ```

## 3. app
  ### 1.app 생성
```
$ python manage.py startapp 앱이름

```
  ### 2. app 등록
  settings.py 파일에 앱 등록

  ### 3. urls.py 설정

## 4. Index
 > url을 등록하고, view 함수 생성, template 만든다.

## 5. CRUD
  ### 1. Model 정의 (DB설계)
    > 클래스 정의
    > 마이그레이션 파일 생성 $ python manage.py makemigrations
    > DB반영(migrate) $ python manage.py migrate

  ### 2. CRUD 기능 구현
   생성 create- 게시글 생성
   > 사용자에게 html form 제공, 입력한 데이터를 처리 (ModelFrom 로직으로 변경)
  #### 1. HTML Form 제공
  > http://localhost:8000/articles/new/ > new함수

  #### 2. 입력받은 데이터 처리
  > http://localhost:8000/articles/create/
  > 게시글 DB에 생성하고 index 페이지로 redirect
  
  게시글 목록 
  > DB에서 게시글 가져와서, template에 전달

  상세보기
  > 특정한 글을 본다.
  > http://localhost:8000/articles/<int:pk>/
  
  