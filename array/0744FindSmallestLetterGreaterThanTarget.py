from problem_abc import ProblemAbc


class Problem744(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/find-smallest-letter-greater-than-target/"
        self.test_cases = [(["c", "f", "j"], "a"), (["c", "f", "j"], "c"), (["c", "f", "j"], "d"),
                           (["c", "f", "j"], "g"), (["c", "f", "j"], "j"), (["c", "f", "j"], "z"),
                           (["e", "e", "e", "e", "n", "n"], "e")]
        self.y = ["c", "f", "f", "j", "c", "c", "n"]

    @staticmethod
    def solution(test_case):
        letters = test_case[0]
        target = test_case[1]

        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] == target:
                if mid == len(letters) - 1:
                    return letters[0]
                if letters[mid] != letters[mid + 1]:
                    return letters[mid + 1]
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left] if left != len(letters) else letters[0]


if __name__ == '__main__':
    p = Problem744()
    p.submit()
