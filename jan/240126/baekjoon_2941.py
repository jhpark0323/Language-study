word = input()

# croatia 단어 사전
croatia = {
    'c=' : 1,
    'c-' : 1,
    'dz=' : 1,
    'd-' : 1,
    'lj' : 1,
    'nj' : 1,
    's=' : 1,
    'z=' : 1
    }

croatia_ls = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 전체 단어 수 - 크로아티아 단어 수 + 치환할 때 마다 하나씩 추가
change_word = 0
croatia_word = 0
new_word = word
# 두개이상 있으면?

for i in croatia_ls:
    while 1:
        if i in new_word:
            change_word += 1
            croatia_word += len(i)
            # 있는 단어를 *로 바꿈 -> croatia_ls에 * 이 없기에 바꿔도 다시 겹칠일이 없음
            # '' (공백)으로 바꾸게 되면 nljj같은 경우 lj가 사라지고 nj가 되어 다시 한번 ls에 있는 단어가 나와서 이상하게 한번더 지워짐
            new_word = new_word.replace(i, '*', 1)
            # print(new_word)
        if i not in new_word:
            # print(i)
            break

# print(change_word)
# print(croatia_word)
# print(len(word))

print(change_word + (len(word) - croatia_word))