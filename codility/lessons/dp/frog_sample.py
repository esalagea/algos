"""A small frog wants to get from position 0 to k (1 <= k <= 10000). The frog can jump over any one of n fixed
distances s0,s1,...,sn−1 (1 <= si <= k). The goal is to count the number of different ways in which the frog can jump
to position k. To avoid overflow, it is sufficient to return the result modulo q, where q is a given number. We
assume that two patterns of jumps are different if, in one pattern, the frog visits a position which is not visited
in the other pattern.
"""


""" 
Algorithm: 


The number of ways in which the frog can jump to position j with a final jump of si is dp[j − si].

dp[0] = 1
dp[j] = sum(dp[j − si] for si in S if j − si >= 0
"""


def frog(S, k, q):
    dp = [0] * (k + 1)
    dp[0] = 1
    for j in range(1, k + 1):
        for si in S:
            if j - si >= 0:
                dp[j] += dp[j - si] % q
    return dp[k] % q


def test_small_frog():
    assert frog([1, 2, 3], 5, 1) == 13

def test_medium_frog():
    assert frog([1, 3, 5], 10, 1) == 49


def test_large_frog():
    assert frog([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1000, 1000000007) == 504365805