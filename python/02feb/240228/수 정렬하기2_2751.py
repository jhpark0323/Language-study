import sys

n = int(sys.stdin.readline().strip())
ls = [int(sys.stdin.readline().strip()) for _ in range(n)]
# print(ls)

ls.sort()
for i in ls:
    print(i)