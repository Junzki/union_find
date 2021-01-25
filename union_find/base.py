# -*- coding:utf-8 -*-
from typing import Dict, Optional


class AbstractUF(object):

    def __init__(self):
        self.tree: Dict[int, int] = dict()
        self._count = 0

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def find(self, x: int) -> int:
        raise NotImplementedError("`find` method should be implemented.")

    def union(self, x: int, y: int):
        raise NotImplementedError("`union` method should be implemented.")

    def setdefault(self, x):
        self.tree.setdefault(x, x)
        self._count += 1

    @property
    def count(self):
        return self._count

    def __len__(self):
        return self.count

    def tabulate(self):
        rows = list()
        for v, b in self.tree.items():
            if v != b:
                b = self.find(b)  # Get root node

            rows.append((b, v))

        rows = list(sorted(rows, key=(lambda x: x[0])))
        return rows
