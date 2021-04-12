from problem_abc import ProblemAbc


class Problem1(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/two-sum/"
        self.test_cases = [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]
        self.y = [[0, 1], [1, 2], [0, 1]]

    @staticmethod
    def solution(test_case):
        nums = test_case[0]
        target = test_case[1]

        hashtable = {}
        for i, num in enumerate(nums):
            if num in hashtable:
                return [hashtable[num], i]
            else:
                hashtable[target - num] = i


if __name__ == '__main__':
    p = Problem1()
    p.submit()
