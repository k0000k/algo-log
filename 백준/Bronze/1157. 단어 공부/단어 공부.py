import sys

word = sys.stdin.readline().rstrip()
alpha = [0 for i in range(26)]

for i in word:
    if 65 <= ord(i) <= 90:
        alpha[ord(i) - 65] += 1
    else:
        alpha[ord(i) - 97] += 1

max_alpha = max(alpha)
if (alpha.count(max_alpha) != 1):
    print("?")
else:
    print(chr(alpha.index(max_alpha) + 65))