from problem_abc import ProblemAbc


class Problem55(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/jump-game/"
        self.test_cases = [[2,3,1,1,4], [3,2,1,0,4]]
        self.y = [True, False]

    @staticmethod
    def solution(test_case):
        nums = test_case
        target = len(nums) - 1
        for cur in range(len(nums)-2, -1, -1):
            if nums[cur] >= target - cur:
                target = cur
        return True if target == 0 else False


if __name__ == '__main__':
    p = Problem55()
    p.submit()
