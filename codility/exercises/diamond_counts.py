"""
https://app.codility.com/programmers/trainings/3/diamonds_count/

A diamond is a quadrilateral whose four sides all have the same length and whose diagonals are parallel to the coordinate axes.

You are given N distinct points on a plane. Count the number of different diamonds that can be constructed using these points as vertices (two diamonds are different if their sets of vertices are different). Do not count diamonds whose area is empty.

Write a function:

def solution(X, Y)

that, given two arrays X and Y, each containing N integers, representing N points (where X[K], Y[K] are the coordinates of the K-th point), returns the number of diamonds on the plane.

For example, for N = 7 points whose coordinates are specified in arrays X = [1, 1, 2, 2, 2, 3, 3] and Y = [3, 4, 1, 3, 5, 3, 4], the function should return 2, since we can find two diamonds as shown in the picture below:



Given arrays: X = [1, 2, 3, 3, 2, 1], Y = [1, 1, 1, 2, 2, 2], the function should return 0, since there are no diamonds on the plane:



Write an efficient algorithm for the following assumptions:

N is an integer within the range [4..1,500];
each element of arrays X and Y is an integer within the range [0..N-1];
given N points are pairwise distinct.
"""

from collections import defaultdict


def y_coordinate_to_points(X, Y):
    y_to_points = defaultdict(list)
    for x, y in zip(X, Y):
        y_to_points[y].append(x)
    return y_to_points


def x_coordinate_to_points(X, Y):
    x_to_points = defaultdict(list)
    for x, y in zip(X, Y):
        x_to_points[x].append(y)
    return x_to_points


def get_all_points(X, Y):
    return set(zip(X, Y))


def solution(X, Y):
    x_coords_of_points_with_same_y = y_coordinate_to_points(X, Y)
    y_coords_of_points_with_same_x = x_coordinate_to_points(X, Y)
    all_points = get_all_points(X, Y)
    nb_of_diamonds = 0
    for top_x, top_y in all_points:
        candidates_botom = []
        for candidate_y in y_coords_of_points_with_same_x[top_x]:
            if candidate_y < top_y:
                candidates_botom.append((top_x, candidate_y))
        if len(candidates_botom) == 0:
            continue
        for candidate_bottom in candidates_botom:
            bottom_x, bottom_y = candidate_bottom
            mid_y = (top_y + bottom_y) / 2
            all_x_points_on_mid_y_axis = sorted(x_coords_of_points_with_same_y[mid_y])
            # print(top_x, top_y, "--", bottom_x, bottom_y, "--", mid_y, all_x_points_on_mid_y_axis)
            if len (all_x_points_on_mid_y_axis) < 2:
                continue
            for candidate_x1 in all_x_points_on_mid_y_axis:
                if candidate_x1 >= top_x:
                    break
                candidate_x2 = top_x + (top_x - candidate_x1)
                if candidate_x2 in all_x_points_on_mid_y_axis:
                    nb_of_diamonds += 1
                    # print("Found diamond: ", top_x, top_y, "--", bottom_x, bottom_y, "--", candidate_x1, mid_y, "--", candidate_x2, mid_y)

    return nb_of_diamonds




def test_x_to_points():
    X = [1, 1, 2, 2, 2, 3, 3]
    Y = [3, 4, 1, 3, 5, 3, 4]
    x_to_points = x_coordinate_to_points(X, Y)
    assert x_to_points == {1: [3, 4], 2: [1, 3, 5], 3: [3, 4]}


def test_y_to_points():
    X = [1, 1, 2, 2, 2, 3, 3]
    Y = [3, 4, 1, 3, 5, 3, 4]
    y_to_points = y_coordinate_to_points(X, Y)
    assert y_to_points == {3: [1, 2, 3], 4: [1, 3], 1: [2], 5: [2]}


def test_all_points():
    X = [1, 1, 2, 2, 2, 3, 3]
    Y = [3, 4, 1, 3, 5, 3, 4]
    all = get_all_points(X, Y)
    assert all == {(1, 3), (1, 4), (2, 1), (2, 3), (2, 5), (3, 3), (3, 4)}
    assert (2, 3) in all
    assert (3, 2) not in all


test_x_to_points()
test_y_to_points()
test_all_points()

def test1():
    X = [1, 1, 2, 2, 2, 3, 3]
    Y = [3, 4, 1, 3, 5, 3, 4]
    assert  solution(X, Y) == 2

def test0():
    X = []
    Y = []
    assert  solution(X, Y) == 0



test0()