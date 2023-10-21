meat, cheese = map(int, input().split())

if (meat > cheese):
    print(cheese + cheese + 1)
elif (meat <= cheese):
    print(meat - 1 + meat)
