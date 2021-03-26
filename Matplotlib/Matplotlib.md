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

font = fm.FontProperties(fname='./NanumBarunGothic.ttf')

# 막대의 높이가 빈도의 값이 되도록 설정합니다.
plt.bar(pos, temperatures, align='center')

# 각 막대에 해당되는 단어를 입력합니다.
plt.xticks(pos, dates, rotation='vertical', fontproperties=font)

# 그래프의 제목을 설정합니다.
plt.title('제목', fontproperties=font)

# Y축에 설명을 추가합니다.
plt.ylabel('Y축', fontproperties=font)

# 단어가 잘리지 않도록 여백을 조정합니다.
plt.tight_layout()

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
- set(list) : 집합연산자
- union : set1 | set2 #합집합
- intersection :  set1 & set2 #교집합
- diff : set1 - set2 #차집합
- xor : set1 ^ set2 #XOR


# CSV(Comma Separated Value)

- 같은 데이터를 저당하는데 용량을 적게 소모함
- 데이터 오염에 취약함

ex) name, age, address, gender
콤마가 아닌 다른 문자로도 구분하는 경우도 포함

```
import csv

wiht open('file.csv') as file:
    reader = csv.reader(file, delimiter=',') #구분자를 명시해야한다
    for row in reader:
        print(row[0])
```