def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    ##check for not a str
    if not isinstance(s, str):
        return "is not string"

    ##start at end, stop at beginning, -1 to move backwards
    else:
        print(s[::-1])
        return s[::-1]


string_reverse("Hello World")
string_reverse("Python")


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
