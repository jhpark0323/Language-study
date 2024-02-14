'''
10
-7 -5 2 3 8 -2 4 6 9 0
'''

n = int(input())
arr = list(map(int, input().split()))

def f(arr, n):
    for i in range(1, 1<<n):
        s = 0
        for j in range(n):
            if i & (1 << j):
                s += arr[j]
        #         print(arr[j], end = ' ')
        # print('sum : ',s)
        if s == 0:
             return True
    return False
print(f(arr, n))
