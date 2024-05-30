n, m = map(int, input().split())
ls = list(map(int, input().split()))
# print(ls)

def back(cnt):
    if cnt == m:
        print(*p)
        return

    for i in ls:
        if i not in p:
            p.append(i)
            back(cnt+1)
            p.pop()

ls.sort()
p = []
back(0)