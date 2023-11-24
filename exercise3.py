# 3
# Write a program for an extension of the program from the previous question to
# include the possibility to indicate also the amount of years to the age of pre-retirement
# (assumed at 60% at 60 and growing linearly with each year).

# Validity of age input is expected to be handed by IO
# If age is below pre-retirement age, we show the ages left to go
# If it is above, we show the amount of retirement being received
# If age is 65 or above, the percentage stays at 100%

def if_vote(age):
    voting_age = 18

    if age >= voting_age:
        can_vote = True
    else:
        can_vote = False
    return can_vote


def pre_retirement(age):
    retirement_age = 65
    pre_ret = 60

    if pre_ret <= age < retirement_age:
        qualify_pre_ret = True
        until_retirement = retirement_age - age
        years_til_pre_ret = 0

        i = age - pre_ret # calculating the years after 60
        percentage = 60 + (i * ((100-60)/6))  # adding 10% for each of the 6 years after 60

    elif pre_ret > age:  # < retirement_age:
        until_retirement = retirement_age - age
        years_til_pre_ret = pre_ret - age
        qualify_pre_ret = False
        percentage = 0
    else:  # if age > retirement_age
        until_retirement = 0
        years_til_pre_ret = 0
        qualify_pre_ret = False
        percentage = 100
    return until_retirement, years_til_pre_ret, qualify_pre_ret, percentage
