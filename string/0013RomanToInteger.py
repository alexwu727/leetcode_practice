from problem_abc import ProblemAbc


class Problem13(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/roman-to-integer/"
        self.test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
        self.y = [3, 4, 9, 58, 1994]

    @staticmethod
    def solution(test_case):
        s = test_case

        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        for i, char in enumerate(s):
            if i != len(s) - 1 and table[char] < table[s[i + 1]]:
                ans -= table[char]
            else:
                ans += table[char]
        return ans


if __name__ == '__main__':
    p = Problem13()
    p.submit()
