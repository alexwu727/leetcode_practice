from problem_abc import ProblemAbc


class Problem17(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/letter-combinations-of-a-phone-number/"
        self.test_cases = ["23", "2", ""]
        self.y = [["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], ["a", "b", "c"], []]

    @staticmethod
    def solution(test_case):
        digits = test_case

        if not digits:
            return []
        table = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [""]
        for digit in digits:
            tmp = []
            for j in ans:
                for k in table[int(digit)]:
                    tmp.append(j + k)
            ans = tmp
        return ans


if __name__ == '__main__':
    p = Problem17()
    p.submit()
