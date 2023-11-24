a1, b1 = input().split()
a2, b2 = input().split()
a3, b3 = input().split()

result_a = 0
result_b = 0

if (a1 == a2):
    result_a = a3
elif (a2 == a3):
    result_a = a1
elif (a1 == a3):
    result_a = a2

if (b1 == b2):
    result_b = b3
elif (b2 == b3):
    result_b = b1
elif (b1 == b3):
    result_b = b2

print(result_a, result_b)