from itertools import permutations

'''
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
'''
# 35

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
print(arr)

# n까지의 순열을 만듬
p = permutations(range(n))
answer = float('inf')

for permu in p:
    # print(i)
    flag = True
    temp = 0

    for