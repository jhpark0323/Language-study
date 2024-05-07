T = int(input())

for _ in range(T):
    record = input().split()
    ls = []
    while True:
        ipt = input()
        if ipt == 'what does the fox say?':
            break
        else:
            ls.append(ipt.split()[2])
    # print(ls)

    for i in record:
        if i not in ls:
            print(i, end=' ')

