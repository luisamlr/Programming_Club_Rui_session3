import pytest
import exercise2

# 2
# Write a program that asks the users how old they are and returns an answer indicating
# if the users are old enough to vote and how many years are there until they can retire
# (assume at age 65).

# Validity of age input is expected to be handled by IO
# Voting age is assumed to be 18

# different test cases inserted here: the diff test cases are defined as a list of tuples


@pytest.mark.parametrize('age, can_vote', [
    (18, True),
    (12, False),
    (0, False)
])
def test_if_vote(age, can_vote):
    assert exercise2.if_vote(age) == can_vote
