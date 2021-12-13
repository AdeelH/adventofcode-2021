from typing import List, Tuple
from os import PathLike
import numpy as np
from scipy.signal import convolve2d


def solve(params: dict) -> int:
    arr: np.ndarray = params['arr']
    steps: np.ndarray = params['steps']
    k = np.ones((3, 3))
    k[1, 1] = 0
    total_flashes = 0
    for i in range(steps):
        arr, step_flash_mask = step(arr, k)
        total_flashes += step_flash_mask.sum()
    out = total_flashes
    return out


def step(arr: np.ndarray, k: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    step_flash_mask = np.zeros(arr.shape, dtype=bool)
    arr = (arr + 1) % 10
    flash_mask = arr == 0
    while np.any(flash_mask):
        step_flash_mask |= flash_mask
        flash_inc = convolve2d(flash_mask, k, mode='same').astype(np.int64)
        arr = np.clip((arr + ((~step_flash_mask) * flash_inc)), 0, 10) % 10
        flash_mask = (arr == 0) & ~step_flash_mask
    return arr, step_flash_mask


def parse(lines: list) -> dict:
    arr = np.array([[int(c) for c in l] for l in lines])
    out = {'arr': arr, 'steps': 100}
    return out


def read(inputs_path: PathLike) -> List[str]:
    with open(inputs_path, 'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if len(l) > 0]
    return lines


def pprint(arr):
    for row in arr.tolist():
        print(''.join(map(str, row)))
    print()


if __name__ == '__main__':
    inp = read('./inputs/21.txt')
    params = parse(inp)
    ans = solve(params)
    print(ans)

# print(solve(parse("""11111
# 19991
# 19191
# 19991
# 11111""".split('\n'))))

# print(
#     solve(
#         parse("""6594254334
# 3856965822
# 6375667284
# 7252447257
# 7468496589
# 5278635756
# 3287952832
# 7993992245
# 5957959665
# 6394862637""".split('\n'))))

# print(
#     solve(
#         parse("""5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526""".split('\n'))))
