import pytest
import exercise2

# 2
# Write a program that asks the users how old they are and returns an answer indicating
# if the users are old enough to vote and how many years are there until they can retire
# (assume at age 65).

# Validity of age input is expected to be handled by IO
# When age is above retirement age, then desired result is 0

# different test cases inserted here: the diff test cases are defined as a list of tuples


@pytest.mark.parametrize('age, until_retirement', [
    (20, 45),
    (0, 65),
    (67, 0)
])
def test_until_retire(age, until_retirement):
    assert exercise2.until_retire(age) == until_retirement
