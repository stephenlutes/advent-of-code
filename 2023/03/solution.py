import math


def parse(input_data: str) -> list[str]:
    """
    Parse the input data.

    Args:
        input_data (str): The input data to parse.

    Returns:
        list[str]: The engine schematic as a list of strings.
    """
    return input_data.splitlines()


def _extract_part_number(line: str, start: int) -> int:
    """
    Extract the part number that is at the given position.

    Args:
        line (str): The line the part number is in.
        start (int): The position to start at.

    Returns:
        int: The part number.
    """
    # Find all digits before the starting position.
    value: str = line[start]
    i: int = start - 1
    while i >= 0 and line[i].isdigit():
        value = line[i] + value
        i -= 1

    # Find all digits after the starting position
    i = start + 1
    while i < len(line) and line[i].isdigit():
        value += line[i]
        i += 1

    return int(value)


def _find_part_numbers(schematic: list[str], i: int, j: int) -> list[int]:
    """
    Find the part numbers in the engine schematic.

    Args:
        schematic (list[str]): The engine schematic.
        i (int): The row the symbol is in.
        j (int): The column the symbol is in.

    Returns:
        list[int]: A list of the part numbers surrounding the symbol.
    """
    numbers: list[int] = []

    # Check for a number above and to the left of the symbol.
    if i > 0 and j > 0 and schematic[i - 1][j - 1].isdigit():
        numbers.append(_extract_part_number(schematic[i - 1], j - 1))

    # Check for a number above the symbol.
    if (
        i > 0
        and schematic[i - 1][j].isdigit()
        and not schematic[i - 1][j - 1].isdigit()
    ):
        numbers.append(_extract_part_number(schematic[i - 1], j))

    # Check for a number above and to the right of the symbol.
    if (
        i > 0
        and j < len(schematic[i])
        and schematic[i - 1][j + 1].isdigit()
        and not schematic[i - 1][j].isdigit()
    ):
        numbers.append(_extract_part_number(schematic[i - 1], j + 1))

    # Check for a number to the left of the symbol.
    if j > 0 and schematic[i][j - 1].isdigit():
        numbers.append(_extract_part_number(schematic[i], j - 1))

    # Check for a number to the right of the symbol.
    if j < len(schematic[i]) - 1 and schematic[i][j + 1].isdigit():
        numbers.append(_extract_part_number(schematic[i], j + 1))

    # Check for a number below and to the left of the symbol.
    if i < len(schematic) - 1 and j > 0 and schematic[i + 1][j - 1].isdigit():
        numbers.append(_extract_part_number(schematic[i + 1], j - 1))

    # Check for a number below the symbol.
    if (
        i < len(schematic) - 1
        and schematic[i + 1][j].isdigit()
        and not schematic[i + 1][j - 1].isdigit()
    ):
        numbers.append(_extract_part_number(schematic[i + 1], j))

    # Check for a number below and to the right of the symbol.
    if (
        i < len(schematic) - 1
        and schematic[i + 1][j + 1].isdigit()
        and not schematic[i + 1][j].isdigit()
    ):
        numbers.append(_extract_part_number(schematic[i + 1], j + 1))

    return numbers


def part_1(schematic: list[str]) -> int:
    """
    Find the sum of all the part numbers in the schematic.

    Args:
        schematic (list[str]): The engine schematic.

    Returns:
        int: The sum of all the part numbers.
    """
    numbers: list[int] = []
    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            if not schematic[i][j].isdigit() and schematic[i][j] != ".":
                numbers += _find_part_numbers(schematic, i, j)

    return sum(numbers)


def part_2(schematic: list[str]) -> int:
    """
    Find the sum of all the gear ratios in the schematic.

    Args:
        schematic (list[str]): The engine schematic.

    Returns:
        int: THe sum of all the gear ratios.
    """
    ratios: list[int] = []
    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            if schematic[i][j] == "*":
                numbers = _find_part_numbers(schematic, i, j)
                if len(numbers) == 2:
                    ratios.append(math.prod(numbers))

    return sum(ratios)
