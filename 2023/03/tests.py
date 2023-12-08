from textwrap import dedent

import pytest
from solution import parse, part_1, part_2


@pytest.fixture(scope="session")
def parsed_data() -> list[str]:
    data: str = dedent(
        """\
            467..114..
            ...*......
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598.."""
    )

    return parse(data)


def test_part_1(parsed_data: list[str]) -> None:
    assert part_1(parsed_data) == 4361


def test_part_2(parsed_data: list[str]) -> None:
    assert part_2(parsed_data) == 467835
