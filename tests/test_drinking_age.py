import pytest
import exercise4

# 4
# Write a program for an extension of the program from the previous question to
# include the possibility to indicate also if they are legal drinking age.

# Validity of age input is expected to be handed by IO
# If age is below pre-retirement age, we show the ages left to go
# If it is above, we show the amount of retirement being received
# If age is 65 or above, the percentage stays at 100%
# The legal drinking age is assumed to be 18
# Validity of age input is expected to be handled by IO
# When age is above retirement age, then desired result is 0

# different test cases inserted here: the diff test cases are defined as a list of tuples


@pytest.mark.parametrize('age, until_retirement, years_til_pre_ret, qualify_pre_ret, percentage, if_legal', [
    (0, 65, 60, False, 0, False),
    (20, 45, 40, False, 0, True),
    (60, 5, 0, True, 60, True),
    (65, 0, 0, False, 100, True),
    (66, 0, 0, False, 100, True),
    (18, 47, 42, False, 0, True)
])
def test_drinking_age(age, until_retirement, years_til_pre_ret, qualify_pre_ret, percentage, if_legal):
    assert exercise4.pre_retirement_and_legal(age) == (until_retirement, years_til_pre_ret, qualify_pre_ret, percentage,
                                                       if_legal)
