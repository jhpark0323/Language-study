n = int(input())

ls = [0] + list(int(input()) for _ in range(n))
# print(ls)

count = 0
ans = 0
for i in range(1, n+1):
    visited = [0] * (n+1)
    visited[i] = 1
    stack = [i]
    cnt = 0
    while stack:
        current = stack.pop()
        cnt += 1

        next_ = ls[current]
        if not visited[next_]:
            stack.append(next_)
            visited[next_] = 1
    # print(visited)
    if count < cnt:
        count = cnt
        ans = i
print(ans)