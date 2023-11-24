#8
# Linear Search is a simple algorithm that you can use to search for an item in a list
# or (list of) string. It can be expressed in pseudo-code as:

# element = 0
# found = False
# lengthOfList = len(listOfItems)
# WHILE (found == False) and (element < max) DO
# IF searchItem == listOfItems[element] THEN
# found = True
# ...other statements...
# ELSE
# element = element + 1
# END IF
# END WHILE

# Implement this pseudo-code. Implement only the case that the string is not a list
# after the other cases pass your tests.

def linear_search(search_item, list_of_items):
    element = 0
    found = False
    length_of_list = len(list_of_items)

    while not found and element < length_of_list:
        if search_item == list_of_items[element]:
            found = True
            # Other statements can be added here as needed
        else:
            element += 1



# Example usage:
my_list = "examplestring"
linear_search("p", my_list)
linear_search("z", my_list)
