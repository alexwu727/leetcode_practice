from problem_abc import ProblemAbc


class Problem4(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/median-of-two-sorted-arrays/"
        self.test_cases = [([1, 3], [2]), ([1, 2], [3, 4]), ([0, 0], [0, 0]), ([], [1]), ([2], [])]
        self.y = [2, 2.5, 0, 1, 2]

    @staticmethod
    def solution(test_case):
        nums1 = test_case[0]
        nums2 = test_case[1]

        nums = sorted(nums1 + nums2)
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        else:
            return nums[len(nums) // 2]


if __name__ == '__main__':
    p = Problem4()
    p.submit()
