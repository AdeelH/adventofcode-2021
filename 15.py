from typing import List
from os import PathLike


def solve(params: dict) -> int:
    inputs: List[str] = params['inputs']
    outputs: List[str] = params['outputs']
    num_easy_digits = 0
    for inp, out in zip(inputs, outputs):
        digits = [signal_to_digit(s) for s in out]
        num_easy_digits += len([d for d in digits if d is not None])

    out = num_easy_digits
    return out


unique_mappings = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}


def signal_to_digit(signal: str) -> int:
    n = len(signal)
    if n in unique_mappings:
        return unique_mappings[n]


def parse(lines: list) -> dict:
    parts = [[part.strip() for part in l.split('|')] for l in lines]
    inputs = [p.split(' ') for p, _ in parts]
    outputs = [p.split(' ') for _, p in parts]
    out = {'inputs': inputs, 'outputs': outputs}
    return out


def read(inputs_path: PathLike) -> List[str]:
    with open(inputs_path, 'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines


if __name__ == '__main__':
    inp = read('./inputs/15.txt')
    params = parse(inp)
    ans = solve(params)
    print(ans)

# print(
#     solve(
#         parse(
#             """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
#             .split('\n'))))
