"""
A rectangular map consisting of N rows and M columns of square areas is given. Each area is painted with a certain color.

Two areas on the map belong to the same country if the following conditions are met:

they have the same color;
it is possible to travel from one area to the other orthogonally (that is, by moving only north, south, west or east) without moving over areas of a different color.
The map can be described by a zero-indexed matrix A consisting of N rows and M columns of integers. The color of each area is described by the corresponding element of the matrix. Two areas have the same color if and only if their corresponding matrix elements have the same value.

For example, consider the following matrix A consisting of seven rows and three columns:

A[0][0] = 5    A[0][1] = 4    A[0][2] = 4
A[1][0] = 4    A[1][1] = 3    A[1][2] = 4
A[2][0] = 3    A[2][1] = 2    A[2][2] = 4
A[3][0] = 2    A[3][1] = 2    A[3][2] = 2
A[4][0] = 3    A[4][1] = 3    A[4][2] = 4
A[5][0] = 1    A[5][1] = 4    A[5][2] = 4
A[6][0] = 4    A[6][1] = 1    A[6][2] = 1
Matrix A describes a map that is colored with five colors. The areas on the map belong to eleven different countries (C1−C11), as shown in the following figure:


Write a function

def solution(A)

that, given a zero-indexed matrix A consisting of N rows and M columns of integers, returns the number of different countries to which the areas of the map described by matrix A belong.

For example, given matrix A consisting of seven rows and three columns corresponding to the example above, the function should return 11.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..300,000];
the number of elements in matrix A is within the range [1..300,000];
each element of matrix A is an integer within the range [−1,000,000,000..1,000,000,000].
"""
from copy import deepcopy


def get_all_positions(A):
    positions = set()
    for i in range(len(A)):
        for j in range(len(A[i])):
            positions.add((i, j))
    return positions


def pick_start_position(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] != -1:
                return i, j
    return None, None


def get_neighbours(A, row, col):
    """
    get al the neoghbouring cells that are not -1
    """
    neighbours = []
    if row > 0 and A[row - 1][col] != -1:
        neighbours.append((row - 1, col))
    if row < len(A) - 1 and A[row + 1][col] != -1:
        neighbours.append((row + 1, col))
    if col > 0 and A[row][col - 1] != -1:
        neighbours.append((row, col - 1))
    if col < len(A[0]) - 1 and A[row][col + 1] != -1:
        neighbours.append((row, col + 1))
    return neighbours


def explore_recursive(A, current_row, current_col, color):
    """
    explore the map recursively and mark all the cells that are part of the same country as -1
    """
    A[current_row][current_col] = -1
    neighbours = get_neighbours(A, current_row, current_col)
    for neighbour in neighbours:
        if A[neighbour[0]][neighbour[1]] == color:
            explore_recursive(A, neighbour[0], neighbour[1], color)


def solution_rec(a):
    nb_of_countries = 0
    A = deepcopy(a)
    start_row, start_col = pick_start_position(A)
    while (start_row, start_col) != (None, None):
        nb_of_countries += 1
        explore_recursive(A, start_row, start_col, A[start_row][start_col])
        start_row, start_col = pick_start_position(A)
    return nb_of_countries


def explore_bfs(A, start_row, start_col, color, all_pos):
    queue = [(start_row, start_col)]
    while queue:
        current_row, current_col = queue.pop(0)
        all_pos.remove((current_row, current_col)) if (current_row, current_col) in all_pos else None
        A[current_row][current_col] = -1
        neighbours = get_neighbours(A, current_row, current_col)
        for neighbour in neighbours:
            if A[neighbour[0]][neighbour[1]] == color:
                queue.append(neighbour)


def solution(a):
    nb_of_countries = 0
    A = deepcopy(a)
    all_pos = get_all_positions(A)
    start_row, start_col = all_pos.pop() if all_pos else (None, None)
    while (start_row, start_col) != (None, None):
        nb_of_countries += 1
        explore_bfs(A, start_row, start_col, A[start_row][start_col], all_pos)
        start_row, start_col = all_pos.pop() if all_pos else (None, None)
    return nb_of_countries


def test1():
    A = [[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]
    assert solution(A) == 11


def test0():
    A = []
    assert solution(A) == 0


def test2():
    A = [[1]]
    assert solution(A) == 1


def test3():
    A = [[1, 2], [3, 4]]
    assert solution(A) == 4


def test4():
    A = [[1, 1], [1, 2]]
    assert solution(A) == 2


def test5():
    A = [[1, 1], [1, 1]]
    assert solution(A) == 1


def test5():
    """
    A is a 4 x 4 labyrinth with 1s and 0s
    """
    A = [[1, 0, 0, 0],
         [1, 1, 1, 1],
         [0, 0, 0, 1],
         [1, 1, 1, 1]]
    assert solution(A) == 3


def test_get_neighbours_1():
    A = [[1, 2],
         [3, 4]]
    assert set(get_neighbours(A, 0, 0)) == set([(0, 1), (1, 0)])
    assert set(get_neighbours(A, 0, 1)) == set([(0, 0), (1, 1)])
    assert set(get_neighbours(A, 1, 0)) == set([(0, 0), (1, 1)])
    assert set(get_neighbours(A, 1, 1)) == set([(0, 1), (1, 0)])


def test_get_neighbours_2():
    A = [[1, -1],
         [3, -1]]
    assert set(get_neighbours(A, 0, 0)) == set([(1, 0)])
    assert set(get_neighbours(A, 1, 0)) == set([(0, 0)])


test0()
test1()
test3()
test4()
test5()

test_get_neighbours_1()
test_get_neighbours_2()
