from problem_abc import ProblemAbc


class Problem322(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/minimum-path-sum/"
        self.test_cases = [([1, 2, 5], 11), ([2], 3), ([1], 0)]
        self.y = [3, -1, 0]

    @staticmethod
    def solution(test_case):
        coins = test_case[0]
        amount = test_case[1]

        # bottom-up dp, idea from rod_cutting bottom-up
        if amount == 0:
            return 0
        r = [0 for _ in range(amount + 1)]  # optimal solution for each amount
        s = [0 for _ in range(amount)]  # first coin of optimal solution
        for amt in range(1, amount + 1):
            min_coins = float("inf")
            for first_coin in coins:
                if first_coin > amt:
                    continue
                if min_coins > 1 + r[amt - first_coin]:
                    min_coins = 1 + r[amt - first_coin]
                    s[amt - 1] = first_coin
            r[amt] = min_coins
        return r[amount] if r[amount] != float("inf") else -1


if __name__ == '__main__':
    p = Problem322()
    p.submit()
