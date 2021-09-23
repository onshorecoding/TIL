

# django

장고를 활용해서 게시판 CRUD기능을 구현하는 실습을 진행하여 학습할 예정입니다.

 

MVT <-> MVC

Model 단일한 데이터에 대한 정보를 가짐

저장된 데이터 베이스의 구조

장고는 모델을 통해 데이터에 접속하고 관리

일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑됨



Model: 웹 어플리케이션의 데어트를 구조화하고 조작하기 위한 도구

스키마: 데이터베이스의 구조와 제약조건(자료의 조건, 표현방법, 관계)에 관련한 전반적인 명세를 기술한 것

테이블 : 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합(SQL 에서는 테이블을 관계라고도 한다)

- 열(column): 필드 또는 속성(INT, TEXT, NULL) -> 각 열에는 고유한 데이터 형식이 지정된다.
- 행(row): 레코드 또는 튜플 -> 데이터는 행에 저장된다.

- PK: 각 행의 고유값으로 Primary Key라고 불린다. 반드시 설정해야하며, 데이터 관리 및 관계설정시 주요하게 활용 된다.



ORM: Object Relational Mapping 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에 데이터를 변환하는 변환하는 프로그래밍 기술

OOP 프로그래밍에서 RDBMS를 연동할 때, 데이터 베이스와 객체 지향 프로그래밍 언어간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법, 장고는 내장 Django ORM을 사용합니다.





## Get Started

### 프로젝트 생성

현재 디렉토리에서 practice라는 프로젝트를 생성합니다.

```
$ django-admin startproject practice
```

```
practice/
    manage.py
    practice/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```



### 게시판 앱 생성

1. 게시판 앱을 생성합니다.

```
$ python manage.py startapp articles
```

```
practice/
    manage.py
    practice/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    articles/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
```



2. 게시판 앱을 practice/settings.py 에 등록해줍니다.

```pyhton
INSTALLED_APPS = [
    # app
    "articles", #생성된 앱을 추가해줍니다.

    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```



### 앱 분리

1. /practice/url.py

```
from django.contrib import admin
from django.urls import path, include


# 확장성 및 가독성을 위해 url 분리
# 각 App에 대해 include 사용

urlpatterns = [
    path("admin/", admin.site.urls),
    parth("articles/", include("articles.urls")),
]
```

프로젝트가 확장성을 위해서 프로젝트의 url을 분리하는 작업을 진행합니다.



2. /articles/urls.py

```
from django.contrib import admin
from django.urls import path
from . import views

# articles/urls.py app 내의 url.py
app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
]
```

```
<a href="{% url 'articles:index' %}"> main </a>
```

앱 내 urls.py을 생성하여 앱 별로 url을 관리합니다.
효율적인 url 관리를 위해서 url 마다 name을 지정해줍니다.
또한 다른 앱과 url이름이 겹치는 문제를 방지하기 위해 namespace를 추가합니다.



### Templates

충돌을 막기 위해 templates/articles 디렉토리 내 index.html 생성

```html
practice/
    manage.py
    practice/
    articles/
        __init__.py
        admin.py
        apps.py
        migrations/
        templates/
    			articles/
						index.html
        models.py
        tests.py
        views.py
```



## Model

개시판의 테이블을 만들기 위한 모델을 생성해줍니다.
간단하게 제목, 내용, 생성시간, 수정시간에 대한 필드를 생성합니다.

```
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
		
```



## Model Queryset



쉘스크립트를

```

```

1. Create

```python
# 방법 1
article = Article() 
article.title = "글1"
article.content = "내용1"
article.save()

# 방법 2
article = Article(title=“글1”, content=“내용1”) 
article.save()

# 방법 3
Article.objects.create(title=“글1", content="내용1")
```

2. Read

```
In [1]: Article.objects.get(pk=1)
Out[1]: <Article: Article object (1)>
```

3. Update

```
In [1]: article = Article.objects.get(pk=1)
In [2]: article.title = "글2"
In [3]: article.save()
```

4. Delete

```
In [1]: article = Article.objects.get(pk=1)
In [2]: article.delete()
Out[2]: (1, {'articles.Article': 1})
```





## admin

```
$ python manage.py createsuperuser

사용자 이름 (leave blank to use '사용자 이름'): admin
이메일 주소:               
Password: 
Password (again): 
Superuser created successfully.
```





**multipart/form-data**

`image/*. .pdf`





## Boostrap 



### CDN



### Complied Boostrap

#### boostrap file 다운로드



static/aritcles 폴더 생성(경로 생성)

static/article/js

stataic/article/css


앱이 많아지는 것(CSS를 커스텀해서 해비하게 사용할 경우) 보통 앱 별로 관리하게 된다.



settings.py

```python
STATICFILES_DIRS = [BASE_DIR / "static"]
```

base.html

```html
<link href="{ static 'articles/css/boostrap.min.css'}"
```

