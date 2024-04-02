ls = [i for i in range(1, 31)]

for _ in range(28):
    ls.remove(int(input()))

ls.sort()

for i in range(len(ls)):
    print(ls[i])