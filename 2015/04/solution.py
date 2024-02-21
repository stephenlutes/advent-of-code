from hashlib import md5


def parse(data: str) -> str:
    return data.strip()


def _mine_coins(key: str, num_zeros: int) -> int:
    counter: int = -1
    coin: str = ""
    while coin[:num_zeros] != "0" * num_zeros:
        counter += 1
        coin = md5(bytes(f"{key}{counter}", "utf-8")).hexdigest()

    return counter


def part_1(key: str) -> int:
    return _mine_coins(key, 5)


def part_2(key: str) -> int:
    return _mine_coins(key, 6)
