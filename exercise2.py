# 2
# Write a program that asks the users how old they are and returns an answer indicating
# if the users are old enough to vote and how many years are there until they can retire
# (assume at age 65).

def if_vote(age):
    voting_age = 18

    if age >= voting_age:
        can_vote = True
    else:
        can_vote = False
    return can_vote


def until_retire(age):
    retirement_age = 65

    if age <= retirement_age:
        until_retirement = retirement_age - age
    else:
        until_retirement = 0
    return until_retirement
