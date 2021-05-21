from problem_abc import ProblemAbc


class Problem64(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/minimum-path-sum/"
        self.test_cases = [[[1, 3, 1], [1, 5, 1], [4, 2, 1]], [[1, 2, 3], [4, 5, 6]]]
        self.y = [7, 12]

    @staticmethod
    def solution(test_case):
        grid = test_case
        dp = grid.copy()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] += dp[i][j - 1]
                elif j == 0:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]


if __name__ == '__main__':
    p = Problem64()
    p.submit()
