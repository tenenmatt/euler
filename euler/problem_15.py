"""
Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.

How many such routes are there through a 20×20 grid?

"""


from functools import lru_cache


# Combinatorial explosion makes this benefit tremendously from lru_cache
# (which lets us write grid_paths in a nice recursive way without
# worrying about the evaluation cost)

@lru_cache(512)
def grid_paths(x, y):
    # If one position is at 1 (eg, (1, y) or (x, 1)),
    # number of paths is just 1 + the other position
    if 1 in {x, y}:
        return 1 + max(x, y)
    # Otherwise, sum of paths after rightward step and after downward step
    return grid_paths(x - 1, y) + grid_paths(x, y - 1)


if __name__ == '__main__':
    answer = grid_paths(20, 20)
    print("Possible down/right paths through 20x20 grid: {}".format(answer))
