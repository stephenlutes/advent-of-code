import math
from heapq import nsmallest
from itertools import combinations


def parse(data: str) -> list[list[int]]:
    return [[int(x) for x in p.split("x")] for p in data.strip().splitlines()]


def part_1(presents: list[list[int]]):
    return sum(
        [
            2 * sum([math.prod(c) for c in combinations(p, 2)])
            + math.prod(nsmallest(2, p))
            for p in presents
        ]
    )


def part_2(presents: list[list[int]]):
    return sum([2 * sum(nsmallest(2, p)) + math.prod(p) for p in presents])
