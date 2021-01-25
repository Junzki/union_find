# -*- coding:utf-8 -*-
from .base import AbstractUF


class QuickUnionUF(AbstractUF):

    def union(self, x: int, y: int):
        x_id = self.find(x)
        y_id = self.find(y)

        if x_id == y_id:
            return

        # y <- x
        self.tree[y_id] = x_id

        self._count -= 1

    def find(self, x: int) -> int:
        if x not in self.tree:
            self.setdefault(x)

        while x != self.tree[x]:
            x = self.tree[x]

        return x
