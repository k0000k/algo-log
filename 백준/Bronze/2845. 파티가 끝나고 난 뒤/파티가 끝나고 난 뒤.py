L, P = map(int, input().split())
peoples = list(map(int, input().split()))

member = L * P

for i in peoples:
    print(i - member, end=" ")