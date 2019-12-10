import pytest

from day04 import check_larger_group_matching


@pytest.mark.parametrize("number, expected_result", [
    (112233, True),
    (123444, False),
    (111122, True),
])
def test_group_matching(number, expected_result):
    digits = list(map(int, str(number)))
    assert check_larger_group_matching(digits) == expected_result
