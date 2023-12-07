import re
from collections import namedtuple

Game = namedtuple("Game", "id colors")


def _parse_game_id(entry: str) -> int:
    """
    Extract the game ID from the game in string format.

    Args:
        entry (str): The game in string format.

    Returns:
        int: The game ID.
    """
    result: re.Match[str] | None = re.search(r"Game (?P<id>\d+): ", entry)
    if result:
        return int(result.group("id"))
    else:
        raise ValueError


def parse(input_data: str) -> list[Game]:
    """
    Parse the input data into a list of games.

    Args:
        input_data (str): The input data to parse.

    Returns:
        list[Game]: The list of games played.
    """
    games: list[Game] = []
    for entry in input_data.splitlines():
        id: int = _parse_game_id(entry)
        colors: dict[str, int] = {"red": 0, "green": 0, "blue": 0}
        for round in entry.split(": ")[1].split("; "):
            for grab in round.split(", "):
                result: re.Match[str] | None = re.search(
                    r"(?P<count>\d+) (?P<color>\w+)", grab
                )
                if result:
                    count: int = int(result.group("count"))
                    color: str = result.group("color")
                    if count > colors[color]:
                        colors[color] = count
        games.append(Game(id, colors))

    return games


def part_1(games: list[Game]) -> int:
    """
    Find the sum of the ID's of the games that would be possible with only
    12 red cubes, 13 green cubes and 14 blue cubes.

    Args:
        games (list[Game]): The list of games played.

    Returns:
        int: The sum of the ID's of the possible games.
    """
    total: int = 0
    for game in games:
        if (
            game.colors["red"] <= 12
            and game.colors["green"] <= 13
            and game.colors["blue"] <= 14
        ):
            total += game.id

    return total


def part_2(games: list[Game]) -> int:
    """
    Find the sum of the powers of the minimum cubes necessary to play each game.

    Args:
        games (list[Game]): The list of games played.

    Returns:
        int: The sum of the powers of the minimum cubes necessary.
    """
    total: int = 0
    for game in games:
        total += game.colors["red"] * game.colors["green"] * game.colors["blue"]

    return total
