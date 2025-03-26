n = int(input())
arr = [input() for _ in range(n)]
# print(arr)

chat = set()
cnt = 0
# n번 반복
for i in range(n):
    # ENTER가 들어오면
    if arr[i] == 'ENTER':
        # 이 때 까지 친 채팅 더해주기
        cnt += len(chat)
        # 채팅창 초기화
        chat = set()

    else:
        chat.add(arr[i])
        # print(chat)

cnt += len(chat)

print(cnt)