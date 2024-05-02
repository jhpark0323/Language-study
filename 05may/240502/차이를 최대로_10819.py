n = int(input())
ls = list(map(int, input().split()))

def back(cnt):
    global ans
    if cnt == n:
        # print(a)

        new_ans = cal(a)
        if ans < new_ans:
            ans = new_ans
        return

    for i in range(n):
        if i not in idx:
            idx.append(i)
            a.append(ls[i])
            back(cnt+1)
            idx.pop()
            a.pop()

def cal(list):
    num = 0
    for j in range(0, n-1):
        new_num = abs(list[j] - list[j+1])
        num += new_num
    # print(list, num)
    return num

a = []
idx = []
ans = 0
back(0)
print(ans)