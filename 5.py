from os import PathLike
import numpy as np


def solve(params: dict) -> int:
    readings = params['readings']
    gamma_bin = (readings.mean(axis=0) > 0.5)
    epsilon_bin = ~gamma_bin
    gamma = bit_array_to_dec(gamma_bin)
    epsilon = bit_array_to_dec(epsilon_bin)
    out = gamma * epsilon
    return out


def bit_array_to_dec(bit_arr: np.array) -> int:
    bit_arr = bit_arr.astype(np.uint8)
    bit_str = ''.join(map(str, bit_arr))
    dec = int(bit_str, base=2)
    return dec


def parse(lines: list) -> dict:
    readings = [[int(char) for char in list(line.strip())] for line in lines]
    readings = np.array(readings)
    out = {'readings': readings}
    return out


def read(inputs_path: PathLike) -> dict:
    with open(inputs_path, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    inp = read('./inputs/5.txt')
    params = parse(inp)
    ans = solve(params)
    print(ans)

# print(
#     solve(
#         parse([
#             '00100',
#             '11110',
#             '10110',
#             '10111',
#             '10101',
#             '01111',
#             '00111',
#             '11100',
#             '10000',
#             '11001',
#             '00010',
#             '01010',
#         ])))
