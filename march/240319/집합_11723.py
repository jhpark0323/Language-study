import sys

m = int(input())

s = set()
ipt = sys.stdin.readline
for i in range(m):
    ipt_data = list(map(str, ipt().strip().split()))
    # print(ipt_data)

    if ipt_data[0] == 'add':
        s.add(ipt_data[1])

    elif ipt_data[0] == 'remove':
        if ipt_data[1] in s:
            s.remove(ipt_data[1])
        else:
            continue

    elif ipt_data[0] == 'check':
        if ipt_data[1] in s:
            print(1)
        else:
            print(0)

    elif ipt_data[0] == 'toggle':
        if ipt_data[1] in s:
            s.remove(ipt_data[1])
        else:
            s.add(ipt_data[1])

    elif ipt_data[0] == 'all':
        s = {str(i) for i in range(1, 21)}
        # print(s)

    elif ipt_data[0] == 'empty':
        s = set()

    # print(s)