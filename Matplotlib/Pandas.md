# Pandas
구조화된 데이터를 효과적으로 처리하고 저장할 수 있는 파이썬 라이브러리
.Array 계산에 특화된 numpy기반으로 만들어져 다양한 기능을 제공한다

```
import pandas as pd

#series: numpy array가 보강된 형태(data와 index를 가지고 있다)

data = pd.series([1,2,3,4], index['a','b','c','d'])
# 인덱스로 접근이 가능하다
data['c']
# 2

# 딕셔너리로도 만들 수 있다
```

# DataFrame 새 데이터 추가 및 수정
- 리스트로 추가하는 방법 / 딕셔너리로 추가하는 방법
- 새로운 칼럼 추가


# Indexing / Slicing

- loc : 명시적인 인덱스를 참조하는 인덱싱. 슬라이싱
- iloc: 파이썬 스타일 정수 인덱스 인덱싱, 슬라이싱

```
dataframe.loc[행의번호, 칼람명] = '바꿀 값'
```


# 누락된 데이터 처리
```
dataframe.dropna()
dataframe['칼럼'] = dataframe['칼럼'].fillna('word')
#빈 값을 word로 치환한다

A = pd.Series([2,4,6], index=[0,1,2])
B = pd.Series([1,3,5], index=[1,2,3])
A + B
A.add(B, fill_value=0)
->빈 값을 0으로 하여 계산
```


# 데이터 값으로 정렬하기

```
df.sort_values('칼럼명') 
#칼럼명으로 정렬

sorted_df = df.sort_values('col2', ascending = False)
sorted_df = df.sort_values('col2', ascending = True)

data = data.sort_values(['col2', 'col1'], ascending=[True, False])

```

# 조건으로 검색하기
```
df.query("검색 조건")

df[칼럼명].str.contains("검색조건")
df.칼럼명.str.match("검색조건")
```

# groupby 연산

```
# key를 기준으로 묶어 합계를 구해 출력
print(df.groupby('key').sum())

# key와 data1을 기준으로 묶어 합계를 구해 출력
print(df.groupby(['key','data1']).sum())

# 데이터 프레임을 'key' 칼럼으로 묶고, data1과 data2 각각의 최솟값, 중앙값, 최댓값을 출력
print(df.groupby('key').aggregate([min, np.median, max]))

# 데이터 프레임을 'key' 칼럼으로 묶고, data1의 최솟값, data2의 합계를 출력
print(df.groupby('key').aggregate({'data1': 'min', 'data2': np.sum}))

```

# filter() /apply() 활용

```
# 데이터 프레임을 'key' 칼럼으로 묶고, data1과 data2 각각의 최솟값, 중앙값, 최댓값을 출력
print(df.groupby('key').aggregate([min, np.median, max]))

# 데이터 프레임을 'key' 칼럼으로 묶고, data1의 최솟값, data2의 합계를 출력
print(df.groupby('key').aggregate({'data1': 'min', 'data2': np.sum}))
``` 

# pivot_table 활용

```
df = pd.read_csv("읽을 csv 파일 이름)

df0 = df[df["칼럼"] == "칼럼값"]

df1 =df0.groupby("칼럼").mean()

df2 = df0.pivot_table(index="칼럼", columns="칼럼", values="값", aggfunc=np.mean)

```