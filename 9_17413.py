import sys
from collections import deque


stack = []
queue = deque()

def print_stack():
    while stack:
        print(stack.pop(), end="")

def print_queue():
    while queue:
        print(queue.popleft(), end="")

if __name__=="__main__":
    problem = sys.stdin.readline().rstrip()

    in_tag = False
    for item in problem:
        if in_tag:
            queue.append(item)
            if item == ">":
                print_queue()
                in_tag = False
        else:
            if item == "<":
                print_stack()
                queue.append(item)
                in_tag = True
            elif item == " ":
                print_stack()
                print(" ", end="")
            else:
                stack.append(item)

    print_stack()
