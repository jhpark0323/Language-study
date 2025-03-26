n, m = map(int, input().split())
true_n = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m)]
# print(arr)

# 사실을 아는 사람의 집합
true_ls = set(true_n[1:])
# print(true_ls)

# 총 2번 반복함
for i in range(m):
    for j in range(m):
        party = set(arr[j][1:])
        # print(party, j)
        # print(arr[j])

        # 사실을 아는 사람이 party에 포함이 되어 있을 때
        if true_ls.intersection(party):
            true_ls = true_ls.union(party)

# 최종으로 아는사람들 다 모임
# print(true_ls)

ans = 0
for i in range(m):
    party = set(arr[i][1:])

    if not true_ls.intersection(party):
        ans += 1

print(ans)