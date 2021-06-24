from problem_abc import ProblemAbc


class Problem77(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/combinations/"
        self.test_cases = [(4, 2), (1, 1)]
        self.y = [[[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4], ], [[1]]]
        self.adjust_output = "any_order"

    @staticmethod
    def solution(test_case):
        n = test_case[0]
        k = test_case[1]

        ans = []

        def backtrack(tmpList=[], remain=k):
            if remain == 0:
                ans.append(tmpList)
                return
            start = tmpList[-1] + 1 if tmpList else 1
            # huge improvement by adding this condition
            if n - start + 1 < remain:
                return
            if n - start + 1 == remain:
                ans.append(tmpList + list(range(start, n + 1)))
                return
            for i in range(start, n + 1):
                backtrack(tmpList + [i], remain - 1)

        backtrack()
        return ans


if __name__ == '__main__':
    p = Problem77()
    p.submit()
