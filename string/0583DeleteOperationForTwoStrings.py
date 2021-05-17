from collections import Counter

from problem_abc import ProblemAbc


class Problem583(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/delete-operation-for-two-strings/"
        self.test_cases = [("sea", "eat"), ("leetcode", "etco"), ("a", "a"), ("tea", "eat")]
        self.y = [2, 4, 0, 2]

    @staticmethod
    def solution(test_case):
        word1 = test_case[0]
        word2 = test_case[1]

        # longest sequence
        l1 = len(word1)
        l2 = len(word2)
        c = [[0 for _ in range(l2 + 1)] for __ in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    c[i + 1][j + 1] = c[i][j] + 1
                else:
                    c[i + 1][j + 1] = max(c[i][j + 1], c[i + 1][j])
        return l1 + l2 - c[-1][-1] * 2


if __name__ == '__main__':
    p = Problem583()
    p.submit()
