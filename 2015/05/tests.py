from textwrap import dedent

from solution import parse, part_1, part_2


def test_part_1() -> None:
    data: str = dedent(
        """
        ugknbfddgicrmopn
        aaa
        jchzalrnumimnmhp
        haegwjzuvuyypxyu
        dvszwmarrgswjxmb
        """
    )
    parsed_data: list[str] = parse(data)

    assert part_1(parsed_data) == 2


def test_part_2() -> None:
    data: str = dedent(
        """
        qjhvhtzxzqqjkmpb
        xxyxx
        uurcxstgmygtbstg
        ieodomkazucvgmuy
        """
    )
    parsed_data: list[str] = parse(data)

    assert part_2(parsed_data) == 2
