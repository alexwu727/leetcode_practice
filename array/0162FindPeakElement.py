from problem_abc import ProblemAbc


class Problem162(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/find-peak-element/"
        self.test_cases = [[1, 2, 3, 1], [1, 2, 1, 3, 5, 6, 4]]
        self.y = [2, 5]

    @staticmethod
    def solution(test_case):
        nums = test_case
        nums = [-float("inf")] + nums + [-float("inf")]
        left = 1
        right = len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            # if max(nums[mid], nums[mid-1], nums[mid+1]) == nums[mid]:
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid - 1
            # elif max(nums[mid], nums[mid-1], nums[mid+1]) == nums[mid-1]:
            elif nums[mid - 1] > nums[mid] and nums[mid - 1] > nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1


if __name__ == '__main__':
    p = Problem162()
    p.submit()
