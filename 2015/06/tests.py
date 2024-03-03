from textwrap import dedent

import pytest
from solution import Command, parse, part_1, part_2


@pytest.fixture
def parsed_data() -> list[Command]:
    data: str = dedent(
        """
        turn on 0,0 through 999,999
        toggle 0,0 through 999,0
        turn off 499,499 through 500,500
        """
    ).strip()

    return parse(data)


def test_parse(parsed_data: list[Command]) -> None:
    expected: list[Command] = [
        Command("turn on", slice(0, 1000), slice(0, 1000)),
        Command("toggle", slice(0, 1000), slice(0, 1)),
        Command("turn off", slice(499, 501), slice(499, 501)),
    ]

    assert parsed_data == expected


def test_part_1(parsed_data: list[Command]) -> None:
    assert part_1(parsed_data) == 998996


def test_part_2(parsed_data: list[Command]) -> None:
    assert part_2(parsed_data) == 1001996
