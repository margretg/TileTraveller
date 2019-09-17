def movecharacter(position, userinput):
    """Takes our current position and the user input and returns our new position based on
    what the user input was"""
    if position == 1:
        if userinput == 'n':
            return position + 1

    if position == 2:
        if userinput == 'n':
            return position + 1
        elif userinput == 'e':
            return position + 3
        elif userinput == 's':
            return position - 1

    if position == 3:
        if userinput == 'e':
            return position + 3
        elif userinput == 's':
            return position - 1
    if position == 4:

        if userinput == 'n':
            return position + 1
    if position == 5:

        if userinput == 'w':
            return position - 3
        elif userinput == 's':
            return position - 1
    if position == 6:

        if userinput == 'w':
            return position - 3
        elif userinput == 'e':
            return position + 3
    if position == 7:

        if userinput == 'n':
            return position + 1
    if position == 8:
        if userinput == 'n':
            return position + 1
        elif userinput == 's':
            return position - 1
    if position == 9:

        if userinput == 'w':
            return position - 3
        elif userinput == 's':
            return position - 1


def legalmoves(n,s,w,e):
    """Takes input as binary numbers and prints if they are true, and if they are true adds them to a binary
    string and returns that string."""
    print("You can travel:", end=' ')
    return_string = '0000'
    if n == 1:
        print("(N)orth", end=' ')
        return_string = '1'+return_string[1:]
    if s == 1:
        print("(S)outh", end=' ')
        return_string = return_string[:1] + '1' + return_string[2:]
    if w == 1:
        print("(W)est", end=' ')
        return_string = return_string[:2] + '1' + return_string[3:]
    if e == 1:
        print("(E)ast", end=' ')
        return_string = return_string[:3] + '1'
    print()
    return return_string

#   main


position = 1  # player position
is_legal = ''  # string to check what routes are available
while True:
    # print legal positions(north, south, west, east)
    if position == 1:
        is_legal = legalmoves(1, 0, 0, 0)
    elif position == 2:
        is_legal = legalmoves(1, 1, 0, 1)
    elif position == 3:
        is_legal = legalmoves(0, 1, 0, 1)
    elif position == 4:
        is_legal = legalmoves(1, 0, 0, 0)
    elif position == 5:
        is_legal = legalmoves(0, 1, 1, 0)
    elif position == 6:
        is_legal = legalmoves(0, 0, 1, 1)
    elif position == 7:
        print("Victory!")
        break
    elif position == 8:
        is_legal = legalmoves(1, 1, 0, 0)
    elif position == 9:
        is_legal = legalmoves(0, 1, 1, 0)

    # Direction control's
    userinput = str(input("Direction:"))
    userinput = userinput.lower()

    # Checks our input and asks if our position for 'n' equals 1 in our string
    if userinput == 'n' and is_legal[0] == '1':
        position = movecharacter(position, userinput)
    elif userinput == 's' and is_legal[1] == '1':
        position = movecharacter(position, userinput)
    elif userinput == 'w' and is_legal[2] == '1':
        position = movecharacter(position, userinput)
    elif userinput == 'e' and is_legal[3] == '1':
        position = movecharacter(position, userinput)
    else:
        print("Not a valid direction!")

