import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    words = list(sys.stdin.readline().rstrip().split())

    print("Case #" + str(i + 1) + ":", end = " ")
    for j in range(len(words)):
        print(words.pop(), end = " ")
    print()