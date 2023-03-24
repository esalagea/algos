"""
For a given set of denominations, you are asked to find the minimum number of coins with which a given amount of money can be paid.
"""
import random

from pandas import *


def coin_changing(denominations, amount):
    """
    Let dp[i,j] be the minimum number of coins needed to pay the amount j if we use the set containing the i smallest denominations.
    Let te denominations be c1, c2,..., ci, ..., cn


    dp[i,0] = 0
    dp[0,j] = infinity
    dp[i, j] = dp[i-1, j] if j < ci   -> we cannot use the i-th denomination because the amaount to pay j is smaller than the denomination
    dp[i,j] = min(dp[i,j − ci] + 1,dp[i − 1,j]) (for all i > 0 and all j such that ci <= j)   -> eitherwe use the i-th denomination or we don't
    """
    rows = len(denominations) + 1
    cols = amount + 1

    dp = [[0] * cols for _ in range(rows)]

    for j in range(1, cols):
        dp[0][j] = float("inf")

    for i in range(1, rows):
        for j in range(1, cols):
            if j < denominations[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i][j - denominations[i - 1]] + 1, dp[i - 1][j])

    # print(DataFrame(dp))

    print (f"coin_changing iterations DP: {rows * cols}")

    return (dp[rows - 1][cols - 1])


def coin_changing_with_recursion(denominations, amount):
    iterations = 0

    def coin_changing_rec(denominations, amount, coins_used):
        nonlocal iterations
        iterations += 1
        if amount == 0:
            return coins_used

        best_solution = float("inf")
        for denomination in denominations:
            if denomination <= amount:
                solution = coin_changing_rec(denominations, amount - denomination, coins_used + 1)
                if solution == None:
                    continue
                if best_solution > solution:
                    best_solution = solution
        return best_solution

    solution = coin_changing_rec(denominations, amount, 0)
    print(f"coin_changing_with_recursion iterations: {iterations}")
    return solution


def coin_changing_with_recursion_and_memoization(denominations, amount):
    iterations = 0

    def coin_changing_rec(denominations, amount, coins_used, memo):
        nonlocal iterations
        iterations += 1
        if amount == 0:
            return coins_used

        previously_coined_used = memo.get(amount, float("inf"))
        if previously_coined_used <= coins_used:
            return float("inf")
        if (amount, coins_used) in memo:
            return memo[(amount, coins_used)]

        best_solution = float("inf")
        for denomination in denominations:
            if denomination <= amount:
                solution = coin_changing_rec(denominations, amount - denomination, coins_used + 1, memo)
                if best_solution > solution:
                    best_solution = solution
        memo[amount] = coins_used
        return best_solution

    sol = coin_changing_rec(denominations, amount, 0, {})
    print(f"coin_changing_with_recursion_and_memoization iterations: {iterations}")
    return sol


def coin_changing_by_ChatGPT(denominations, amount):
    iterations = 0

    def helper(coin_index, remaining_amount, memo):
        nonlocal iterations

        """
        The helper function takes two parameters i and j, which represent the current
        denomination index and the remaining amount to be paid, respectively.
        """
        iterations += 1
        if remaining_amount == 0:
            return 0
        if coin_index == len(denominations):
            return float("inf")
        if (coin_index, remaining_amount) in memo:
            return memo[(coin_index, remaining_amount)]
        if remaining_amount < denominations[coin_index]:
            result = helper(coin_index + 1, remaining_amount, memo)
        else:
            result = min(helper(coin_index, remaining_amount - denominations[coin_index], memo) + 1, helper(coin_index + 1, remaining_amount, memo))
        memo[(coin_index, remaining_amount)] = result
        return result

    memo = {}
    solution = helper(0, amount, memo)
    print (f"coin_changing_by_ChatGPT iterations: {iterations}")
    return solution


def test_DP():
    denominations = [1, 3, 4]
    amount = 6
    assert coin_changing(denominations, amount) == 2


def test_recursion():
    denominations = [1, 3, 4]
    amount = 6
    assert coin_changing_with_recursion(denominations, amount) == 2


def test_recursion_with_memo():
    denominations = [1, 3, 4]
    amount = 6
    assert coin_changing_with_recursion_and_memoization(denominations, amount) == 2

def test_ChatGPT():
    denominations = [1, 3, 4]
    amount = 6
    assert coin_changing_by_ChatGPT(denominations, amount) == 2



def test_random(number_of_denominations, max_denomination_value, amount):
    # generate 20 random denominations with values under 100
    denominations = [random.randint(1, max_denomination_value) for _ in range(number_of_denominations)]
    denominations.sort()
    dp_solution = coin_changing(denominations, amount)
    rec_solution_with_memo = coin_changing_with_recursion_and_memoization(denominations, amount)
    chat_GPT_solution = coin_changing_by_ChatGPT(denominations, amount)
    assert dp_solution == rec_solution_with_memo == chat_GPT_solution


def all_tests():
    test_DP()
    test_recursion()
    test_recursion_with_memo()
    test_ChatGPT()

    print ("----------------------------")
    test_random(5, 10, 20)

    print ("----------------------------")
    test_random(20, 100, 300)

    print ("----------------------------")
    test_random(20, 100, 1000)

    print("All tests passed")


all_tests()
