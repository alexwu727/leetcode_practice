from problem_abc import ProblemAbc


class Problem43(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/multiply-strings/"
        self.test_cases = [("2", "3"), ("123", "456")]
        self.y = ["6", "56088"]

    @staticmethod
    def solution(test_case):
        num1 = test_case[0]
        num2 = test_case[1]

        return str(int(num1) * int(num2))


if __name__ == '__main__':
    p = Problem43()
    p.submit()
