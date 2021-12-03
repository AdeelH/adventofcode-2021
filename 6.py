from os import PathLike
import numpy as np


def solve(params: dict) -> int:
    readings = params['readings']
    ox_bin = find_ox_reading(readings)
    co2_bin = find_co2_reading(readings)
    ox_dec = bit_array_to_dec(ox_bin)
    co2_dec = bit_array_to_dec(co2_bin)
    out = ox_dec * co2_dec
    return out


def find_ox_reading(readings: np.array):
    def recurse(pos: int, mask: np.array) -> int:
        if pos == readings.shape[1]:
            return mask
        pos_bits = readings[:, pos]
        filtered_pos_bits = pos_bits[mask]
        if len(filtered_pos_bits) == 1:
            return mask
        val = int(filtered_pos_bits.mean() >= 0.5)
        next_mask = mask & (pos_bits == val)
        return recurse(pos + 1, next_mask)

    mask = recurse(0, np.ones(len(readings), dtype=bool))
    ox_bin = readings[mask].squeeze()
    return ox_bin


def find_co2_reading(readings: np.array):
    def recurse(pos: int, mask: np.array) -> int:
        if pos == readings.shape[1]:
            return mask
        pos_bits = readings[:, pos]
        filtered_pos_bits = pos_bits[mask]
        if len(filtered_pos_bits) == 1:
            return mask
        val = int(filtered_pos_bits.mean() < 0.5)
        next_mask = mask & (pos_bits == val)
        return recurse(pos + 1, next_mask)

    mask = recurse(0, np.ones(len(readings), dtype=bool))
    co2_bin = readings[mask].squeeze()
    return co2_bin


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
    inp = read('./inputs/6.txt')
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
