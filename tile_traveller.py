userinput('You can travel: ')


def movecharacter(position, userinput):
    if position == 1:
        if userinput == 'n':
            return position + 1
        else:
            pass
    if position == 2:
        if userinput == 'n':
            return position + 1
        elif userinput == 'e':
            return position + 3
        elif userinput == 's':
            return position - 1
        else:
            pass

    if position == 3:
        if userinput == 'e':
            return position + 3
        elif userinput == 's':
            return position - 1
        else:
            pass
    if position == 4:
        if userinput == 'n':
            return position + 1
        else:
            pass
    if position == 5:
        if userinput == 'w':
            return position - 3
        elif userinput == 's':
            return position - 1
        else:
            pass
    if position == 6:
        if userinput == 'w':
            return position - 3
        elif userinput == 'e':
            return position + 3
        else:
            pass
    if position == 7:
        if userinput == 'n':
            return position + 1
        else:
            pass
    if position == 8:
        if userinput == 'n':
            return position + 1
        elif userinput == 's':
            return position - 1
        else:
            pass
    if position == 9:
        if userinput == 'w':
            return position - 3
        elif userinput == 's':
            return position - 1
        else:
            pass


def legalmoves(n, s, w, e):
    print("You can travel", end=' ')
    if n == 1:
        print("(N)orth")
    if s == 1:
        print(("(S)outh"))
    if w == 1:
        print("(W)est")
    if e == 1:
        print("(E)ast")


position = 1  # player position

while True:
    if position == 1:
        legalmoves(1, 0, 0, 0)
    if position == 2:
        pass
    if position == 3:
        pass
    if position == 4:
        pass
    if position == 5:
        pass
    if position == 6:
        pass
    if position == 7:
        pass
    if position == 8:
        pass
    if position == 9:
        break
