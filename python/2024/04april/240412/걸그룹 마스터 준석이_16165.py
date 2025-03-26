n, m = map(int, input().split())

girl_group = {}
for _ in range(n):
    # 그룹 이름
    group = input()
    # 멤버 수
    member = int(input())
    # 멤버
    member_ls = sorted([input() for _ in range(member)])
    # 딕셔너리에 추가
    girl_group[group] = member_ls

# print(girl_group)

for _ in range(m):
    question = input()
    q_type = int(input())

    # q_type이 1이면
    if q_type:
        # girl_group.items를 순회하며
        for group_name, member_name in girl_group.items():
            # value값에 question이 있으면
            if question in member_name:
                print(group_name)
                break
    else:
        for name in girl_group[question]:
            print(name)

