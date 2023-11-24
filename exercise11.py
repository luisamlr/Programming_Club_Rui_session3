# 11
# With a given integral number n, write a program to generate a dictionary that
# contains (i, i * i) such that is an integral number between 1 and n (both included)
# and then the program should print the dictionary. An example of a unit test is: If 8
# is provided, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def generate_sq_dict(n):
    # Using a dictionary comprehension to generate the (i, i * i) pairs
    square_dict = {i: i * i for i in range(1, n + 1)}
    return square_dict

    # Example usage with n = 8

n = 8
result_dict = generate_square_dict(n)
print(result_dict)

# In this program:
#
# generate_square_dictionary is a function that takes an integral number n as input and returns a dictionary containing
# (i, i * i) for each i from 1 to n.
# The example usage sets input_number to 8 and calls the generate_square_dictionary function.
# The resulting dictionary is then printed.
# When you run this code with input_number = 8, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Feel free to modify the input_number variable to test the program with different values of n.
