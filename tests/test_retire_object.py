import pytest
from object_exercise2 import AgeAnalyzer  # Replace 'your_module_name' with the actual name of your module

@pytest.mark.parametrize('age, can_vote', [
    (18, True),
    (12, False),
    (0, False)
])
def test_can_vote(age, can_vote):
    age_analyzer = AgeAnalyzer(age)
    assert age_analyzer.can_vote() == can_vote

@pytest.mark.parametrize('age, until_retirement', [
    (20, 45),
    (0, 65),
    (67, 0)
])
def test_until_retire(age, until_retirement):
    age_analyzer = AgeAnalyzer(age)
    assert age_analyzer.until_retire() == until_retirement
