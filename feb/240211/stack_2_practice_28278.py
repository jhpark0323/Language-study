class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if not self.items:
            return 1
        else:
            return 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return -1

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return -1

    def size(self):
        return len(self.items)

# cnt = 0
stack = Stack()

n = int(input())

ls = [list(map(int, input().split())) for _ in range(n)]

for i in ls:
    # stack에 정수를 넣음
    if i[0] == 1:
        stack.push(i[1])
        # cnt += 1

    # 스택이 비어있으면 pop으로 출력 없으면 -1 출력
    elif i[0] == 2:
        print(stack.pop())

    # 스택의 길이 출력
    elif i[0] == 3:
        print(stack.size())

    # 스택이 비어있는지 조사
    elif i[0] == 4:
        print(stack.is_empty())
    # 스택에 정수가 있으면 스택의 맨위를 출력
    else:
        print(stack.peek())