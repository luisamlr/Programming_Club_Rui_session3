# 7
# Given the list [0,1,2,3,4,5,6,7,8], modify by reference the elements at given
# positions (e.g. 0, 3, 5, 6) to be equal to the element in the next position (result:
# [1,1,2,4,4,6,7,7,8]). Write down unit tests.


def modify_list_by_reference(alist, positions):
    for i in positions:
        # if i < len(alist) - 1:

        alist[i] = alist[i + 1]
    return alist


original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
positions_to_modify = [0, 3, 5, 6]
