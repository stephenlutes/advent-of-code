import re


def parse(input_data: str) -> list[str]:
    """
    Parse the calibration data from the input.

    Args:
        input_data (str): The data read from the input.

    Returns:
        list[str]: The list of corrupted calibration values.
    """
    return input_data.splitlines()


def _interpret_number(value: str) -> str:
    """
    Interpret the given number. If it is a digit, return the value. If it is a
    word, return the digit version.

    Args:
        value (str): The value to interpret.

    Returns:
        str: The interpreted number as a digit.
    """
    word_values: dict[str, str] = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    if value.isdigit():
        return value
    else:
        return word_values[value]


def _find_calibration_values(calibrations: list[str], pattern: str) -> int:
    """
    Find the calibration values.

    Args:
        calibrations (list[str]): The corrupted calibration values.
        pattern (str): The pattern to use with regex to find the numbers.

    Returns:
        int: The sum of all the calibration values.
    """
    total: int = 0
    for entry in calibrations:
        digits: list[str] = re.findall(pattern, entry)
        value: str = _interpret_number(digits[0]) + _interpret_number(digits[-1])
        total += int(value)

    return total


def part_1(calibrations: list[str]) -> int:
    """
    Find the sum of all the calibration values.

    Args:
        calibrations (list[str]): The corrupted calibration values.

    Returns:
        int: The sum of the calibration values.
    """
    return _find_calibration_values(calibrations, r"\d")


def part_2(calibrations: list[str]) -> int:
    """
    Find the sum of all the calibration values.

    Args:
        calibrations (list[str]): The corrupted calibration values.

    Returns:
        int: The sum of the calibration values.
    """
    pattern: str = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

    return _find_calibration_values(calibrations, pattern)
