# 9
# Using a list comprehension, create a new list called "newlist" out of the list "numbers",
# which contains only the positive numbers from the list, as integers.

numbers = [1.5, -2.3, 3.8, -4.2, 5.0, -6.1, 7.4]

newlist = [int(num) for num in numbers if num > 0]

print(newlist)

# In this example, the list comprehension [x for x in numbers if x > 0] iterates through each element x in the
# numbers list and includes it in the new list newlist only if it's greater than 0. The resulting newlist will
# contain only the positive numbers from the original list.
# Adjust the numbers list to your specific case, and this list comprehension will filter out the positive numbers for you.

# Output will be:
# [1, 3, 5, 7]