from itertools import permutations

'''
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
'''
# 35

'''
참고로 시간초과나서 pypy3로 돌림
'''

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

path = list(permutations(range(n)))
# print(path)

# 최소 비용 초기화
min_cost = float('inf')

# 순열을 순회
for p in path:
    # print(p)

    # 매 순열마다 계산 할 cost
    cost = 0
    # 이전 위치, 여기서는 마지막에서 처음위치로 올때가 될듯
    prev = p[-1]
    # 각 도시를 순회
    for city in p:
        # 만약 다음 위치가 0이면 그곳은 못감
        if arr[prev][city] == 0:
            cost = float('inf')
            break
        # 비용은 저번 곳에서 현재 위치로
        cost += arr[prev][city]
        # 저번 곳 갱신
        prev = city

    if min_cost > cost:
        min_cost = cost
print(min_cost)