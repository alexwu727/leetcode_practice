from problem_abc import ProblemAbc


class Problem658(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/find-k-closest-elements/"
        self.test_cases = [([1, 2, 3, 4, 5], 4, 3), ([1, 2, 4, 6, 7], 3, 5), ([1, 2, 4, 16, 17], 3, 5)]
        self.y = [[1, 2, 3, 4], [4, 6, 7], [1, 2, 4]]

    @staticmethod
    def solution(test_case):
        arr = test_case[0]
        k = test_case[1]
        x = test_case[2]

        left = 0
        right = len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
        left = 0
        right = len(arr) - 1
        target_index = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                target_index = mid
                left = mid
                break
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        if target_index == -1:
            if x < arr[0]:
                return arr[:k]
            if x > arr[-1]:
                return arr[-k:]
            target_index = left - 1 if x - arr[left - 1] <= arr[left] - x else left
        left = target_index
        right = left
        while right - left < k - 1:
            if left == 0:
                return arr[:k]
            if right == len(arr) - 1:
                return arr[-k:]
            left_diff = x - arr[left - 1]
            right_diff = arr[right + 1] - x
            if left_diff <= right_diff:
                left -= 1
            else:
                right += 1

        return arr[left:right + 1]


if __name__ == '__main__':
    p = Problem658()
    p.submit()
