import pytest
from object_exercise4 import UserAgeAnalyzerExtended  # Replace 'your_module' with your actual module name

@pytest.mark.parametrize('age, until_retirement, years_til_pre_ret, qualify_pre_ret, percentage, if_legal', [
    (0, 65, 60, False, 0, False),
    (20, 45, 40, False, 0, True),
    (60, 5, 0, True, 60, True),
    (65, 0, 0, False, 100, True),
    (66, 0, 0, False, 100, True),
    (18, 47, 42, False, 0, True)
])
def test_extended_pre_retirement_and_legal(age, until_retirement, years_til_pre_ret, qualify_pre_ret, percentage,
                                           if_legal):
    user_analyzer = UserAgeAnalyzerExtended(age)
    assert user_analyzer.pre_retirement_and_legal() == (until_retirement, years_til_pre_ret, qualify_pre_ret,
                                                        percentage, if_legal)