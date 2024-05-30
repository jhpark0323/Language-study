n, m = map(int, input().split())

# ls에 m번 바구니의 순서를 바꾸는 경우를 append
ls = []
for i in range(m):
    ls.append(list(map(int, input().split())))

# basket에 0 ~ n까지 숫자 입력 -> 이렇게 해야 나중에 index에서 안 헷갈림 -> 마지막에 답구할 때는 첫번째 0만 빼면 됨
basket = [i for i in range(n+1)]

for i in range(m):
    basket[ls[i][0]:ls[i][1]+1] = basket[ls[i][1]:ls[i][0]-1:-1]

print(*basket[1:])