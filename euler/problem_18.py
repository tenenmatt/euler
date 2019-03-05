"""
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                  3
                                 7 4
                                2 4 6
                               8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                                  75
                                95 64
                               17 47 82
                             18 35 87 10
                            20 04 82 47 65
                          19 01 23 75 03 34
                         88 02 77 73 07 63 67
                       99 65 04 28 06 16 70 92
                      41 41 26 56 83 40 80 70 33
                    41 48 72 33 47 32 37 16 94 29
                   53 71 44 65 25 43 91 52 97 51 14
                 70 11 33 28 77 73 17 78 39 68 17 57
                91 71 52 38 17 14 91 43 58 50 27 29 48
              63 66 04 68 89 53 67 30 73 16 69 87 40 31
             04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this
problem by trying every route. However, Problem 67, is the same
challenge with a triangle containing one-hundred rows; it cannot be
solved by brute force, and requires a clever method! ;o)

"""


from collections import namedtuple

Node = namedtuple('Node', 'value, left, right')


def parse_triangle(tri_str):
    rows = [[int(n) for n in r.split()]
            for r in tri_str.strip().split('\n')]
    return rows


def make_tree(rows):
    def crown(tree_rows):
        return tree_rows[0][0]

    if len(rows) == 1:
        return Node(crown(rows), None, None)
    else:
        return Node(crown(rows),
                    # left subtree
                    make_tree([r[:-1] for r in rows[1:]]),
                    # right subtree
                    make_tree([r[1:] for r in rows[1:]]))


def is_leaf(node):
    return node.left is None and node.right is None


# Always take the largest next option. This won't always work!
def max_path_sum(tree):
    node_value = tree.value
    if is_leaf(tree):
        return node_value
    elif tree.left > tree.right:
        return node_value + max_path_sum(tree.left)
    else:
        return node_value + max_path_sum(tree.right)


def paths(tree):
    pass


