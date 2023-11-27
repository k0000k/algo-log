n = int(input())

for i in range(n):
    string = input()
    answer = 0
    current_score = 0
    for j in string:
        if (j == "O"):
            current_score += 1
            answer += current_score
        else:
            current_score = 0
    print(answer)