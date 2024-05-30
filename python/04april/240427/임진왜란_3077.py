import sys
input = sys.stdin.readline
n = int(input())

ls = list(input(). split())
ans_ls = list(input(). split())
# print(ls)

question_dict = {}
for i in range(n):
    question_dict[ls[i]] = i
# print(question_dict)

answer = 0
for first in range(n):
    for second in range(first+1, n):
        if question_dict[ans_ls[first]] < question_dict[ans_ls[second]]:
            answer += 1

total = n*(n-1)//2

print(f'{answer}/{total}')