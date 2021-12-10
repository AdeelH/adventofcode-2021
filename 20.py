from typing import List
from os import PathLike
from collections import deque
import numpy as np


def solve(params: dict) -> int:
    lines: List[str] = params['lines']
    scores = [calc_score(l) for l in lines]
    out = int(np.median([s for s in scores if s > 0]))
    return out


def calc_score(line: str) -> int:
    stack = deque()
    score_mapping = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    matching_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    openings = set(matching_pairs.values())
    closings = set(matching_pairs.keys())
    for c in line:
        if c in openings:
            stack.append(c)
        elif c in closings and matching_pairs[c] != stack.pop():
            return 0
    if len(stack) > 0:
        scores = (score_mapping[c] for c in reversed(stack))
        score = 0
        for s in scores:
            score = 5 * score + s
        return int(score)
    return 0


def parse(lines: list) -> dict:
    out = {'lines': lines}
    return out


def read(inputs_path: PathLike) -> List[str]:
    with open(inputs_path, 'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if len(l) > 0]
    return lines


if __name__ == '__main__':
    inp = read('./inputs/20.txt')
    params = parse(inp)
    ans = solve(params)
    print(ans)

# print(
#     solve(
#         parse("""[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]""".split('\n'))))
