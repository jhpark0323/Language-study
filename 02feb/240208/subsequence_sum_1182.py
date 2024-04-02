import itertools

n, s = map(int, input().split())

ls = list(map(int, input().split()))

# 부분집합을 담을 list
subsequence = []

# 반복문으로 부분집합의 원소의 갯수를 순회하여 각 i마다의 부분집합들을 전부 subsequence에 extend
for i in range(1, n+1):
    subsequence.extend(list(itertools.combinations(ls, i)))

# print(subsequence)

# 정답을 담을 list
answer = []

# 갯수만 찾으면 되므로 갯수를 담을 cnt 할당
cnt = 0
for i in subsequence:
    # 각 부분집합의 합이 s와 같다면 cnt += 1
    if sum(i) == s:
        cnt += 1

print(cnt)