from collections import Counter

from problem_abc import ProblemAbc


class Problem389(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/find-the-difference/"
        self.test_cases = [("abcd", "abcde"), ("", "y"), ("a", "aa"), ("ae", "aea")]
        self.y = ["e", "y", "a", "a"]

    @staticmethod
    def solution(test_case):
        s = test_case[0]
        t = test_case[1]

        cs = Counter(s)
        ct = Counter(t)
        for i in ct:
            if i not in cs:
                return i
            if ct[i] != cs[i]:
                return i


if __name__ == '__main__':
    p = Problem389()
    p.submit()
