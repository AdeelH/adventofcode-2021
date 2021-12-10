from typing import List
from os import PathLike
from collections import deque


def solve(params: dict) -> int:
    lines: List[str] = params['lines']
    out = sum(calc_score(l) for l in lines)
    return out


def calc_score(line: str) -> int:
    stack = deque()
    score_mapping = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
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
        elif c in closings:
            if matching_pairs[c] == stack.pop():
                continue
            else:
                return score_mapping[c]
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
    inp = read('./inputs/19.txt')
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
