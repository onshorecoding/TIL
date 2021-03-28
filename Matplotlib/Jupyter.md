```
# numpy
import numpy as np

# pandas
import pandas as pd

# seaborn
import seaborn as sns

# matplotlib의 pyplot
import matplotlib.pyplot as plt
# matplotlib 시각화 결과를 jupyter notebook에서 바로 확인하기 위한 코드 작성 
%matplotlib inline
```




# machine learning
```
import pandas as pd

def load_titanic_dataset():
    df = pd.read_csv('./data/titanic.csv')
    df = df.drop('PassengerId', axis=1)
    return df
	
def check_missing_values(df): #결측치 확인
    titanic_null = df.isnull().sum()
    sleep(2)
    for col, val in titanic_null.items():
        print("{} : {:.2f}%".format(col, val/df.shape[0]*100))

def variable_selection(df): #변수선택
    columns = ['Name', 'Ticket', 'Cabin']
    df.drop(columns, axis=1, inplace=True)

def handling_missing_values(df): #결측 데이터 처리
    age_median = df['Age'].median()
    df['Age'].fillna(age_median, inplace=True)

def vectorization_sex(df):
    try:
        sex_mapping = {'male': 0, 'female': 1}
        df['Sex'].replace(sex_mapping, inplace=True)
    except TypeError:
        return df

def vectorization_embarked(df): #데이터 변환
    try:
        embarked_mapping = {'S': 0, 'C': 1, 'Q': 2}
        df['Embarked'].replace(embarked_mapping, inplace=True)
        return df.copy()
    except TypeError:
        return df
		
def show_result(df):
    print(df.sample(8, random_state=623))
    
```


# 선형회귀분석
```
```


# PCA 자원축소
- sklearn.decomposition.PCA
```
pca = sklearn.decomposition.PCA(n_components=2)
pca.fit(X)
pca_array = pca.transform(X)
```

