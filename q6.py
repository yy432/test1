def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """

    length = len(lst)
    count = 0

    ##while loop exits when count < length becomes false.
    #this means that the list have been checked to the end
    while count < length:
        if (lst[count] < 0):
            print(lst[count]) 
            return lst[count]
        else:
            count +=1

    print("no negatives")
    return "no negatives"

find_first_negative([3, 5, -1, 7, -2, 8])
find_first_negative([2, 10, 7, 0])


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
