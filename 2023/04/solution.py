import re
from collections import namedtuple
from functools import cache

Card = namedtuple("Card", "winning numbers")


def parse(input_data: str) -> dict[str, Card]:
    """
    Parse the input data into a list of cards.

    Args:
        input_data (str): The input data to parse.

    Returns:
        dict[str, Card]: A dictionary where the key is the card number.
    """
    cards: dict[str, Card] = {}
    for line in input_data.splitlines():
        id: str = re.findall(r"Card *(\d+)", line)[0]
        winning, numbers = line.split(": ")[1].split(" | ")
        pattern: str = r"(\d+)"
        cards[id] = Card(re.findall(pattern, winning), re.findall(pattern, numbers))

    return cards


def part_1(cards: dict[str, Card]) -> int:
    """
    Find the total points the cards are worth.

    Args:
        cards (dict[str, Card]): The scratch cards.

    Returns:
        int: The total points the cards are worth
    """
    points: int = 0
    for _, card in cards.items():
        count: int = len([n for n in card.numbers if n in card.winning])
        if count > 0:
            points += 2 ** (count - 1)

    return points


def part_2(cards: dict[str, Card]) -> int:
    """
    Find the number of cards and copies of cards you have won.

    Args:
        cards (dict[str, Card]): A dictionary of the scratch cards.

    Returns:
        int: The number of cards and copies of card you have won.
    """

    @cache
    def _num_copies(id: str) -> int:
        """
        Find the number of copies that the card gives.

        Args:
            id (str): The card number.

        Returns:
            int: The number of copies from winning the card.
        """
        num_winning: int = len([n for n in cards[id].numbers if n in cards[id].winning])
        if num_winning > 0:
            count: int = num_winning
            copies: list[str] = [
                str(x) for x in range(int(id) + 1, int(id) + num_winning + 1)
            ]
            for copy in copies:
                count += _num_copies(copy)

            return count
        else:
            return 0

    count: int = 0
    for id in cards:
        count += _num_copies(id)

    return count + len(cards.keys())
