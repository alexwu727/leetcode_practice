from problem_abc import ProblemAbc


class Problem11(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/container-with-most-water/"
        self.test_cases = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1], [4, 3, 2, 1, 4], [1, 2, 1],
                           [1, 8, 6, 2, 5, 4, 8, 25, 7]]
        self.y = [49, 1, 16, 2, 49]

    @staticmethod
    def solution(test_case):
        height = test_case
        left = 0
        right = len(height) - 1
        ans = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            ans = max(ans, min(height[left], height[right]) * (right - left))
        return ans


if __name__ == '__main__':
    p = Problem11()
    p.submit()
