import sys

def dfs(i, ans, add, sub, mul, div):
    global max_val
    global min_val

    # 다 구했을 때 비교
    if i == n:
        if max_val < ans:
            max_val = ans
        if min_val > ans:
            min_val = ans
        return
    # 각각의 연산자 기준 dfs 진행
    else:
        if add:
            dfs(i + 1, ans + an[i], add - 1, sub, mul, div)
        if sub:
            dfs(i + 1, ans - an[i], add, sub - 1, mul, div)
        if mul:
            dfs(i + 1, ans * an[i], add, sub, mul - 1, div)
        if div:
            dfs(i + 1, int(ans / an[i]), add, sub, mul, div - 1)


n = int(sys.stdin.readline())

# 수열
an = list(map(int, sys.stdin.readline().split()))

# 연산자 : 차례대로 +, -, x, / 의 갯수
add, sub, mul, div = map(int, sys.stdin.readline().split())

max_val = -float('inf')
min_val = float('inf')

dfs(1, an[0], add, sub, mul, div)
print(max_val)
print(min_val)