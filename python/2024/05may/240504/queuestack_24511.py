import sys
input = sys.stdin.readline
n = int(input())
an = list(map(int, input().split()))
bn = list(map(int, input().split()))
m = int(input())
cn = list(map(int, input().split()))

ls = []
i = 0
for j in range(n-1, -1, -1):
    # 뽑았을 때 0이면
    if not an[j]:
        ls.append(bn[j])
        i += 1
        print(bn[j], end = ' ')

        if i == m:
            break
# for문을 다 돌았음에도 i가 m을 채우지 못하면
else:
    for j in range(m-i):
        print(cn[j], end=' ')


