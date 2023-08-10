#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function


# TODO: function that takes arguments


# TODO: function that returns a value


# TODO: function with default value for an argument

# * means we can pass in variable number of args

# value = 10

def multi_add(value, *args):
    result = value
    for x in args:
        result = result + x
    return result


print(multi_add(10, 2, 2, 2, 2, 2))
