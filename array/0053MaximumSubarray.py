from problem_abc import ProblemAbc


class Problem53(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/maximum-subarray/"
        self.test_cases = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8], [1, 2, 3, 4, 5],
                           [-1, -2, -3, -4, -5]]
        self.y = [6, 1, 23, 15, -1]

    @staticmethod
    def solution(test_case):
        nums = test_case
        if len(nums) == 1:
            return nums[0]
        current_subarray = ans = nums[0]
        for num in nums[1:]:
            current_subarray = max(num, num + current_subarray)
            ans = max(current_subarray, ans)
        return ans


if __name__ == '__main__':
    p = Problem53()
    p.submit()
