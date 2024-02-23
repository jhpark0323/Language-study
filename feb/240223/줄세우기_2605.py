n = int(input())

std = list(map(int, input().split()))
ans = []
for i in range(n):
  ans.insert(i - std[i], i+1)

for i in range(len(ans)):
  print(ans[i], end = ' ')