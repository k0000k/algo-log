import sys

while (True):
    try:
        word = input()

        small = 0
        big = 0
        num = 0
        space = 0

        for i in word:
            if (i.isalpha()):
                if (97 <= ord(i) <= 122):
                    small += 1
                else:
                    big += 1
            elif (i.isdigit()):
                num += 1
            else:
                space += 1

        print(small, big, num, space)
    except:
        sys.exit()
