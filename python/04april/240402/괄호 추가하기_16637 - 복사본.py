from copy import deepcopy

n = int(input())

ls = list(input())
print(ls)

word = ''.join(ls)

# ls.insert(3, ')')
# ls.insert(0, '(')
# ls.insert(5, ')')
# ls.insert(2, '(')
# ls.insert(7, ')')
# ls.insert(4, '(')
# ls.insert(9, ')')
# ls.insert(6, '(')
#
# print(ls)

print(eval(word[0:3]))

if n == 1:
    print(ls[0])
    exit()

for i in range(0, n, 2):
    eval(word[i:i+3])



for i in range(3, n+1, 2):
    new_ls = deepcopy(ls)
    # new_ls.insert(i, ')')
    # new_ls.insert(i-3, '(')
    print(new_ls[i-3 : i])
    word = ''.join(new_ls[i-3 : i])
