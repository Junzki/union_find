# -*- coding:utf-8 -*-
from .base import AbstractUF


class SimpleUF(AbstractUF):

    def union(self, x: int, y: int):
        x_id = self.find(x)
        y_id = self.find(y)

        if x_id == y_id:
            return

        # y <- x
        for k, v in self.tree.items():
            if v != y_id:
                continue

            self.tree[k] = x_id

        self._count -= 1

    def find(self, x: int) -> int:
        if x not in self.tree:
            self.tree.setdefault(x, x)

        return self.tree.get(x, x)
