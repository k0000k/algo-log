word = input()
counter = 0

for i in word:
    print(i, end="")
    counter += 1

    if (counter % 10 == 0):
        print()
