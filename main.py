
def calculator(number_one, number_two, operator):
    if operator == '+':
        return float(number_one + number_two)
    elif operator == '-':
        return float(number_one - number_two)
    elif operator == '*':
        return float(number_one * number_two)
    elif operator == '/' and number_two != 0:
        return float(number_one / number_two)
    elif operator == '/' and number_two == 0:
        raise ZeroDivisionError


message_1 = 'Enter an equation '
message_2 = 'Do you even know what numbers are? Stay focused!'
message_3 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
message_4 = 'Yeah... division by zero. Smart move...'
OPERATORS = tuple('+ - * /'.split())

while True:

    print(message_1)

    x, op, y = input().strip().split()

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

    if op not in OPERATORS:
        print(message_3)
        continue

    try:

        result = calculator(x, y, op)

    except ZeroDivisionError:

        print(message_4)
        continue

    print(result)
    break
