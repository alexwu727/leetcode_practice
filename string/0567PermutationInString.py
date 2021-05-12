from collections import Counter

from problem_abc import ProblemAbc


class Problem567(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/permutation-in-string/"
        self.test_cases = [("ab", "eidbaooo"), ("ab", "eidboaoo")]
        self.y = [True, False]

    @staticmethod
    def solution(test_case):
        s1 = test_case[0]
        s2 = test_case[1]

        s1_len = len(s1)
        c1 = Counter(s1)
        c2 = Counter(s2[:s1_len])
        if c1 == c2:
            return True
        for a, b in zip(s2, s2[s1_len:]):
            c2[a] -= 1
            if c2[a] == 0:
                del c2[a]
            c2[b] += 1
            if c1 == c2:
                return True
        return False


if __name__ == '__main__':
    p = Problem567()
    p.submit()
