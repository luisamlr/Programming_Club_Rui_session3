import pytest
import exercise9

# 9
# Using a list comprehension, create a new list called "newlist" out of the list "numbers",
# which contains only the positive numbers from the list, as integers.

@pytest.mark.parametrize('numbers, positive_numbers', [
    ([1, 2, 3, 4], [1, 3, 3, 4]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 3, 5, 6], [1, 1, 2, 4, 4, 6, 7, 7, 8]),
    ([10, 20, 30, 40, 50], [0, 2, 4], [11, 20, 31, 40, 51]),
    ([], [], [])
])
def test_modify_list(alist, positions, new):
    assert exercise7.modify_list_by_reference(alist, positions, new) == new


def test_pre_ret(age, until_retirement, years_til_pre_ret, qualify_pre_ret, percentage):
    assert exercise3.pre_retirement(age) == (until_retirement, years_til_pre_ret, qualify_pre_ret, percentage)
