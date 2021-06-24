from problem_abc import ProblemAbc


class Problem390(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/elimination-game/"
        self.test_cases = [9, 1]
        self.y = [6, 1]

    @staticmethod
    def solution(test_case):
        n = test_case

        m = n
        k = 1
        start = 1
        while m > 1:
            if k % 2 == 1 or m % 2 == 1:
                start += (1 << (k - 1))
            m = m // 2
            k += 1
        return start


if __name__ == '__main__':
    p = Problem390()
    p.submit()
