k = int(input())

ls = [int(input()) for _ in range(k)]
# print(ls)

stack = []

for i in ls:
    # 0이 아니면
    if i != 0:
        stack.append(i)

    else:
        stack.pop()

print(sum(stack))