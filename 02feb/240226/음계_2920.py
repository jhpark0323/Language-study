ls = list(map(int, input().split()))

answer = 'mixed'

s = 0
for i in range(7):
    if ls[i] < ls[i+1]:
        s += 1

if s == 7:
    answer = 'ascending'

s_2 = 0
for i in range(7):
    if ls[i] > ls[i+1]:
        s_2 += 1

if s_2 == 7:
    answer = 'descending'

print(answer)