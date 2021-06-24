from problem_abc import ProblemAbc


class Problem78(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/subsets/"
        self.test_cases = [[1, 2, 3], [0]]
        self.y = [[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], [[], [0]]]
        self.adjust_output = "any_order"

    @staticmethod
    def solution(test_case):
        nums = test_case

        def backtrack(l, tmpList, nums, start):
            l.append(tmpList.copy())
            for i in range(start, len(nums)):
                tmpList.append(nums[i])
                backtrack(l, tmpList, nums, i + 1)
                tmpList.pop()

        l = []
        nums = sorted(nums)
        backtrack(l, [], nums, 0)
        return l


if __name__ == '__main__':
    p = Problem78()
    p.submit()
