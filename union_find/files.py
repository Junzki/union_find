# -*- coding:utf-8 -*-
from typing import Tuple, List

SEPARATOR = ' '


def get_number(src: str) -> int:
    src = src.strip()
    return int(src)


def load_data(path: str) -> List[Tuple[int, int]]:
    with open(path) as f:
        rows = f.readlines()

    rows = rows[1:]

    results = list()
    for r in rows[1:]:
        x, y = r.split(SEPARATOR)
        x = get_number(x)
        y = get_number(y)
        results.append((x, y))

    return results
