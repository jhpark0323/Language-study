from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    ls = list(input().split())
    # print(ls)

    ans = deque([])
    for i in range(n):
        if i == 0:
            ans.append(ls[i])

        else:
            # 맨앞의 글자보다 아스키코드가 크면
            if ord(ans[0]) < ord(ls[i]):
                # 뒤에다 append
                ans.append(ls[i])
            # 작으면
            else:
                ans.appendleft(ls[i])

    print(''.join(ans))