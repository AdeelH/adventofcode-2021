from typing import List
from os import PathLike
import numpy as np


def solve(params: dict) -> int:
    map: np.array = params['map']
    padded = np.pad(map, 1, constant_values=100)
    lt_upper = map < padded[2:, 1:-1]
    lt_lower = map < padded[:-2, 1:-1]
    lt_left = map < padded[1:-1, 2:]
    lt_right = map < padded[1:-1, :-2]
    mask = lt_upper & lt_lower & lt_left & lt_right
    out = (map[mask] + 1).sum()
    return out


def parse(lines: list) -> dict:
    map = np.array([[int(c) for c in line] for line in lines])
    out = {'map': map}
    return out


def read(inputs_path: PathLike) -> List[str]:
    with open(inputs_path, 'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if len(l) > 0]
    return lines


if __name__ == '__main__':
    inp = read('./inputs/17.txt')
    params = parse(inp)
    ans = solve(params)
    print(ans)

# print(
#     solve(
#         parse("""2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""".split('\n'))))
