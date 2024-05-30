n, m = map(int, input().split())
ls = []
# ls에 2차원 배열로 담기
for _ in range(m):
    ls.append(list(map(int, input().split())))
# print(ls)

# basket list에 처음 세팅하기
basket = [i for i in range(1, n+1)]
# basket : [1,2,3,4,5 ...]
# print(basket)

# basket안의 공의 위치를 바꿈
# 이때 index조심 1씩 빼줘야함
for i in range(m):
    basket[ls[i][0]-1], basket[ls[i][1]-1] = basket[ls[i][1]-1], basket[ls[i][0]-1]

print(*basket)