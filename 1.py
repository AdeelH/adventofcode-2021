from os import PathLike
import numpy as np


def solve(params: dict) -> int:
    depths = params['depths']
    diffs = depths[1:] - depths[:-1]
    num_increases = int((diffs > 0).sum())
    return num_increases


def parse(inputs_path: PathLike) -> dict:
    with open(inputs_path, 'r') as f:
        lines = f.readlines()
    out = {'depths': np.array([int(line.strip()) for line in lines])}
    return out


if __name__ == '__main__':
    params = parse('./inputs/1.txt')
    ans = solve(params)
    print(ans)
