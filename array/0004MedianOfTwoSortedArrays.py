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

        # binary search
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        nums1 = [-float("inf")] + nums1 + [float("inf")]
        nums2 = [-float("inf")] + nums2 + [float("inf")]
        left = 0
        right = m + 1
        while left <= right:
            mid = (left + right) // 2
            tmp = (m + n) // 2 - mid
            if nums1[mid] <= nums2[tmp + 1] and nums2[tmp] <= nums1[mid + 1]:
                break
            elif nums2[tmp] > nums1[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        if (m + n) % 2 == 0:
            return (max(nums1[mid], nums2[tmp]) + min(nums1[mid + 1], nums2[tmp + 1])) / 2
        return min(nums1[mid + 1], nums2[tmp + 1])
        # sorted array
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        else:
            return nums[len(nums) // 2]


if __name__ == '__main__':
    p = Problem4()
    p.submit()
