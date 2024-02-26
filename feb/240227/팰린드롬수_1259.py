from collections import deque

while 1:
    n = input()
    if n == '0':
        break

    ls = list(n)
    # print(ls)

    deq = deque(ls)
    # print(deq)

    answer = 'yes'
    while len(deq) > 1:
        left = deq.popleft()
        right = deq.pop()
        if left == right:
            pass

        else:
            answer = 'no'
            break

    print(answer)