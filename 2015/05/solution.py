import re


def parse(data: str) -> list[str]:
    return data.strip().splitlines()


def part_1(strings: list[str]) -> int:
    return len(
        [
            s
            for s in strings
            if re.search(r"(.*[aeiou]){3,}", s)
            and re.search(r"([a-z])\1", s)
            and not re.search(r"ab|cd|pq|xy", s)
        ]
    )


def part_2(strings: list[str]) -> int:
    return len(
        [s for s in strings if re.search(r"(..).*\1", s) and re.search(r"(.).\1", s)]
    )
