from problem_abc import ProblemAbc


class Problem121(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
        self.test_cases = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1], [12], [1, 2, 3, 4, 5]]
        self.y = [5, 0, 0, 4]

    @staticmethod
    def solution(test_case):
        prices = test_case
        earning = 0
        low = prices[0]
        for i in prices[1:]:
            if low < i:
                earning = max(earning, i - low)
            else:
                low = i

        return earning


if __name__ == '__main__':
    p = Problem121()
    p.submit()
