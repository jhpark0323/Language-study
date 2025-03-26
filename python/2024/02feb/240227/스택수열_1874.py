n = int(input())

ls = list(int(input()) for _ in range(n))
# print(ls)

p = [i for i in range(1, n+1)]
# print(p)

stack = []
answer = []
for i in p:
    # 일단 append
    stack.append(i)
    answer.append('+')

    # append하다가 같아지면
    if stack[-1] == ls[0]:
        # 달라질 때 까지 pop
        while stack and ls and stack[-1] == ls[0]:
            # stack에서 pop
            stack.pop()
            # answer에는 '-' append
            answer.append('-')
            # ls도 pop(0)
            ls.pop(0)

# print(stack)
if stack:
    print('NO')
else:
    for i in answer:
        print(i)