# 6
# Define a multiply_by2 function, that takes one parameter and returns the value
# multiplied by two, using pass by value and pass by reference. Hint: Python does not
# allow pass by reference, but we can make use of a list.

# chatgpt comment:
# In Python, the concept of pass-by-value and pass-by-reference can be a bit nuanced.
# In Python, when you pass a mutable object like a list, changes made to the object within
# the function are reflected outside the function. However, Python itself is strictly pass-by-object-reference.

# Below we look at the multiply_by2 function, using first pass by value and secondly pass by reference, using a list.


def multiply_by_2_pass_by_value(number):
    # Pass by value (using an immutable object like an integer)
    return number * 2


def multiply_by_2_pass_by_reference(a_list):
    # Pass by reference (using a mutable object like a list)
    a_list[0] *= 2


# we could add an example now
# the example goes into name == main; because a lot of times you want to import and if you send the file to somebody
# else, they only want the functions to use them
