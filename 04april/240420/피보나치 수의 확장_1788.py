n = int(input())

fibo = [0, 1]
new_n = abs(n)
for i in range(2, new_n+1):
    fibo.append((fibo[i-1] + fibo[i-2]) % 1000000000)

if n < 0 and new_n % 2 == 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(fibo[new_n])

