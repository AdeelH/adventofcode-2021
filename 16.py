from typing import Iterable, List
from os import PathLike
from collections import defaultdict


def solve(params: dict) -> int:
    inputs: List[str] = params['inputs']
    outputs: List[str] = params['outputs']
    out = sum(decode(inp, out) for inp, out in zip(inputs, outputs))
    return out


def decode(in_signals: Iterable[str], out_signals: Iterable[str]) -> int:
    mapping = signals_to_mapping(in_signals)
    unjumbled = unjumble(out_signals, mapping)
    num = signals_to_num(unjumbled)
    return num


def signals_to_mapping(signals: str) -> dict:
    len_to_signals = defaultdict(list)
    for s in signals:
        len_to_signals[len(s)].append(s)
    len_to_signals = {
        k: v if len(v) > 1 else v[0]
        for k, v in len_to_signals.items()
    }
    in_069 = lambda c: all(c in s for s in len_to_signals[6])
    mapping = {}
    mapping['f'] = [c for c in len_to_signals[2] if in_069(c)]
    mapping['c'] = [c for c in len_to_signals[2] if c not in mapping['f']]
    mapping['a'] = [
        c for c in len_to_signals[3] if c not in mapping['c'] + mapping['f']
    ]
    bd = set(len_to_signals[4]) - set(len_to_signals[2])
    mapping['b'] = [c for c in bd if in_069(c)]
    mapping['d'] = [c for c in bd if c not in mapping['b']]
    eg = set('abcdefg') - set(sum(mapping.values(), []))
    mapping['g'] = [c for c in eg if in_069(c)]
    mapping['e'] = [c for c in eg if c not in mapping['g']]
    assert all(len(v) for v in mapping.values())
    mapping = {v[0]: k for k, v in mapping.items()}
    return mapping


def unjumble(signals: str, mapping: dict) -> List[List[str]]:
    signals = [[mapping[c] for c in s] for s in signals]
    return signals


def signals_to_num(signals: str) -> int:
    num = int(''.join(str(signal_to_digit(s)) for s in signals))
    return num


def signal_to_digit(signal: Iterable[str]) -> int:
    s = set(signal)
    if s == set('abcefg'):
        return 0
    elif s == set('cf'):
        return 1
    elif s == set('acdeg'):
        return 2
    elif s == set('acdfg'):
        return 3
    elif s == set('bcdf'):
        return 4
    elif s == set('abdfg'):
        return 5
    elif s == set('abdefg'):
        return 6
    elif s == set('acf'):
        return 7
    elif s == set('abcdefg'):
        return 8
    elif s == set('abcdfg'):
        return 9
    raise ValueError(s)


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
    inp = read('./inputs/16.txt')
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
