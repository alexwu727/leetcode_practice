from problem_abc import ProblemAbc


class Problem153(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"
        self.test_cases = [[3, 4, 5, 1, 2], [4, 5, 6, 7, 0, 1, 2], [11, 12, 14, 17]]
        self.y = [1, 0, 11]

    @staticmethod
    def solution(test_case):
        nums = test_case

        if nums[0] <= nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1


if __name__ == '__main__':
    p = Problem153()
    p.submit()
