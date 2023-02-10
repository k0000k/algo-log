import sys

word = sys.stdin.readline().rstrip()
chars = [0 for i in range(26)]

for i in word:
    chars[ord(i) - 97] += 1

for i in chars:
    print(i, end=" ")

