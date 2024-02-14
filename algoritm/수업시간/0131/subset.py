n = 3
arr = [1, 2, 3]

for i in range(1<<n):
    s = 0
    for j in range(n):
        if i & (1 << j):
            s += arr[j]
            print(arr[j], end = ' ')
    print('sum : ',s)
'''
sum :  0
1 sum :  1
2 sum :  2
1 2 sum :  3
3 sum :  3
1 3 sum :  4
2 3 sum :  5
1 2 3 sum :  6
'''