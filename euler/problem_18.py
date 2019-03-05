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

# A potential clever trick: once we parse the initial triangle, cumulate
# the valuses:
# 
#                                   A
#                                  B C
#                                 D E F
# 
# becomes
# 
#                                   A
#                                A+B A+C
#                        A+B+D max(A+B+E, A+C+E) A+C+F
# 
# Then the max value is just the largest leaf. No tree traversal, no
# clever path algorithms.
#
# Note that the inner values must take the max of their two parent-sums.
# We can get away with this because the larger value represents the path
# we would choose to take when we're summing terms.


def parse_triangle(tri_str):
    rows = [[int(n) for n in r.split()]
            for r in tri_str.strip().split('\n')]
    return rows


def cumulate_triangle(tri):
    assert len(tri) > 0
    res = [tri[0]]
    for i, row in enumerate(tri[1:]):
        prev_row = res[i]
        # r[0] increments r-1[0]; r[-1] increments r-1[-1],
        # everything in between ads max(r-1[i-1] and r-1[i])
        first = row[0] + prev_row[0]
        last = row[-1] + prev_row[-1]
        inner = []
        if len(row) > 2:
            inner = [row[j] + max(prev_row[j-1], prev_row[j])
                     for j in range(1, len(row)-1)]
        res.append([first] + inner + [last])
    return res


def max_path_sum(tri):
    cumul = cumulate_triangle(tri)
    # greatest path sum is just the largest leaf value in the last row
    return max(cumul[-1])



if __name__ == '__main__':
    PROBLEM_INPUT = '''
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
'''
    answer = max_path_sum(parse_triangle(PROBLEM_INPUT))
    print("Max path sum in problem triangle: {}".format(answer))
