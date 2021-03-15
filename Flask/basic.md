Flask의 경우 소규모 어플리케이션을 빠르게 빌드할 수 있는 동시에, 어플리케이션의 기능 확장의 역할을 하기 쉽다는 장점이 있다고 한다. 반면 Django의 경우 대규모 어플리케이션을 빠르게 빌드 할 수 있으며, 기본적으로 제공하는 기능(ORM 기능이 내장)이 많다고 한다. ORM(Object Relational Mapping)이란 데이터 베이스와 객치 지향 프로그래밍 언어간의 호환되지 않는 데이터를 변환하는 기법이라고 한다.


```
from flask import Flask

app = Flask(__name__)

# 웹페이지와 해당 페이지에서 작동할 함수를 매칭한다(라우팅)
# @(데코레이터)를 통해 선언
@app.route('/')

def hello_world():
    return "Hello World"

# 모듈명이 main일 경우에만 실행하도록 조건문을 추가
if __name__ == '__main__':
    app.run()

```
# 데이터 반환

Flask는 데이터를 json 파일 형식으로 데이터를 교환한다.
```
from flask import Flask

return jsonify(반환값)
```

# Flask Methods

- GET: 암호화 되지 않은 형태의 데이터를 서버로 전송
- HEAD: GET과 유사하며, response body를 포함하지 않고 사용
- POST: 데이터를 암호화하여 서버로 전송
- PUT: 데이터를 갱신
- DELETE: 지정된 대상을 삭제

# Flask의 URL

Flask의 URL 규칙은 Werkzeug의 라우팅 모듈에 기반한다. 
Werkzeug는 요청,응답 객체 및 다른 utility 함수를 구현하는 WSGI 툴킷이라고 한다.
WSGI(web server gateway interface)란 web 서버가 받은 호출을 python 어플리케이션에서
전달하고 응답받기 위한 호출조약(calling convention)이다


# route()를 사용한 url path 값 활용

- 문자열 활용
```
@app.route('/<variable>')
def hello(variable):
    return variable
```

- 정수 활용
```
@app.route('/<int: id>')
def hello(id):
    return id
```

- 서브경로 활용
```
@app.route('/path/<path: subpath>')
def hello(subpath):
    return subpath
```

- url_for()메소드를 통해 다른페이지로 이동 할 수 있는 링크를 생성할 수 있다.
```
@app.route('/<int: id>')
def hello(id):
    return redirect(url_for('user'))
```