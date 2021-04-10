# React 자습서 

## JavaScript 재 입분하기
타입
- 수(Number)
- 문자열(String)
- 부울(Boolean)
- 기호(Symbol)
- 객체(Object): 함수(Function), 배열(Array), 날짜(Date), 정규식(RegExp)
- 널(Null)
- 정의되지 않음 (Undefined)

- while 문
```
while (true) {
  // 무한루프!
}

#적어도 한번이상 실행되게 하기 위해서 사용할 수 있는 방법
var input;
do {
  input = get_input();
} while (inputIsNotValid(input));
```

-switch 문
```
switch(action) {
    case 'draw':
        drawIt();
        break;
    case 'eat':
        eatIt();
        break;
    default:
        doNothing();
}

#break을 추가하지 않았다면, 다음단계를 실행한다.
```

# DOM에 엘리먼트 렌더링하기