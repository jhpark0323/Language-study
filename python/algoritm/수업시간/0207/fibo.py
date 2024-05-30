def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

cnt = 0
n =7
print(fibo(n), cnt)  # 13 41


def fibo_memo(n):
    global cnt
    cnt += 1
    # n이 2이상이고 memo의 n번째 idx가 비어있으면
    if n >= 2 and memo[n] == 0:
        # memo의 n번째 idx에 재귀를 이용해 전항과 전전항을 더해서 저장해라
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    # memo의 n번째 idx 0이 아니면 memo[n] return
    return memo[n]

cnt = 0
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
print(fibo_memo(n), cnt)  # 13 13