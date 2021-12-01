from os import PathLike
import numpy as np


def moving_sum(arr: np.ndarray, size: int) -> np.ndarray:
    N = len(arr)
    return sum(arr[i:N - (size - i - 1)] for i in range(size))


def solve(params: dict) -> int:
    depths = params['depths']
    window_size = params['window_size']
    depths = moving_sum(depths, window_size)
    diffs = depths[1:] - depths[:-1]
    num_increases = int((diffs > 0).sum())
    return num_increases


def parse(inputs_path: PathLike) -> dict:
    with open(inputs_path, 'r') as f:
        lines = f.readlines()
    out = {
        'depths': np.array([int(line.strip()) for line in lines]),
        'window_size': 3
    }
    return out


if __name__ == '__main__':
    params = parse('./inputs/2.txt')
    ans = solve(params)
    print(ans)

# print(
#     solve({
#         'depths': np.array([607, 618, 618, 617, 647, 716, 769, 792]),
#         'window_size': 3
#     }))
