import pytest
from solution import _mine_coins


@pytest.mark.parametrize("data,expected", [("abcdef", 609043), ("pqrstuv", 1048970)])
def test__mine_coins(data: str, expected: int) -> None:
    assert _mine_coins(data, 5) == expected
