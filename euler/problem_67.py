import argparse
import io

from problem_18 import max_path_sum, parse_triangle


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('tri')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    with open(args.tri, 'r') as f:
        tri_str = f.read()
        answer = max_path_sum(parse_triangle(tri_str))
        print("Max path sum for giant triangle: {}".format(answer))
