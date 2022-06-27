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


def is_one_digit(v):
    v = float(v)
    return v.is_integer() and (v > -10) and (v < 10)


def check(v1, v2, v3):
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"

    msg = ''

    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6

    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7

    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8

    if msg != '':
        msg = msg_9 + msg

    print(msg)


memory = 0
ask_for_saving = False

message_1 = 'Enter an equation '
message_2 = 'Do you even know what numbers are? Stay focused!'
message_3 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
message_4 = 'Yeah... division by zero. Smart move...'
message_5 = 'Do you want to store the result? (y / n):'
message_6 = 'Do you want to continue calculations? (y / n):'
message_10 = "Are you sure? It is only one digit! (y / n)"
message_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
message_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

stupid_answers = {10: message_10,
                  11: message_11,
                  12: message_12}

OPERATORS = tuple('+ - * /'.split())

while True:
    print(message_1)
    x, op, y = input().strip().split()

    if x == 'M':
        x = memory

    if y == 'M':
        y = memory

    if isinstance(x, str):

        try:

            if '.' not in x:
                x = int(x)
            elif '.' in x:
                x = float(x)

        except ValueError:
            print(message_2)
            continue

    if isinstance(y, str):

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

    check(x, y, op)

    try:

        result = calculator(x, y, op)

    except ZeroDivisionError:
        print(message_4)
        continue

    print(result)

    while True:

        if ask_for_saving:
            break

        else:
            print(message_5)
            answer = input().strip()

        if answer == 'y':
            # beginning of adjustments

            if not is_one_digit(result):
                memory = result
                break

            else:
                msg_index = 10

                while True:

                    output = stupid_answers[msg_index]

                    print(output)

                    user_input = input().strip()

                    if user_input == 'y':

                        if msg_index < 12:
                            msg_index += 1
                            continue

                        else:
                            print('End of while-loop')  # just for debugging
                            memory = result
                            ask_for_saving = True
                            break

                    if user_input == 'n':
                        # print('End of while-loop')  # just for debugging
                        memory = result
                        ask_for_saving = True
                        break

                    else:
                        continue
            # End of adjustments

        elif answer == 'n':
            break

        else:
            continue

    while True:
        print(message_6)
        answer = input().strip()

        if answer == 'y':
            ask_for_saving = False
            break

        elif answer == 'n':
            quit()

        else:
            continue
