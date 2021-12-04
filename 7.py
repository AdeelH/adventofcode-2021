from os import PathLike
from typing import Optional, List
import numpy as np
from itertools import product
from re import split


class BingoBoard():
    def __init__(self, arr: np.array) -> None:
        self.arr = arr
        R, C = arr.shape
        self.num2pos = {
            arr[i, j]: (i, j)
            for (i, j) in product(range(R), range(C))
        }
        self.row_sums = arr.sum(axis=1)
        self.col_sums = arr.sum(axis=0)

    def mark(self, n: int) -> Optional[int]:
        if n not in self.num2pos:
            return
        i, j = self.num2pos[n]
        self.arr[i, j] = 0
        self.row_sums[i] -= n
        self.col_sums[j] -= n
        if self.row_sums[i] == 0 or self.col_sums[j] == 0:
            return self.arr.sum() * n


def solve(params: dict) -> int:
    nums: np.array = params['nums']
    boards: List[BingoBoard] = params['boards']
    for n in nums:
        for b in boards:
            winning_score = b.mark(n)
            if winning_score is not None:
                return winning_score
    raise Exception('Out of numbers!')


def parse(chunks: list) -> dict:
    nums = np.array([int(s) for s in chunks[0].split(',')])
    boards = []
    for chunk in chunks[1:]:
        board_arr = np.array([[int(s) for s in split('\s+', line.strip())]
                              for line in chunk.split('\n')])
        board = BingoBoard(board_arr)
        boards.append(board)

    out = {'nums': nums, 'boards': boards}

    return out


def read(inputs_path: PathLike) -> List[str]:
    with open(inputs_path, 'r') as f:
        text = f.read()
    chunks = [c.strip() for c in text.split('\n\n')]
    chunks = [c for c in chunks if len(c) > 0]
    return chunks


if __name__ == '__main__':
    inp = read('./inputs/7.txt')
    params = parse(inp)
    ans = solve(params)
    print(ans)
