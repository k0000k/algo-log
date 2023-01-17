month, day = map(int, input().split())

month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

sum = 0

for i in range(month):
    sum = sum + month_list[i]
sum = sum + day

print(day_list[sum % 7])
