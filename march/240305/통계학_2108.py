n = int(input())

ls = [int(input()) for _ in range(n)]

# 산술평균
first = sum(ls) / n
print(round(first))

# 중앙값
ls.sort()
print(ls[n//2])

# 최빈값
mode_dict = {}
for i in ls:
    if i not in mode_dict:
        mode_dict[i] = 1
    else:
        mode_dict[i] += 1
# print(mode_dict)
# print(max(mode_dict.values()))

# 갯수의 최댓값
max_val = max(mode_dict.values())

mode_key = []
for i in mode_dict.keys():
    if mode_dict[i] == max_val:
        mode_key.append(i)
# print('mode_key :', mode_key)
mode_key.sort()

if len(mode_key) >= 2:
    # 두번째로 작은 값 print
    print(mode_key[1])
else:
    print(mode_key[0])

# 범위
print(max(ls) - min(ls))