```
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_title("그래프명")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.set_dpi(300)
fig.savefig("파일명.png")

```


# 그래프 디자인

```
fig, ax = plt.subplots()
x = np.arrange(15)
y = x**2
ax.plot(
    x,y
    linestyle=":",  #라인스타일 ( - , -- , -. , : )
    marker="*",     #마커 ( . , o , v , s , * )
    color="#00000'  #컬러
)

```


- Line
- Scatter
- Bar plot


# JSON(JavaScript Object Notation)

- loads() : JSON 형태의 문자열을 딕셔너리로 변환한다. 딕셔너리의 모든 원소는 문자열로 설정된다. 
- dumps() : 딕셔너리를 JSON 형태의 문자열로 변환한다.

```
with open(파일명) as file:
    json_string = file.read()
    
    json_string json.loads(json_string)

with open(filename, 'w') as file:
    json_string = json.dumps(dictionary)

    file.write(json_string)

```

# 집합
- union : set1 | set2 #합집합
- intersection :  set1 & set2 #교집합
- diff : set1 - set2 #차집합
- xor : set1 ^ set2 #XOR
