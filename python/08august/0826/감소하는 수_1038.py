n = int(input())

def backtracking(num, cnt):
    if cnt == n:
        print(num)
        return num

    str_num = str(num)

    for i in range(len(str_num)-1):
        if str_num[i] <= str_num[i+1]:
            break
    else:
        cnt += 1

    num += 1
    backtracking(num, cnt)

a = backtracking(0, 0)
print(a)