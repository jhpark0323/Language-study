n = int(input())

# 받은 정수의 각 자리를 list에 넣음
n_ls = []
for i in str(n):
    n_ls.append(int(i))

# print(n_ls)

# sort후 join
n_ls.sort(reverse=True)

# str형태로 바꾼후 join -> join은 str형태로 바꿔야 가능

for i in range(len(n_ls)):
    n_ls[i] = str(n_ls[i])

answer = ''.join(n_ls)
print(answer)