from os import PathLike
import numpy as np


def move_to_vector(dir: str, dist: int) -> tuple:
    if dir == 'forward':
        return (dist, 0)
    elif dir == 'backward':
        return (-dist, 0)
    elif dir == 'up':
        return (0, -dist)
    elif dir == 'down':
        return (0, dist)
    else:
        raise ValueError(dir)


def solve(params: dict) -> tuple:
    dirs = params['dirs']
    dists = params['dists']
    init_x, init_y = params['init_x'], params['init_y']
    init_position = np.array((init_x, init_y))

    x_aim_vectors = np.array(
        [move_to_vector(dir, dist) for dir, dist in zip(dirs, dists)])
    x_aim_vectors[:, 1] = np.cumsum(x_aim_vectors[:, 1])

    x_y_vectors = x_aim_vectors
    x_y_vectors[:, 1] *= x_y_vectors[:, 0]

    final_position = init_position + x_y_vectors.sum(axis=0)
    out = final_position[0] * final_position[1]

    return final_position, out


def parse(lines: list) -> dict:
    moves = [line.strip().split(' ') for line in lines]
    dirs = [dir.lower() for dir, _ in moves]
    dists = [int(dist) for _, dist in moves]
    out = {
        'dirs': dirs,
        'dists': dists,
        'init_x': 0,
        'init_y': 0,
        'init_aim': 0
    }
    return out


def read(inputs_path: PathLike) -> dict:
    with open(inputs_path, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    inp = read('./inputs/4.txt')
    params = parse(inp)
    ans = solve(params)
    print(ans)

# print(
#     solve(
#         parse([
#             'forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'
#         ])))
