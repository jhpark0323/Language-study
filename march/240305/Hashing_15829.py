l = int(input())

word = input()

alphabet = {}
for i in range(26):
    alphabet[chr(97+i)] = i+1
# print(alphabet)

answer = 0
for i in range(l):
    # word를 하나씩 뽑아 숫자로 치환
    answer += alphabet[word[i]] * (31 ** i)
print(answer % 1234567891)