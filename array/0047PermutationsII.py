from problem_abc import ProblemAbc


class Problem47(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/permutations/"
        self.test_cases = [[1, 1, 2], [1, 2, 3]]
        self.y = [[[1, 1, 2], [1, 2, 1], [2, 1, 1]], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]]

    @staticmethod
    def solution(test_case):
        nums = test_case

        ans = []
        seen = []

        def recur(picked, unpicked):
            if (picked, unpicked) in seen:
                return
            seen.append((picked, unpicked))
            if not unpicked:
                ans.append(picked)
                return
            for num in unpicked:
                tmp = unpicked.copy()
                tmp.remove(num)
                recur(picked + [num], tmp)

        recur([], nums)
        return ans


if __name__ == '__main__':
    p = Problem47()
    p.submit()
