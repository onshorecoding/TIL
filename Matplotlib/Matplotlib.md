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