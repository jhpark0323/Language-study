n = int(input())

ls = []
for i in range(n):
    new = input()
    if new not in ls:
        ls.append(new)

ls.sort(key = lambda x: (len(x), x))

for i in ls:
    print(i)