# part of the object-oriented programming series
# 2
# Write a program, using object-oriented programming, that asks the users how old they are and returns an answer
# indicating if the users are old enough to vote and how many years are there until they can retire (assume at age 65).


class AgeAnalyzer:
    def __init__(self, age):
        self.age = age
        self.voting_age = 18
        self.retirement_age = 65

# instead of the above you can also indicate use type-hint the output type (this is usually common of more declarative
# languages)
# Python users decided they were creating such complicated programs, they wanted to indicate the output first
# but this is not at runtime (when you actually run the code), but only at programming time,
# like while creating the code:
#    def __init__(self, age: int = None) -> None:
#        self.age = age
# this way we only "update" the indicated variables as "exit code", but then in __name__ you can trigger all of them

    def can_vote(self):
        return self.age >= self.voting_age

    def until_retire(self):
        return max(0, self.retirement_age - self.age)


# This class, AgeAnalyzer, takes an age as an argument when instantiated. It has two methods, can_vote and
# until_retire, which correspond to your previous functions.

# we could add an example now
# the example goes into name == main; because a lot of times you want to import and if you send the file to somebody
# else, they only want the functions to use them
# like mentioned before, this indicates an example, so it can be called by other people
