import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sentence = sys.stdin.readline()[::-1]
    print(sentence)