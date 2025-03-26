import sys

input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
s = input().strip()

len_ioi = 2*n+1
ioi = ''
for i in range(len_ioi):
    if i % 2 == 0:
        ioi += 'I'
    else:
        ioi += 'O'
# print(ioi)

cnt = 0
for i in range(m-len_ioi+1):
    if s[i] =='I':
        if s[i:i+len_ioi] == ioi:
            cnt += 1

print(cnt)