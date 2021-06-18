from problem_abc import ProblemAbc


class Problem167(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"
        self.test_cases = [([2, 7, 11, 15], 9), ([2, 3, 4], 6), ([3, 3], 6), ([-1, 0], -1)]
        self.y = [[1, 2], [1, 3], [1, 2], [1, 2]]

    @staticmethod
    def solution(test_case):
        numbers = test_case[0]
        target = test_case[1]

        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    p = Problem167()
    p.submit()
