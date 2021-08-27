
# 내 풀이
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    problem = sys.stdin.readline().rstrip()
    _stack = []
    stack_size = 0
    status = None

    for item in problem:
        if item == "(":
            _stack.append(item)
            stack_size += 1
        else:
            if stack_size == 0:
                status = False
                break
            top = _stack[stack_size-1]
            if top == ")":
                status = False
                break
            stack_size -= 1
            _stack.pop()

    if stack_size != 0 or status == False:
        print("NO")
    else:
        print("YES")
