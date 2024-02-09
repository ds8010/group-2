a_range=range(0,10)

def forvalues(r):
    """
    Prints all the values in the given range on a single line using a for loop.
    activity 4.3.5 which requires us to use a for loop in order to produce the same
    as the older functions and print them on single lines.
    """
    for value in r:
        print(value, end=" ")

forvalues(a_range)