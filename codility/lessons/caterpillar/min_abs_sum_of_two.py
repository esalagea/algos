"""
Let A be a non-empty array consisting of N integers.

The abs sum of two for a pair of indices (P, Q) is the absolute value |A[P] + A[Q]|, for 0 ≤ P ≤ Q < N.

For example, the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
has pairs of indices (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2).
The abs sum of two for the pair (0, 0) is A[0] + A[0] = |1 + 1| = 2.
The abs sum of two for the pair (0, 1) is A[0] + A[1] = |1 + 4| = 5.
The abs sum of two for the pair (0, 2) is A[0] + A[2] = |1 + (−3)| = 2.
The abs sum of two for the pair (1, 1) is A[1] + A[1] = |4 + 4| = 8.
The abs sum of two for the pair (1, 2) is A[1] + A[2] = |4 + (−3)| = 1.
The abs sum of two for the pair (2, 2) is A[2] + A[2] = |(−3) + (−3)| = 6.
Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the minimal abs sum of two for any pair of indices in this array.

For example, given the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
the function should return 1, as explained above.

Given array A:

  A[0] = -8
  A[1] =  4
  A[2] =  5
  A[3] =-10
  A[4] =  3
the function should return |(−8) + 5| = 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
"""

def solution(A):
    if len(A) == 0:
        return 0


    A.sort()
    left_index = 0
    right_index = len(A) - 1
    min_abs_sum = abs(A[left_index] + A[right_index])

    while (left_index < right_index):

        if A[left_index] > 0:
            return min ( min_abs_sum, abs(A[left_index] * 2 ))

        if A[right_index] < 0:
            return min (min_abs_sum, abs(A[right_index] *2 ))

        current_sum = abs(A[left_index] + A[right_index])
        if abs(current_sum) < min_abs_sum:
            min_abs_sum = abs(current_sum)

        if abs(A[left_index ]) < abs(A[right_index ]):
            right_index -= 1
        else:
            left_index += 1

    return min_abs_sum


def test():
    A = [1, 4, -3]
    assert solution(A) == 1
    print("test passed!")

def test_negative():
    A = [-8, 4, 5, -10, 3]
    assert solution(A) == 3
    print("test_negative passed!")

def test_all_positives():
    A = [8, 5, 3, 4, 6, 8]
    print(solution(A))
    assert solution(A) == 6

def test_all_negatives():
    A = [-8, -5, -3, -4, -6, -8]
    print(solution(A))
    assert solution(A) == 6
    print("test_all_negatives passed!")

def test2():
    A = [-10, -8, 3, 4, 5, 100, 200]
    assert solution(A) == 3
    print("test2 passed!")

def test_empty_array():
    A = []
    assert solution(A) == 0
    print("test_empty_array passed!")


test()
test_negative()
test_all_positives()
test_all_negatives()
test2()
test_empty_array()