import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)
    exit()

ls = [int(sys.stdin.readline()) for _ in range(n)]

ls.sort()
# print(ls)

# 제외할 사람 수
# 반올림 하기
delete = int(n * 0.15 + 0.5)

# 제외한 new_ls
if delete == 0:
    new_ls = ls
else:
    new_ls = ls[delete:-delete]
# print(new_ls)

answer = int(sum(new_ls) / len(new_ls) + 0.5)
print(answer)