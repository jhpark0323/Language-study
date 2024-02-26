n = int(input())

ls = []
for i in range(n):
    ls.append(input())

ls.sort(key = lambda x: (len(x), x))

for i in ls:
    print(i)