from typing import List
from os import PathLike
import numpy as np
from functools import lru_cache


def solve(params: dict) -> int:
    timers: np.array = params['timers']
    days: int = params['days']
    spawn_days: int = params['spawn_days']
    maturity_days: int = params['maturity_days']
    out = fish_count(timers, days, spawn_days, maturity_days)
    return out


def fish_count(timers: np.array, days: int, spawn_days: int,
               maturity_days: int):
    @lru_cache(256)
    def recurse(t: int, days: int) -> int:
        if t + 1 > days:
            return 1
        birthdays = range(days - t - 1, -1, -spawn_days)  # in days-left units
        return 1 + sum(recurse(init_timer, _t) for _t in birthdays)

    init_timer = maturity_days + spawn_days - 1
    return sum(recurse(t, days) for t in timers)


def parse(lines: list) -> dict:
    timers = np.array([int(s.strip()) for s in lines[0].split(',')])
    out = {'timers': timers, 'days': 256, 'spawn_days': 7, 'maturity_days': 2}
    return out


def read(inputs_path: PathLike) -> List[str]:
    with open(inputs_path, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    inp = read('./inputs/12.txt')
    params = parse(inp)
    ans = solve(params)
    print(ans)

# print(
#     solve({
#         'timers': np.array([3, 4, 3, 1, 2]),
#         'days': 256,
#         'spawn_days': 7,
#         'maturity_days': 2
#     }))
