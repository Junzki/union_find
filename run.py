# -*- coding:utf-8 -*-
import argparse
import tqdm
from union_find.files import load_data
from union_find.simple_uf import SimpleUF
from union_find.quick_union import QuickUnionUF
from union_find.weighted_quick_union import WeightedQuickUnionUF


_map = {
    'simple': SimpleUF,
    'quick-union': QuickUnionUF,
    'weighted': WeightedQuickUnionUF
}


parser = argparse.ArgumentParser()
parser.add_argument('command', help='Algorithm to execute.')
parser.add_argument('data_source', help='Data file.')


if __name__ == '__main__':
    args = parser.parse_args()

    cls = _map.get(args.command.lower())
    if not cls:
        raise ValueError(f'Command `{args.command}` not registered.')

    items = load_data(args.data_source)
    handle = cls()

    for x, y in tqdm.tqdm(items):
        handle.union(x, y)

    for base, value in handle.tabulate():
        print(f'[{base}] {value}')
