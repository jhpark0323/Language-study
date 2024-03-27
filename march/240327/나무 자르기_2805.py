'''
내림차순 정렬하고 처음부터 순회해서 다음 나무의 길이까지 잘라서 가져감
'''

import math
import sys

ipt = sys.stdin.readline

n, m = map(int, ipt().strip().split())
ls = list(map(int, ipt().strip().split()))

ls.sort(reverse=True)

length = 0
# 처음 높이는 제일 긴거 기준
ans = ls[0]
# ls 순회
for i in range(n-1):
    cut = ls[i] - ls[i+1]
    if length + (i+1) * cut < m:
        # 잘리는 나무는 하나씩 늘어남
        length += (i+1) * cut
        ans -= cut

    elif length + (i+1) * cut == m:
        ans -= cut
        break

    else:
        # print('ans :', ans)
        # 남은 길이
        left = m - length
        # print('left :', left)
        # 한 그루당 더 필요한 높이
        more = math.ceil(left / (i+1))
        ans -= more
        break
# 끝까지 왔는데도 break가 안걸림
else:
    # print('ans :', ans)
    # print('length :', length)
    # print(m)
    # 한 그루당 더필요한 높이
    more = math.ceil((m - length) / n)
    # print('more :', more)
    ans -= more
print(ans)

'''
5 6
10 10 10 10 9
'''

'''
5 6
50 50 50 50 49
'''