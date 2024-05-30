n = int(input())

def tf(now):
    # 같은 열에 있으면 안됨
    if now in path:
        return False

    now_idx = len(path)

    # 대각선 비교
    for origin in range(now_idx):
        # 원래있던것들의 index와 새로 들어온 index의 차이가 두 숫자이 차이와 같으면 대각선으로 겹침
        if now_idx - origin == abs(path[origin] - now):
            return False

    return True

def back(cnt):
    global ans

    # 종료조건
    if cnt == n:
        ans += 1
        return

    # 전체 순회
    for i in range(n):
        # 조건을 만족하면
        if tf(i):
            path.append(i)
            back(cnt+1)
            path.pop()

path = []
ans = 0
back(0)
print(ans)