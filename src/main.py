def factorial(n):
    """
    Calculate the factorial of a number.
    :param n: The number to calculate the factorial of.
    :return: The factorial of the number.
    """
    if n < 0:
        raise ValueError("Number must be non-negative.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def get_user_input():
    """
    Get user input from the command line.
    :return: The user input as an integer.
    """
    user_input = input("Enter a number: ")
    return int(user_input)

def print_factorial(n):
    """
    Print the factorial of a number.
    :param n: The number to calculate the factorial of.
    """
    print("The factorial of {} is: {}".format(n, factorial(n)))

if __name__ == "__main__":
    try:
        n = get_user_input()
        print_factorial(n)
    except ValueError as e:
        print(e)