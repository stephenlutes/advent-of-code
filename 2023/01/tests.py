from textwrap import dedent

from solution import parse, part_1, part_2


def test_part_1() -> None:
    data: str = dedent(
        """\
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet"""
    )
    parsed_data: list[str] = parse(data)

    assert part_1(parsed_data) == 142


def test_part_2() -> None:
    data: str = dedent(
        """\
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen"""
    )
    parsed_data: list[str] = parse(data)

    assert part_2(parsed_data) == 281
