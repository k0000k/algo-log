word = input()

for i in range(97, 123):
    char = chr(i)
    for j in word:
        if (char == j):
            print(word.index(char), end=" ")
            break
    else:
        print(-1, end=" ")

