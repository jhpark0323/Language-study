a, b, c = map(int, input().split())

# print(a**b % c)

def f(n):
    if n == 1:
        return a % c

    if n == 2:
        return a**2 % c

    else:
        num = f(n//2)
        # 짝수일때
        if n % 2 == 0:
            return (num * num) % c
        # 홀수일때
        else:
            return (num * num * a) % c

print(f(b))