import sys

N = int(sys.stdin.readline())

for i in range(N):
    cnt, word = sys.stdin.readline().rstrip().split()
    for char in word:
        for j in range(int(cnt)):
            print(char, end="")
    print()