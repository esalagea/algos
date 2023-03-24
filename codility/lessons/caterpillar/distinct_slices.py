"""
An integer M and a non-empty array A consisting of N non-negative integers are given. All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct slice is a slice consisting of only unique numbers.
That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..M].
"""




def solution_old(M, A):
    slices = 0
    start_index = 0

    elements_in_slice = set()
    while start_index < len(A):
        end_index = start_index

        duplicate_element = None
        while end_index < len(A) and duplicate_element is None:
            if A[end_index] in elements_in_slice:
                duplicate_element = A[end_index]
            else:
                elements_in_slice.add(A[end_index])
            end_index += 1
            slices += 1
        if slices > 1000000000:
            return 1000000000
        if duplicate_element is not None:
            # move start index forward until we find the duplicate element
            while A[start_index] != duplicate_element:
                elements_in_slice.remove(A[start_index])
                start_index += 1
        start_index += 1

    return slices

def test():
    A = [3, 4, 5, 5, 2]
    M = 6
    assert solution(M, A) == 9
    print("test passed!")

def test1():
    A = [1, 2, 3]
    M = 6
    result = solution(M, A)
    print(result)
    assert result == 6
    print("test passed!")



test1()


