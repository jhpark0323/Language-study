n = int(input())

ls = list(int(input()) for _ in range(n))

print(ls)

stack = []
answer = []
start = 1
while len(answer) != n:
