from problem_abc import ProblemAbc


class Problem56(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/merge-intervals/"
        self.test_cases = [[[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 4], [4, 5]], [[1, 2], [3, 10], [6, 8], [15, 19]]]
        self.y = [[[1, 6], [8, 10], [15, 18]], [[1, 5]], [[1, 2], [3, 10], [15, 19]]]

    @staticmethod
    def solution(test_case):
        intervals = test_case
        intervals = sorted(intervals)
        ans = [intervals.pop(0)]
        for interval in intervals:
            # interval vs ans[-1]
            if interval[1] <= ans[-1][1]:  # contain
                continue
            if interval[0] <= ans[-1][1]:  # overlap occur
                ans[-1][1] = interval[1]
            else:
                ans.append(interval)
        return ans


if __name__ == '__main__':
    p = Problem56()
    p.submit()
