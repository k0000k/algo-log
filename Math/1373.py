import sys

str_bin = sys.stdin.readline().rstrip()

print(format(int("0b" + str_bin, 2), 'o'))
