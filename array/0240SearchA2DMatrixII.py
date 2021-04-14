from problem_abc import ProblemAbc


class Problem240(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/search-a-2d-matrix-ii/"
        self.test_cases = [
            ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5),
            ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)]
        self.y = [True, False]

    @staticmethod
    def solution(test_case):
        matrix = test_case[0]
        target = test_case[1]
        # for loop
        for row in matrix:
            if target in row:
                return True
        return False
        # recursive
        # def recur(matrix):
        #     if len(matrix) == 1 and len(matrix[0]) == 1:
        #         return True if matrix[0][0] == target else False
        #     elif not matrix or not matrix[0]:
        #         return False
        #     else:
        #         n_mid = len(matrix) // 2
        #         m_mid = len(matrix[0]) // 2
        #         sub_a = [matrix[i][:m_mid] for i in range(n_mid)]
        #         sub_b = [matrix[i][m_mid:] for i in range(n_mid)]
        #         sub_c = [matrix[i][:m_mid] for i in range(n_mid, len(matrix))]
        #         sub_d = [matrix[i][m_mid:] for i in range(n_mid, len(matrix))]
        #         a = recur(sub_a)
        #         b = recur(sub_b)
        #         c = recur(sub_c)
        #         d = recur(sub_d)
        #         return a or b or c or d
        #
        # return recur(matrix)


if __name__ == '__main__':
    p = Problem240()
    p.submit()
