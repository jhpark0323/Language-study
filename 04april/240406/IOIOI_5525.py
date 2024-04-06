import sys

input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
s = input().strip()


cnt = 0
ans = 0
location = 0

while location < m-1:
    # 현재 위치부터 2칸뒤까지가 IOI이면
    if s[location:location+3] == 'IOI':
        # cnt 증가
        cnt += 1
        # location은 두칸 건너뜀
        location += 2
        # 총 n번 연속으로 같으면 Pn 존재
        if cnt == n:
            ans += 1
            # 이 때 바로 뒤에 또 IOI형태가 나오면 또 다시 Pn이 존재하는 것이므로
            # cnt는 초기화가 아닌 1만 뺴줌
            cnt -= 1
    # 다르면
    else:
        # cnt초기화
        cnt = 0
        # location 증가
        location += 1

print(ans)