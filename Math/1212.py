import sys

n = sys.stdin.readline().rstrip()
int_n = int('0o' + n, 8)
print(format(int_n, 'b'))
