n, m = map(int, input().split())
ls = list(map(int, input().split()))
# print(ls)

ls.sort()

def back(cnt):
    if cnt == m:
        return print(*path)

    for i in ls:
        if not path or i >= path[-1]:
            path.append(i)
            back(cnt+1)
            path.pop()

path = []
back(0)
