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
        self.active = True

    def mark(self, n: int) -> Optional[int]:
        if not self.active or n not in self.num2pos:
            return
        i, j = self.num2pos[n]
        self.arr[i, j] = 0
        self.row_sums[i] -= n
        self.col_sums[j] -= n
        if self.row_sums[i] == 0 or self.col_sums[j] == 0:
            self.active = False
            return self.arr.sum() * n


def solve(params: dict) -> int:
    nums: np.array = params['nums']
    boards: List[BingoBoard] = params['boards']
    last_winning_score = None
    active_boards = len(boards)
    for n in nums:
        if active_boards == 0:
            break
        for b in boards:
            winning_score = b.mark(n)
            if winning_score is not None:
                last_winning_score = winning_score
                active_boards -= 1
    return last_winning_score


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
    inp = read('./inputs/8.txt')
    params = parse(inp)
    ans = solve(params)
    print(ans)

# print(
#     solve(
#         parse(
#             read2(
#                 """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
# 8  2 23  4 24
# 21  9 14 16  7
# 6 10  3 18  5
# 1 12 20 15 19

# 3 15  0  2 22
# 9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
# 2  0 12  3  7"""))))
