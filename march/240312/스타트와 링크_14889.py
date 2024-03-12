from itertools import combinations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

# 조합을 만드는데 집합의 형태로 만듬
p = set(i for i in range(n))
combi = list(map(set, combinations(p, n//2)))
# print(combi)

# 20C10 = 184,756 할만할듯?

min_ans = float('inf')
# ls를 순회하며 각각의 합을 구해 min값을 찾는다
for i in combi:
    # 각팀으로 나눔
    start, link = list(i), list(p - i)

    # start팀과 link팀 능력치 변수
    start_ability = 0
    link_ability = 0

    # 전부다 순회하면서 찾음
    for i in range(n//2):
        for j in range(n//2):
            start_ability += arr[start[i]][start[j]]
            link_ability += arr[link[i]][link[j]]

    answer = abs(start_ability-link_ability)
    if min_ans > answer:
        min_ans = answer

print(min_ans)