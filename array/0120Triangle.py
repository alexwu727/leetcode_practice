from problem_abc import ProblemAbc


class Problem0120(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/triangle/"
        self.test_cases = [
            [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],[[-10]]]
        self.y = [11, -10]

    @staticmethod
    def solution(test_case):
        triangle = test_case
        if len(triangle) == 1:
            return triangle[0][0]
        for level in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[level])):
                triangle[level][i] += min(triangle[level + 1][i], triangle[level + 1][i + 1])
        return triangle[0][0]


if __name__ == '__main__':
    p = Problem0120()
    p.submit()
