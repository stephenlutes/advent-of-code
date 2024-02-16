from textwrap import dedent

import pytest
from solution import parse, part_1, part_2


@pytest.fixture
def parsed_data() -> list[list[int]]:
    data: str = dedent(
        """
        2x3x4
        1x1x10
        """
    ).strip()

    return parse(data)


def test_parse(parsed_data: list[list[int]]) -> None:
    expected: list[list[int]] = [[2, 3, 4], [1, 1, 10]]

    assert parsed_data == expected


def test_part_1(parsed_data: list[list[int]]) -> None:
    assert part_1(parsed_data) == 101


def test_part_2(parsed_data: list[list[int]]) -> None:
    assert part_2(parsed_data) == 48
