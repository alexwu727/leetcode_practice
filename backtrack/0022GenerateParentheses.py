from problem_abc import ProblemAbc


class Problem22(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/generate-parentheses/"
        self.test_cases = [3, 1]
        self.y = [["((()))", "(()())", "(())()", "()(())", "()()()"], ["()"]]
        self.adjust_output = "any_order"

    @staticmethod
    def solution(test_case):
        n = test_case

        ans = []

        def backtrack(s="", left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

        backtrack()
        return ans


if __name__ == '__main__':
    p = Problem22()
    p.submit()
