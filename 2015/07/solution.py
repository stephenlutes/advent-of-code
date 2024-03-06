from copy import deepcopy
from functools import cache


def parse(data: str) -> dict[str, list[str]]:
    wires: dict[str, list[str]] = {}
    for line in data.strip().splitlines():
        value, key = line.split(" -> ")
        wires[key] = value.split(" ")

    return wires


def compute(wires: dict[str, list[str]], key: str) -> int:
    @cache
    def get_value(key: str) -> int:
        if key.isdigit():
            return int(key)
        elif len(wires[key]) == 1 and wires[key][0].isdigit():
            return int(wires[key][0])
        elif len(wires[key]) == 1:
            return int(get_value(wires[key][0]))
        elif "AND" in wires[key]:
            return get_value(wires[key][0]) & get_value(wires[key][2])
        elif "OR" in wires[key]:
            return get_value(wires[key][0]) | get_value(wires[key][2])
        elif "LSHIFT" in wires[key]:
            return get_value(wires[key][0]) << get_value(wires[key][2])
        elif "RSHIFT" in wires[key]:
            return get_value(wires[key][0]) >> get_value(wires[key][2])
        else:
            return ~int(get_value(wires[key][1])) & 0xFFFF

    get_value.cache_clear()

    return get_value(key)


def part_1(wires: dict[str, list[str]]) -> int:
    return compute(wires, "a")


def part_2(wires: dict[str, list[str]]) -> int:
    circuit: dict[str, list[str]] = deepcopy(wires)
    circuit["b"] = [str(compute(wires, "a"))]

    return compute(circuit, "a")
