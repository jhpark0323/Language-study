word = input()

cap_word = word.upper()
# print(cap_word)

arr = [0] * 26

for i in cap_word:
    # print(ord(i))
    arr[ord(i)-65] += 1

# arr.index(max(arr)) -> arr배열의 제일 큰 수의 index

# print(arr.count(max(arr)))
# print(ord('a'))
if arr.count(max(arr)) >= 2:
    print('?')
else:
    print(chr(arr.index(max(arr)) + 65))