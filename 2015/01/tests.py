import pytest
from solution import part_1, part_2


@pytest.mark.parametrize(
    "data,expected",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_part_1(data: str, expected: int) -> None:
    assert part_1(data) == expected


@pytest.mark.parametrize("data,expected", [(")", 1), ("()())", 5)])
def test_part_2(data: str, expected: int) -> None:
    assert part_2(data) == expected
