n = int(input())

arr = [input() for _ in range(n)]

for i in arr:
    if 6 <= len(i) <= 9:
        print('yes')
    else:
        print('no')