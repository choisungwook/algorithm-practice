import sys
class Stack:
    def __init__(self):
        self.stack = []

    def GetTop(self):
        size = self.GetSize()
        if size == 0:
            return -1
        return self.stack[size-1]

    def GetSize(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        size = self.GetSize()
        if size == 0:
            return -1
        return self.stack.pop()

stack = Stack()
comparable = []
result = []
current_comparable_idx = 0


n = int(input())

for _ in range(n):
    comparable.append(int(sys.stdin.readline()))


for idx in range(1, n+1):
    stack.push(idx)
    result.append("+")

    while stack.GetTop() != -1 and current_comparable_idx < len(comparable) and (stack.GetTop() == comparable[current_comparable_idx]):
        result.append("-")
        stack.pop()
        current_comparable_idx += 1

if stack.GetSize() == 0:
    print("\n".join(result))
else:
    print("NO")


#  두 번째 풀이 -> 더 오래걸림
import sys

i = 1
answer = []
stack = []
for _ in range(int(input())):
    n = int(input())

    while i <= n:
        answer.append("+")
        stack.append(i)
        i += 1

    if stack[-1] == n:
        answer.append("-")
        stack.pop()

if stack:
    print("NO")
else:
    print("\n".join(answer))


# from collections import deque
# import sys
# stack = deque([])
# answer = []
# i=1

# for _ in range(int(input())):
#     n = int(sys.stdin.readline())
#     while i<=n:
#         stack.append(i)
#         answer.append('+')
#         i+=1
#     if stack[-1]== n:
#         stack.pop()
#         answer.append('-')

# if stack:
#     print('NO')
# else:
#     print(*answer,sep='\n')


# import sys
# n = int(sys.stdin.readline())
# stack = []
# cur = 1
# out = []
# done = False

# for _ in range(n):
#     v = int(sys.stdin.readline())
#     while v >= cur:
#         stack.append(cur)
#         cur += 1
#         out.append('+')
#     print(stack)
#     if stack.pop() > v:
#         done = True
#         break
#     else:
#         out.append('-')

# sys.stdout.write('NO') if done else sys.stdout.write('\n'.join(out))