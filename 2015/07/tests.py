from textwrap import dedent

import pytest
from solution import compute, parse


@pytest.fixture
def parsed_data() -> dict[str, list[str]]:
    data: str = dedent(
        """
        123 -> x
        456 -> y
        x AND y -> d
        x OR y -> e
        x LSHIFT 2 -> f
        y RSHIFT 2 -> g
        NOT x -> h
        NOT y -> i
        """
    ).strip()

    return parse(data)


def test_parse(parsed_data: dict[str, list[str]]) -> None:
    expected: dict[str, list[str]] = {
        "x": ["123"],
        "y": ["456"],
        "d": ["x", "AND", "y"],
        "e": ["x", "OR", "y"],
        "f": ["x", "LSHIFT", "2"],
        "g": ["y", "RSHIFT", "2"],
        "h": ["NOT", "x"],
        "i": ["NOT", "y"],
    }

    assert parsed_data == expected


@pytest.mark.parametrize(
    "key,expected",
    [
        ("d", 72),
        ("e", 507),
        ("f", 492),
        ("g", 114),
        ("h", 65412),
        ("i", 65079),
        ("x", 123),
        ("y", 456),
    ],
)
def test_compute(parsed_data: dict[str, list[str]], key: str, expected: int) -> None:
    assert compute(parsed_data, key) == expected
