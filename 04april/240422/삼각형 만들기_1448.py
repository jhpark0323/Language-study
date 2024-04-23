import sys
input = sys.stdin.readline
n = int(input())
ls = [int(input()) for _ in range(n)]
# print(ls)

ls.sort(reverse=True)
# print(ls)

for i in range(n-2):
    a, b, c = ls[i], ls[i+1], ls[i+2]

    if a < b + c:
        print(a+b+c)
        break
else:
    print(-1)