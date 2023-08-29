from art import logo

print(logo)


def calculator():
    '''A calculator function to perform calculations'''

    chain = False
    result = 0
    loop_1 = 0
    operations = {'+': add,
                  '-': subtract,
                  '*': multiply,
                  '/': divide}
    while True:
        if chain == True:
            num_1 = result
        else:
            num_1 = float(input("What's the first number?: "))
        if loop_1 == 0:
            for key in operations:
                print(key)
        operation = input("Pick an operation from the above list: ")
        num_2 = float(input("What's the next number?: "))
        function = operations[operation]
        result = function(num_1, num_2)
        print(num_1, operation, num_2, '=', result)
        reuse_answer = input(
            f"Type 'y' to continue calculating with {result:.1f}, type 'n' to restart, type 'exit' to exit: ")
        if reuse_answer == 'y':
            chain = True
        elif reuse_answer == 'exit':
            break
        else:
            chain == False
        loop_1 += 1


def add(n1, n2):
    return (n1 + n2)


def subtract(n1, n2):
    return (n1 - n2)


def multiply(n1, n2):
    return (n1 * n2)


def divide(n1, n2):
    return (n1 / n2)


calculator()