msg_0 = 'Enter an equation '
msg_1 = 'Do you even know what numbers are? Stay focused!'
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
list_of_operands = ["+", "-", "*", "/"]

while True:

    print(msg_0)
    calc = input()
    x, oper, y = calc.split()

    try:
        x, y = int(x), int(y)
    except ValueError:
        print(msg_1)

    if oper not in list_of_operands:
        print(msg_2)
    else:
        quit()
