# 문제: https://www.acmicpc.net/problem/10828
import sys

_stack = []

testcase = int(sys.stdin.readline())

for _ in range(testcase):
    command = sys.stdin.readline().rstrip().split(' ')

    if command[0] == "push":
        _stack.append(command[1])
    elif command[0] == "pop":
        if len(_stack) == 0:
            print("-1")
        else:
            print(_stack.pop())
    elif command[0] == "size":
        print(len(_stack))
    elif command[0] == "empty":
        if len(_stack) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "top":
        if len(_stack) == 0:
            print("-1")
        else:
            print(_stack[len(_stack)-1])
