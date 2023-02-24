import sys

M, N = map(int, sys.stdin.readline().split())
primes = [True for i in range(N + 1)]
primes[0] = False
primes[1] = False

for i in range(2, N + 1):
    if (primes[i] == False):
        continue
    for j in range(i * 2, N + 1, i):
        primes[j] = False

for i in range(M, N + 1):
    if (primes[i] == True):
        print(i)
