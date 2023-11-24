import pytest
import exercise3


# 3
# Write a program for an extension of the program from the previous question to
# include the possibility to indicate also the amount of years to the age of pre-retirement
# (assumed at 60% at 60 and growing linearly with each year).

# Validity of age input is expected to be handled by IO
# When age is above retirement age, then desired result is 0

# different test cases inserted here: the diff test cases are defined as a list of tuples


@pytest.mark.parametrize('age, until_retirement, years_til_pre_ret, qualify_pre_ret, percentage', [
    (0, 65, 60, False, 0),
    (20, 45, 40, False, 0),
    (60, 5, 0, True, 60),
    (65, 0, 0, False, 100),
    (66, 0, 0, False, 100)
])
def test_pre_ret(age, until_retirement, years_til_pre_ret, qualify_pre_ret, percentage):
    assert exercise3.pre_retirement(age) == (until_retirement, years_til_pre_ret, qualify_pre_ret, percentage)
