# -*- coding:utf-8 -*-
from .base import AbstractUF, Dict


class WeightedQuickUnionUF(AbstractUF):

    def __init__(self):
        super().__init__()

        self.weight_index: Dict[int, int] = dict()

    def union(self, x: int, y: int):
        x_id = self.find(x)
        y_id = self.find(y)

        if x_id == y_id:
            return

        # y <- x
        if self.weight_index[y_id] > self.weight_index[x_id]:
            self.tree[y_id] = x_id
            self.weight_index[y_id] += self.weight_index[x_id]
        else:
            self.tree[y_id] = x_id
            self.weight_index[x_id] += self.weight_index[y_id]

        self._count -= 1

    def find(self, x: int) -> int:
        if x not in self.tree:
            self.setdefault(x)
            self.weight_index[x] = 1

        while x != self.tree[x]:
            x = self.tree[x]

        return x
