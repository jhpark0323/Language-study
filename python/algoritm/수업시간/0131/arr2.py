'''
3
1 2 3
4 5 6
7 8 9
'''

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr2 = [[0] * n for _ in range(n)]

# 이렇게 하면 안됨
arr3 = [[0]*n]*n
print(arr3)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
arr3[0][0] = 1
print(arr3)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
# 얕은 복사가 되기 때문에