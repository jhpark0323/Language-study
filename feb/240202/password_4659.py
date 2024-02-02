
'''
조건1 : 모음 (a,e,i,o,u)중 하나를 무조건 포함
조건2 : 모음, 자음이 연속 3개 나오면 안됨
조건3 : 같은글자 연속2번 X, but ee, oo 허용
'''

word = ''
password_ls = []
while word != 'end':
    word = input()
    password_ls.append(word)

password_ls.remove('end')
# print(password)

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
# print(alphabet)
moeum_ls = ['a', 'e', 'i', 'o', 'u']
jaeum_ls = list(set(alphabet) - set(moeum_ls))

# 조건 1
cnt = 0
clear_1 = []
# password_ls를 순회
for password in password_ls:
    # 모음을 순회
    for moeum in moeum_ls:
        # 모음이 password에 있을시 cnt += 1
        if moeum in password:
            cnt += 1
    # cnt가 1이라도 있으면 모음이 하나라도 있는것 : 조건1 clear
    if cnt >= 1:
        clear_1.append(password)
    cnt = 0

# print(clear_1)

# 조건 2
cnt_2 = 0
fail_2 = []
for password in clear_1:
    # password의 길이가 3이상일 때 연속으로 3개 오는지 확인
    if len(password) >= 3:
        # 순회는 왼쪽글자 기준 전체 길이보다 2적을때 까지
        for i in range(len(password)-2):
            # password의 i번째 글자와 그뒤에 두개 전부 모음일 때
            if (password[i] in moeum_ls) & (password[i+1] in moeum_ls) & (password[i+2] in moeum_ls):
                cnt_2 += 1

            # password의 i번째 글자와 그 뒤에 두개 전부 자음일 때
            if (password[i] in jaeum_ls) & (password[i+1] in jaeum_ls) & (password[i+2] in jaeum_ls):
                cnt_2 += 1

    # cnt_2가 1이라도 있으면 3글자 연속된게 있다는 말
    if cnt_2 >= 1:
        fail_2.append(password)
    cnt_2 = 0

# print(fail_2)

# clear_2에는 차집합으로 계산
clear_2 = list(set(clear_1) - set(fail_2))

# print(clear_2)

# 조건 3
cnt_3 = 0
answer = []
for password_3 in clear_2:
    # password 길이보다 1개 적게 반복
    for i in range(len(password_3)-1):
        # 기준 알파벳과 그 다음 알파벳이 같으면
        if (password_3[i] == password_3[i+1]):
            # 그 알파벳이 e or o인지 확인
            if (password_3[i] != 'e') & (password_3[i] != 'o'):
                cnt_3 += 1
    if cnt_3 == 0:
        answer.append(password_3)
    cnt_3 = 0

# print(answer)
for i in password_ls:
    if i in answer:
        print(f'<{i}> is acceptable.')
    else:
        print(f'<{i}> is not acceptable.')