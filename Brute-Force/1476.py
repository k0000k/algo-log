E, S, M = map(int, input().split())

year = 1
a = b = c = 1

while (a != E or b != S or c != M):
    year += 1
    a += 1
    b += 1
    c += 1

    if (a == 16):
        a = 1
    if (b == 29):
        b = 1
    if (c == 20):
        c = 1
print(year)
