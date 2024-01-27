s = input()

ls = [-1 for _ in range(26)]

after = ''

for i in range(len(s)):
    if s[i] not in after:
        ls[ord(s[i])-97] = i
        after += s[i]
    
print(*ls)
# print(ord('a'))