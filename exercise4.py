# 4
# Write a program for an extension of the program from the previous question to
# include the possibility to indicate also if they are legal drinking age.

# Validity of age input is expected to be handed by IO
# If age is below pre-retirement age, we show the ages left to go
# If it is above, we show the amount of retirement being received
# If age is 65 or above, the percentage stays at 100%
# The legal drinking age is assumed to be 18

def if_vote(age):
    voting_age = 18

    if age >= voting_age:
        can_vote = True
    else:
        can_vote = False
    return can_vote


def pre_retirement_and_legal(age):
    retirement_age = 65
    pre_ret = 60
    legal_age = 18

    if pre_ret <= age < retirement_age:
        qualify_pre_ret = True
        until_retirement = retirement_age - age
        years_til_pre_ret = 0

        i = age - pre_ret  # calculating the years after 60
        percentage = 60 + (i * ((100-60)/6))  # adding 10% for each of the 6 years after 60
        # Rui does: pre_ret + (age - pre_ret) * 8 # but unsure why

        if_legal = True
    elif age < pre_ret:  # < retirement_age:
        qualify_pre_ret = False
        until_retirement = retirement_age - age
        years_til_pre_ret = pre_ret - age
        percentage = 0
        if age >= legal_age:
            if_legal = True
        else:
            if_legal = False
    else:  # if age > retirement_age
        qualify_pre_ret = False
        until_retirement = 0
        years_til_pre_ret = 0
        percentage = 100
        if_legal = True
    return until_retirement, years_til_pre_ret, qualify_pre_ret, percentage, if_legal
