import sys
input = sys.stdin.readline
n, c = map(int, input().split())
ls = list(map(int, input().split()))

ls_dict = {}
for i in range(n):
    # 없는 원소면
    if ls[i] not in ls_dict.keys():
        ls_dict[ls[i]] = [1, n-i]
    # 있는 원소면
    else:
        ls_dict[ls[i]][0] += 1

# print(ls_dict)

ls.sort(key= lambda x: ls_dict[x], reverse=True)
print(*ls)