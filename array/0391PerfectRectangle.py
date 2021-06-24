from problem_abc import ProblemAbc


class Problem391(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/elimination-game/"
        self.test_cases = [[[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]],
                           [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]],
                           [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [3, 2, 4, 4]]]
        self.y = [True, False, False]

    @staticmethod
    def solution(test_case):
        rectangles = test_case

        if not rectangles:
            return False

        def area(rectangle):
            return (rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1])

        corner = set()
        total_area = 0
        outer = rectangles[0]
        for x, y, a, b in rectangles:
            total_area += area([x, y, a, b])
            outer = [min(x, outer[0]), min(y, outer[1]),
                     max(a, outer[2]), max(b, outer[3])]
            corner ^= {(x, y), (a, b), (x, b), (a, y)}
        if corner != {(outer[0], outer[1]),
                      (outer[2], outer[3]),
                      (outer[0], outer[3]),
                      (outer[2], outer[1])}:
            return False
        return total_area == area(outer)


if __name__ == '__main__':
    p = Problem391()
    p.submit()
