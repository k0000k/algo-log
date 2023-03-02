import sys

N = int(sys.stdin.readline())
primes = [True for i in range(N + 1)]
primes[0] = False
primes[1] = False
untill_N_primes = []

for i in range(2, N + 1):
    if (primes[i] == True):
        untill_N_primes.append(i)
        for j in range(i + i, N + 1, i):
            primes[j] = False           

for i in untill_N_primes:
    while (N % i == 0):
        print(i)
        N = N // i
