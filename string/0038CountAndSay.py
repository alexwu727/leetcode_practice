from problem_abc import ProblemAbc


class Problem38(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/count-and-say/"
        self.test_cases = [1, 4, 5, 7]
        self.y = ["1", "1211", "111221", "13112221"]

    @staticmethod
    def solution(test_case):
        n = test_case

        ans = "1"
        for _ in range(n - 1):
            new_ans = ""
            i = 0
            cur_count = 1
            while i < len(ans):
                if i + 1 != len(ans):
                    if ans[i + 1] != ans[i]:
                        new_ans += (str(cur_count) + ans[i])
                        cur_count = 1
                    else:
                        cur_count += 1
                else:
                    new_ans += (str(cur_count) + ans[i])
                i += 1
            ans = new_ans
        return ans


if __name__ == '__main__':
    p = Problem38()
    p.submit()
