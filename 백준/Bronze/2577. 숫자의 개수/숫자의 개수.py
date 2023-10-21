a = int(input())
b = int(input())
c = int(input())

result = []
for i in range(10):
    result.append(0)

product = str(a*b*c)
for i in product:
    result[int(i)] += 1

for i in result:
    print(i)