import pytest
from solution import part_1, part_2


@pytest.mark.parametrize("data,expected", [(">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2)])
def test_part_1(data: str, expected: int) -> None:
    assert part_1(data) == expected


@pytest.mark.parametrize("data,expected", [("^v", 3), ("^>v<", 3), ("^v^v^v^v^v", 11)])
def test_part_2(data: str, expected: int) -> None:
    assert part_2(data) == expected
