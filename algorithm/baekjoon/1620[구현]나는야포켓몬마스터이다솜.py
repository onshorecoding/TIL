import sys


class Pokemon:
    def __init__(self, lst: list):
        self.pokelist = lst

    def get_pokemon(self, v: str):
        try:
            idx = int(v)
            return self.pokelist[idx-1]
        except:
            return self.pokelist.index(v) + 1


input = sys.stdin.readline
N, M = map(int, input().split())
lst = [input().rstrip() for _ in range(N)]

pokemon = Pokemon(lst)
ans = []
for _ in range(M):
    v = input().rstrip()
    print(pokemon.get_pokemon(v))
