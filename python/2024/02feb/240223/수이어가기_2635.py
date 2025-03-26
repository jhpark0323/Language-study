n = int(input())

# 첫번째 : n, 두번째 : k
def f(n, k):
    ls = [n, k]
    cnt = 2
    first = n
    second = k

    while 1:
        # 두개뺏을때 음수가 아니면 append하고 cnt += 1 하고 first, second 재정의
        if first - second >= 0:
            ls.append(first - second)
            cnt += 1
            first, second = ls[-2], ls[-1]
        # 음수면 return
        else:
            return ls, cnt

# print(f(100, 62))
# print(f(100, 62)[1])

count = 0
answer = []
for i in range(1, n+1):
    # 함수돌리기
    go = f(n, i)
    if count < go[1]:
        answer = go
        count = go[1]

print(answer[1])
print(*answer[0])