from problem_abc import ProblemAbc


class Problem1800(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/maximum-ascending-subarray-sum/"
        self.test_cases = [[10, 20, 30, 5, 10, 50], [10, 20, 30, 40, 50], [12, 17, 15, 13, 10, 11, 12], [100, 10, 1],
                           [1, 1]]
        self.y = [65, 150, 33, 100, 1]

    @staticmethod
    def solution(nums):
        s, ans = 0, 0
        for i in range(len(nums)):
            s += nums[i]
            if i == len(nums) - 1 or nums[i] >= nums[i + 1]:
                ans = s if s > ans else ans
                s = 0
        return ans + 1


if __name__ == '__main__':
    p = Problem1800()
    p.submit()
