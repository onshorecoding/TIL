## call by reference / call by value (CBV /CBR )


Python은 함수를 실행할때 Call by reference같은 느낌으로 reference를 넘겨준다. 
하지만 이때 넘겨주는 것은 변수가 담고 있는 자료(Data)의 reference입니다.

자료가 mutable하다면 변경해도 reference가 보존되므로 결과적으로 Call by reference처럼 적용되는 것으로 보인다. 
자료가 immutable하다면 결과적으로 Call by value처럼 적용되는 것으로 보인다

- 숫자형 (Number) : immutable
- 문자열 (String) : immutable
- 리스트 (List) : mutable
- 튜플 (Tuple) : immutable
- 딕셔너리 (Dictionary) : mutable


## python zip 내장함수



## 트리 순회

        1
      /   \ 
    2      3
  /  \    /  \
4     5  6    7

- 전위 순회: 1-2-4-5-3-6-7
- 중위 순회: 4-2-5-1-6-3-7
- 후위 순회: 4-5-2-6-7-3-1