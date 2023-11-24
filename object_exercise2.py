class AgeAnalyzer:
    def __init__(self, age):
        self.age = age
        self.voting_age = 18
        self.retirement_age = 65

    def can_vote(self):
        return self.age >= self.voting_age

    def until_retire(self):
        return max(0, self.retirement_age - self.age)


# This class, AgeAnalyzer, takes an age as an argument when instantiated. It has two methods, can_vote and
# until_retire, which correspond to your previous functions.
