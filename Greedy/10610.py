import sys

N = list(sys.stdin.readline().rstrip())

if ("0" not in N):
    print(-1)
    sys.exit()

sum = 0
for i in N:
    sum = sum + int(i)
    
if (sum % 3 != 0):
    print(-1)
    sys.exit()
    
N.sort(reverse=True)
result = ""

for i in N:
    result += i

print(result)
    
