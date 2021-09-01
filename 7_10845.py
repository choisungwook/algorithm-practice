import sys
from collections import deque

_queue = deque()
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().rstrip().split(' ')

    if command[0] == "push":
        _queue.append(command[1])
    elif command[0] == "pop":
        if len(_queue) == 0:
            print("-1")
        else:
            print(_queue.popleft())
    elif command[0] == "size":
        print(len(_queue))
    elif command[0] == "empty":
        if len(_queue) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if len(_queue) == 0:
            print("-1")
        else:
            print(_queue[0])
    elif command[0] == "back":
        if len(_queue) == 0:
            print("-1")
        else:
            print(_queue[-1])