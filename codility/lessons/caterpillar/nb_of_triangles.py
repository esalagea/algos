"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000];
each element of array A is an integer within the range [1..1,000,000,000].

"""


def solution(a):
    a.sort()
    nb_of_triangles = 0

    for x in range(len(a)):
        z = x + 2
        for y in range(x+1, len(a)):
            while z < len(a) and a[x] + a[y] > a[z]:
                z += 1
            nb_of_triangles += z - y - 1
    return nb_of_triangles


def test():
    A = [10, 2, 5, 1, 8, 12]
    result = solution(A)
    print(result)
    assert result == 4
    print("test passed!")


def test_empty():
    A = []
    assert solution(A) == 0
    A = [1]
    assert solution(A) == 0

    A = [1,2]
    assert solution(A) == 0
    print("test passed!")

    A = [1,2,3]
    assert solution(A) == 0
    print("test passed!")

    A = [1,2,4]
    assert solution(A) == 0
    print("test passed!")

test()
test_empty()
