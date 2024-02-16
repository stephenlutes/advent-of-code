from collections import Counter


def parse(data: str) -> str:
    return data.strip()


def part_1(instructions: str) -> int:
    counts: Counter = Counter(instructions)

    return counts["("] - counts[")"]


def part_2(instructions: str) -> int:
    floor: int = 0
    index: int = 0
    directions: dict[str, int] = {"(": 1, ")": -1}
    while floor != -1:
        floor += directions[instructions[index]]
        index += 1

    return index
