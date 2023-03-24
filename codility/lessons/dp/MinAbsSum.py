"""
For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:

val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

(Assume that the sum of zero elements equals zero.)

For a given array A, we are looking for such a sequence S that minimizes val(A,S).

Write a function:

def solution(A)

that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.

For example, given array:

  A[0] =  1
  A[1] =  5
  A[2] =  2
  A[3] = -2
your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..20,000];
each element of array A is an integer within the range [−100..100].
"""

def solution(A):
    """"
        Only keep the absolute values of A.
        dp[j,k] =


    """

    # corner cases
    # empty array
    if len(A) == 0:
        return 0

    # array with only one element
    if len(A) == 1:
        return abs(A[0])

    A = [abs(x) for x in A]
    n = 2 * max(A) + 1

    dp0 = [0] * n
    for k in range(n):
        dp0[k] = k - A[0]
    print (dp0)
    iteration = 1
    while iteration < len(A):
        dp1 = [0] * n
        for k in range(n):
            val1 = float('inf')
            target1 = abs(k - A[iteration])
            target2 = abs(k + A[iteration])

            val2 = float('inf')

            if target1 >= 0 and target1 < n:
                val1 = dp0[target1]

            if target2 >= 0 and target2 < n:
                val2 = dp0[target2]

            dp1[k] = min (abs(val1), abs(val2))
        dp0 = dp1
        print (dp0)
        iteration += 1

    return dp0[0]


def  test():
    A = [1, 5, 2, -2]
    assert solution(A) == 0


