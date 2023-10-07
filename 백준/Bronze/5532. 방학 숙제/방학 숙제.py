import sys

l = int(sys.stdin.readline().rstrip())
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
d = int(sys.stdin.readline().rstrip())

if (a % c != 0):
    kor = (a // c) + 1
else:
    kor = (a // c)

if (b % d != 0):
    math = (b // d) + 1
else:
    math = (b // d)

if (kor > math):
    print(l - kor)
else:
    print(l - math)
