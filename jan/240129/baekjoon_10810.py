n, m = map(int, input().split())

# n개의 바구니에 대한 list -> 각 번호에 저장, 대신 0부터 시작
basket = [0]*(n+1)

# ls에 각 i, j, k를 받아옴
ls = []
for _ in range(m):
    ls.append(list(map(int, input().split())))
# print(ls)

# i부터 j까지의 index에 k를 넣음
for ls_a in range(m):
    for ls_b in range(ls[ls_a][0], ls[ls_a][1] + 1):
        basket[ls_b] = ls[ls_a][2]

print(*basket[1:])