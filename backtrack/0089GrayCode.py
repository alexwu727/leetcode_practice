from problem_abc import ProblemAbc


class Problem89(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/gray-code/"
        self.test_cases = [1, 2, 3]
        self.y = [[0, 1], [0, 1, 3, 2], [0, 1, 3, 2, 6, 7, 5, 4]]

    @staticmethod
    def solution(test_case):
        n = test_case

        ans = [0]
        for i in range(n):
            ans += [j + (1 << i) for j in ans[::-1]]
        return ans


if __name__ == '__main__':
    p = Problem89()
    p.submit()
