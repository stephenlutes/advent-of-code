import re
from collections import namedtuple

import numpy as np

Command = namedtuple("Command", ["action", "start", "end"])


def parse(data: str) -> list[Command]:
    commands: list[Command] = []
    for line in data.strip().splitlines():
        match: re.Match | None = re.match(
            r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)", line
        )
        if match is not None:
            result: tuple = match.groups()
            commands.append(
                Command(
                    result[0],
                    slice(int(result[1]), int(result[3]) + 1),
                    slice(int(result[2]), int(result[4]) + 1),
                )
            )

    return commands


def part_1(commands: list[Command]) -> int:
    lights: np.ndarray = np.zeros((1000, 1000))
    for cmd in commands:
        if cmd.action == "turn on":
            lights[cmd.start, cmd.end] = 1
        elif cmd.action == "turn off":
            lights[cmd.start, cmd.end] = 0
        else:
            lights[cmd.start, cmd.end] = np.where(lights[cmd.start, cmd.end] == 1, 0, 1)

    return int(sum(sum(lights)))


def part_2(commands: list[Command]) -> int:
    lights: np.ndarray = np.zeros((1000, 1000))
    for cmd in commands:
        if cmd.action == "turn on":
            lights[cmd.start, cmd.end] += 1
        elif cmd.action == "turn off":
            lights[cmd.start, cmd.end] = np.where(
                lights[cmd.start, cmd.end] > 1, lights[cmd.start, cmd.end] - 1, 0
            )
        else:
            lights[cmd.start, cmd.end] += 2

    return int(sum(sum(lights)))
