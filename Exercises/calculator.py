add = lambda n1, n2: n1+n2

subtract = lambda n1, n2: n1-n2

multiply = lambda n1, n2: n1*n2

divide = lambda n1, n2: n1/n2


def calculator():
    num1 = float(input("What's the first number? "))

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    for operator in operations:
        print(operator)
    operation_symbol = input("Pick an operation from the line above: ")

    num2 = float(input("What's the second number? "))

    operation_function = operations[operation_symbol]
    f_answer = operation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {f_answer}")
    while True:
        out = input(f"Type 'y' to continue calculating with {f_answer}, or type 'n' to exit: ")
        if out.lower() == 'n':
            calculator()
        elif out.lower() == 'y':
            num3 = float(input("What's the next number? "))
            operation_symbol = input("Pick another operation: ")
            operation_function = operations[operation_symbol]
            answer = operation_function(f_answer, num3)
            print(f"{f_answer} {operation_symbol} {num3} = {answer}")
            f_answer = answer
        else:
            return "Invalid output"


calculator()
