from os import PathLike
from typing import Iterable, List, Tuple
import numpy as np
from re import split
from collections import Counter
from itertools import chain


def solve(params: dict) -> int:
    segments: np.array = params['segments']
    points = chain.from_iterable(points_hit(*s) for s in segments)
    counts = Counter(points)
    overlaps = len([k for k, v in counts.items() if v > 1])
    return overlaps


def points_hit(x0: int, y0: int, x1: int,
               y1: int) -> Iterable[Tuple[int, int]]:
    dx, dy = x1 - x0, y1 - y0
    if dx == 0 and dy == 0:
        return [(x0, y0)]
    if dx == 0:
        ystep = 1 if dy >= 0 else -1
        ys = range(y0, y1 + ystep, ystep)
        xs = [x0] * len(ys)
    elif dy == 0:
        xstep = 1 if dx >= 0 else -1
        xs = range(x0, x1 + xstep, xstep)
        ys = [y0] * len(xs)
    else:
        ystep = 1 if dy >= 0 else -1
        xstep = 1 if dx >= 0 else -1
        ys = range(y0, y1 + ystep, ystep)
        xs = range(x0, x1 + xstep, xstep)
    return zip(xs, ys)


def parse(lines: list) -> dict:
    segments = np.array([[int(s) for s in split(',\s*|\s*->\s*', l.strip())]
                         for l in lines])
    out = {'segments': segments}
    return out


def read(inputs_path: PathLike) -> List[str]:
    with open(inputs_path, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    inp = read('./inputs/10.txt')
    params = parse(inp)
    ans = solve(params)
    print(ans)

# print(
#     solve(
#         parse([
#             '0,9 -> 5,9',
#             '8,0 -> 0,8',
#             '9,4 -> 3,4',
#             '2,2 -> 2,1',
#             '7,0 -> 7,4',
#             '6,4 -> 2,0',
#             '0,9 -> 2,9',
#             '3,4 -> 1,4',
#             '0,0 -> 8,8',
#             '5,5 -> 8,2',
#         ])))
