def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    #test for cases when num or divisor is not number
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        print("not numeric")
        return "not numeric"

    ##if divisible, modulo will be 0, so check for x==0
    else:
        x = num%divisor
        if(x==0):
            print(True)
            return True
        else:
            print(False)
            return False

check_divisibility(-10, 2)
check_divisibility(-7, 3)


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
