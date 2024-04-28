import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
# ls = [list(map(int, input().split())) for _ in range(n)]

sour = []
bitter = []
for i in range(n):
    s_taste, b_taste = map(int, input().split())
    sour.append(s_taste)
    bitter.append(b_taste)
# print('sour :', sour)
# print('bitter :', bitter)

p = [i for i in range(n)]

combi = []
for i in range(1, n+1):
    combi.extend(list(combinations(p, i)))
# print(combi)


min_diff = float('inf')
for each_combi in combi:
    sour_product = 1
    bitter_sum = 0
    for each in each_combi:
        sour_product *= sour[each]
        bitter_sum += bitter[each]

    diff = abs(sour_product-bitter_sum)
    if min_diff > diff:
        min_diff = diff


# print('diff :', min_diff)
print(min_diff)