import pytest
from object_exercise3 import UserAgeAnalyzerExtended  # Replace 'your_module' with your actual module name

@pytest.mark.parametrize('age, until_retirement, years_til_pre_ret, qualify_pre_ret, percentage', [
    (0, 65, 60, False, 0),
    (20, 45, 40, False, 0),
    (60, 5, 0, True, 60),
    (65, 0, 0, False, 100),
    (66, 0, 0, False, 100)
])
def test_extended_pre_retirement_info(age, until_retirement, years_til_pre_ret, qualify_pre_ret, percentage):
    user_analyzer = UserAgeAnalyzerExtended(age)
    assert user_analyzer.pre_retirement_info() == (until_retirement, years_til_pre_ret, qualify_pre_ret, percentage)
