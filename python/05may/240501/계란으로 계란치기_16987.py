n = int(input())
s = [0]*n
w = [0]*n

for i in range(n):
    s[i], w[i] = map(int, input().split())

res = 0
def backtracking(idx, eggs):
    global res
    if idx == n:
        cnt = 0
        for i in range(n):
            if eggs[i] <= 0:
                cnt +=1
        if cnt > res:
            res = cnt
        return

    if eggs[idx] > 0:
        flag = False
        for i in range(n):
            if eggs[i] > 0 and i != idx:
                flag = True
                tmp = eggs[:]
                tmp[i] -= w[idx]
                tmp[idx] -= w[i]
                backtracking(idx+1, tmp)
        if not flag:
            backtracking(idx+1, eggs)
    else:
        backtracking(idx+1, eggs)

backtracking(0, s)
print(res)