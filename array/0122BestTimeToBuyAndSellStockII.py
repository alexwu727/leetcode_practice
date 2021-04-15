from problem_abc import ProblemAbc


class Problem122(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/"
        self.test_cases = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1], [12], [1, 2, 3, 4, 5]]
        self.y = [7, 0, 0, 4]

    @staticmethod
    def solution(test_case):
        prices = test_case
        ans = 0
        for i in range(len(prices) - 1):
            ans += max(0, prices[i + 1] - prices[i])
        return ans


if __name__ == '__main__':
    p = Problem122()
    p.submit()
