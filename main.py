message_1 = 'Enter an equation '
message_2 = 'Do you even know what numbers are? Stay focused!'
message_3 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
OPERATORS = tuple('+ - * /'.split())

while True:

    print(message_1)

    x, operator, y = input().strip().split()

    try:

        if '.' not in x:
            x = int(x)
        elif '.' in x:
            x = float(x)

    except ValueError:

        print(message_2)
        continue

    try:

        if '.' not in y:
            y = int(y)
        elif '.' in y:
            y = float(y)

    except ValueError:

        print(message_2)
        continue

    if operator not in OPERATORS:

        print(message_3)
        continue

    break
