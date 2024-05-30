n = int(input())
height = [int(input()) for _ in range(n)]
# print(height)

stack = []
cnt = 0
for i in height:
    # stack안에 건물이 있고 마지막이 현재 건물보다 작으면
    while stack and stack[-1] <= i:
        # 뺀다
        stack.pop()
    # 다 뺴고 난 후 현재 건물을 append
    stack.append(i)

    cnt += len(stack) - 1

print(cnt)