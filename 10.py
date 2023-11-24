# 10
# Write a program which will find all numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included), using a list comprehension.

# Using list comprehension to find numbers meeting the criteria
result_list = [num for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]

# Print the result
print(result)

# Print the result
print(result_list)

# This program uses the range function to generate numbers from 2000 to 3200 (both included). The list
# comprehension filters out the numbers that are divisible by 7 (num % 7 == 0) and not multiples of 5 (num % 5 != 0).
# When you run this code, the output will be a list of numbers that meet the specified criteria.