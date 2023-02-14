import sys

word = sys.stdin.readline().rstrip()

for i in word:
    if (i.isalpha()):
        temp = ord(i)
        if (97 <= temp <= 109 or 65 <= temp <= 77):
            print(chr(temp + 13), end="")
        elif (temp <= 90):
            rem = temp + 13 - 90
            print(chr(65 + rem - 1), end="")
        else:
            rem = temp + 13 - 122
            print(chr(97 + rem - 1), end="")

    else:
        print(i, end="")
