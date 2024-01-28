n, b = input().split()
b = int(b)
# print(n, b)

# print(ord('A'))

alphabet = {}

for i in range(65, 91):
    # print(chr(i))
    alphabet[chr(i)] = i - 55

for i in range(10):
    alphabet[str(i)] = i

# print(alphabet)
cnt = 1
answer = 0
for i in n:
    answer += alphabet[i] * (b ** (len(n) - cnt))
    cnt += 1
print(answer)