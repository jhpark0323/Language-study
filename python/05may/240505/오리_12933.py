word = input()
duck = {
    'q': 0,
    'u': 0,
    'a': 0,
    'c': 0,
    'k': 0,
}

ans = 0
new_duck = 0
# word를 돌며 순회
for i in word:
    duck[i] += 1
    if i == 'q':
        new_duck += 1
        ans += 1

        # k+1 보다 크면
        if ans > new_duck:
            ans -= 1

    # u가 나왔는데
    elif i == 'u':
        # q가 많아야함
        if duck['q'] >= duck['u']:
            pass
        # 아니면 끝
        else:
            exit(print(-1))

    elif i == 'a':
        # q, u가 더 많아야함
        if duck['q'] >= duck['u'] >= duck['a']:
            pass
        # 아니면 끝
        else:
            exit(print(-1))

    elif i == 'c':
        # q, u, a가 더 많아야함
        if duck['q'] >= duck['u'] >= duck['a'] >= duck['c']:
            pass
        # 아니면 끝
        else:
            exit(print(-1))

    elif i == 'k':
        new_duck -= 1
        # q, u, a, c가 더 많아야함
        if duck['q'] >= duck['u'] >= duck['a'] >= duck['c'] >= duck['k']:
            pass
        # 아니면 끝
        else:
            exit(print(-1))

# 마지막으로 다 같은지 확인
if duck['q'] == duck['u'] == duck['a'] == duck['c'] == duck['k']:
    print(ans)

else:
    print(-1)