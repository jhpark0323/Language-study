from itertools import permutations

'''
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
'''
# 35

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

path = list(permutations(range(n)))
# print(path)

min_cost = float('inf')  # 최소 비용 초기화
for p in path:
    cost = 0  # 현재 경로의 비용
    prev = p[-1]  # 이전 도시
    # print(p)
    # print('prev :', prev)
    for city in p:
        # 만약 가려고 한 곳이 0이면 거기로 못감
        if arr[prev][city] == 0:
            cost = float('inf')
            break
        cost += arr[prev][city]  # 이전 도시에서 현재 도시로 이동하는 비용 더하기
        # print(prev, city)
        prev = city
    if min_cost > cost:  # 최소 비용 업데이트
        min_cost = cost

print(min_cost)