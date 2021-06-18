from problem_abc import ProblemAbc


class Problem154(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/"
        self.test_cases = [[1, 3, 5], [2, 2, 2, 0, 1], [2, 2, 2, 1, 2, 2], [2, 1, 2, 2, 2, 2]]
        self.y = [1, 0, 1, 1]

    @staticmethod
    def solution(test_case):
        nums = test_case

        if nums[0] < nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[0]


if __name__ == '__main__':
    p = Problem154()
    p.submit()
