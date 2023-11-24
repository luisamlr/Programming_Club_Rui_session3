# 7
# Given the list [0,1,2,3,4,5,6,7,8], modify by reference the elements at given
# positions (e.g. 0, 3, 5, 6) to be equal to the element in the next position (result:
# [1,1,2,4,4,6,7,7,8]). Write down unit tests.

import pytest
import exercise7

# Unit tests using pytest

@pytest.mark.parametrize('alist, positions, new', [
    ([1, 2, 3, 4], [1], [1, 3, 3, 4]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 3, 5, 6], [1, 1, 2, 4, 4, 6, 7, 7, 8]),
    ([10, 20, 30, 40, 50], [0, 2, 4], [11, 20, 31, 40, 51]),
    ([], [], [])
])
def test_modify_list(alist, positions, new):
    assert exercise7.modify_list_by_reference(alist, positions, new) == new


# if __name__ == "__main__":
#     pytest.main()

# In this example, the modify_elements_by_reference function takes a list lst and a list of positions to modify.
# The function iterates over the specified positions and updates the elements at those positions to be equal to the
# element in the next position.
# The test_modify_elements_by_reference function defines several test cases using pytest assertions to ensure that
# the modification is correct for different scenarios.
# To run the tests, save this code in a file (e.g., test_modify_list.py) and run it using the following command:
# pytest test_modify_list.py
