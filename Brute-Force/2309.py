h = []

for i in range(9):
    h.append(int(input()))

sum_of_h = sum(h)
h.sort()

for i in range(9):
    for j in range(i + 1, 9):
        if (sum_of_h - h[i] - h[j] == 100):
            for k in range(9):
                if (k == i or k == j):
                    continue
                print(h[k])
            exit()
