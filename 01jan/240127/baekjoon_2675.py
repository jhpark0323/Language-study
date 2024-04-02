T = int(input())
for test_case in range(T):
    # r : 반복횟수, s : 문자열
    r, s = input().split()
    r = int(r)

    answer = ''
    for i in range(len(s)):
        answer += s[i] * r

    print(answer)
