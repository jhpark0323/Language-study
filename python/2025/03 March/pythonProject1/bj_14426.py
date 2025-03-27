import sys

input = sys.stdin.readline

n, m = map(int, input().split())

hashmap = {}

for i in range(n):
    word = input()
    newWord = ""
    for char in word:
        newWord += char
        hashmap[newWord] = hashmap.get(char, 0) + 1
ans = 0
for i in range(m):
    word = input().strip()
    # print("word = ", word)
    if word in hashmap:
        ans += 1
# print(hashmap)
print(ans)