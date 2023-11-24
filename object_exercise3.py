class UserAgeAnalyzerExtended:
    def __init__(self, age):
        self.age = age
        self.retirement_age = 65
        self.pre_retirement_age = 60

    def can_vote(self):
        return self.age >= 18

    def pre_retirement_info(self):
        if self.age < self.pre_retirement_age:
            until_retirement = self.retirement_age - self.age
            years_til_pre_ret = self.pre_retirement_age - self.age

            qualify_pre_ret = False
            percentage = 0
        elif self.age < self.retirement_age:
            until_retirement = self.retirement_age - self.age
            years_til_pre_ret = 0
            qualify_pre_ret = True
            i = self.age - self.pre_retirement_age
            percentage = self.pre_retirement_age + (i * ((100 - self.pre_retirement_age) / 6))
        else:
            until_retirement = 0
            years_til_pre_ret = 0
            qualify_pre_ret = False
            percentage = 100

        return until_retirement, years_til_pre_ret, qualify_pre_ret, percentage
