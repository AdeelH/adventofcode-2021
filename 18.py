from typing import List
from os import PathLike
import numpy as np
from skimage.morphology import label


def solve(params: dict) -> int:
    map: np.array = params['map']
    basins, nbasins = label(map < 9, connectivity=1, return_num=True)
    basin_sizes = np.array([(basins == n + 1).sum() for n in range(nbasins)])
    top_3_basin_sizes = basin_sizes[np.argpartition(basin_sizes, -3)[-3:]]
    out = np.product(top_3_basin_sizes)
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
    inp = read('./inputs/18.txt')
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
