from problem_abc import ProblemAbc


class Problem6(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/longest-palindromic-substring/"
        self.test_cases = [("PAYPALISHIRING", 3), ("PAYPALISHIRING", 4), ("A", 1)]
        self.y = ["PAHNAPLSIIGYIR", "PINALSIGYAHRPI", "A"]

    @staticmethod
    def solution(test_case):
        s = test_case[0]
        numRows = test_case[1]

        cat = [i for i in range(numRows)]
        cat = cat + cat[-2:0:-1]
        mod = len(cat)
        hashtable = {}
        for i, char in enumerate(s):
            if cat[i % mod] not in hashtable:
                hashtable[cat[i % mod]] = []
            hashtable[cat[i % mod]].append(char)
        ans_list = []
        for i in hashtable:
            ans_list += hashtable[i]
        return ''.join(ans_list)


if __name__ == '__main__':
    p = Problem6()
    p.submit()
