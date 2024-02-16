def parse(data: str) -> str:
    return data.strip()


def next_house(direction: str, coord: tuple[int, int]) -> tuple[int, int]:
    return {
        "^": lambda c: (c[0], c[1] + 1),
        ">": lambda c: (c[0] + 1, c[1]),
        "v": lambda c: (c[0], c[1] - 1),
        "<": lambda c: (c[0] - 1, c[1]),
    }[direction](coord)


def deliver_presents(directions: str):
    visited: list[tuple[int, int]] = [(0, 0)]
    for step in directions:
        visited.append(next_house(step, visited[-1]))

    return visited


def part_1(directions: str) -> int:
    return len(set(deliver_presents(directions)))


def part_2(directions: str) -> int:
    return len(
        set(deliver_presents(directions[0::2]) + deliver_presents(directions[1::2]))
    )
