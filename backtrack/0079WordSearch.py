from problem_abc import ProblemAbc


class Problem79(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/gray-code/"
        self.test_cases = [([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
                           ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
                           ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")]
        self.y = [True, True, False]

    @staticmethod
    def solution(test_case):
        board = test_case[0]
        word = test_case[1]

        m, n = len(board), len(board[0])

        def backtrack(i, j, word=word):
            if (i < 0) or (j < 0) or (i >= m) or (j >= n):
                return False
            if board[i][j] != word[0]:
                return False
            if len(word) == 1:
                return True
            tmp = board[i][j]
            board[i][j] = "#"
            ans = backtrack(i + 1, j, word[1:]) or \
                  backtrack(i - 1, j, word[1:]) or \
                  backtrack(i, j + 1, word[1:]) or \
                  backtrack(i, j - 1, word[1:])
            board[i][j] = tmp
            return ans

        for i in range(m):
            for j in range(n):
                if backtrack(i, j):
                    return True
        return False


if __name__ == '__main__':
    p = Problem79()
    p.submit()
