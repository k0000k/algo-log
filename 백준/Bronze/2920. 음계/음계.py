sounds = list(map(int, input().split()))

for i in range(1, 8):
    interval = sounds[i] - sounds[i - 1]
    if (interval != 1 and interval != -1):
        break
else:
    if (sounds[2] - sounds[1] == 1):
        print("ascending")
        exit()
    elif (sounds[2] - sounds[1] == -1):
        print("descending")
        exit()
print("mixed")
