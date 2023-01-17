N, K = map(int, input().split())

numbers = [i for i in range(1, N + 1)]
counter = K - 1
answer = []

while (True):
    if not numbers:
        break
    if (counter >= len(numbers)):
        counter -= len(numbers)
        continue
    answer.append(numbers[counter])
    del numbers[counter]
    counter += K - 1

answer = str(answer)
print("<" + answer.strip("[]") + ">")
