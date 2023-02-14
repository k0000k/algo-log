import sys

word = sys.stdin.readline().rstrip()
tails = []

for i in range(len(word)):
    tails.append(word[i:])

tails.sort()

for i in tails:
    print(i)
