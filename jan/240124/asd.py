n = int(input())

# prime number 시작 : 2
i = 2
while True:
    if n == 1: # n을 계속 나누다 1이되면 break
        break

    if n % i == 0: # n이 i로 나눠떨어질때
        print(i)
        n //= i  # n을 i로 나눈 몫을 다시 n에 할당
        i = 2  # prime number 재할당
    else:
        i += 1  # 다음 i로 넘김