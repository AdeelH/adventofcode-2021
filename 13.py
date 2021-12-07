from typing import List
from os import PathLike
import numpy as np


def solve(params: dict) -> int:
    nums: np.array = params['nums']
    m = np.median(nums)
    cost = np.abs(nums - m).sum()
    return cost


def parse(lines: list) -> dict:
    nums = np.array([int(s.strip()) for s in lines[0].split(',')])
    out = {'nums': nums}
    return out


def read(inputs_path: PathLike) -> List[str]:
    with open(inputs_path, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    inp = read('./inputs/13.txt')
    params = parse(inp)
    ans = solve(params)
print(ans)

# print(solve({'nums': np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])}))
