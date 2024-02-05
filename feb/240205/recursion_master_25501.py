
'''
머라는지 모르겠어서 걍 문제 빼껴 씀;
'''

def recursion(s, l, r):
    global cnt
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        cnt += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())

ls = [input() for _ in range(n)]

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'), cnt)
for i in range(n):
    cnt = 1
    print(isPalindrome(ls[i]), cnt)