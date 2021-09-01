import sys
from collections import deque

if __name__=="__main__":
    k, n = map(int, sys.stdin.readline().split())
    queue = deque([str(idx) for idx in range(1, k+1)])
    answer = []

    for i in range(k):
        for _ in range(n-1):
            first_data = queue.popleft()
            queue.append(first_data)
        answer.append(queue.popleft())

    # print(f"<{', '.join(answer)}>")
    print("<", end="")
    print(", ".join(answer), end="")
    print(">", end="")
