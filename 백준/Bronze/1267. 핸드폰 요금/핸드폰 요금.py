cnt = int(input())
calls = list(map(int, input().split()))

fee_y = 0
fee_m = 0
for i in calls:
    fee_y += (i // 30 + 1) * 10
    fee_m += (i // 60 + 1) * 15

if (fee_m == fee_y):
    print("Y M", fee_y)
elif (fee_m < fee_y):
    print("M", fee_m)
else:
    print("Y", fee_y)