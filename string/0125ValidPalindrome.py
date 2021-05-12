from problem_abc import ProblemAbc
import re


class Problem125(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/valid-palindrome/"
        self.test_cases = ["A man, a plan, a canal: Panama", "race a car"]
        self.y = [True, False]

    @staticmethod
    def solution(test_case):
        s = test_case
        if len(s) < 2:
            return True
        regex = re.compile('[^a-zA-Z0-9]')
        s2 = regex.sub('', s)
        s2 = s2.lower()
        return s2 == s2[::-1]


if __name__ == '__main__':
    p = Problem125()
    p.submit()
