from problem_abc import ProblemAbc
from binary_tree.nodes import list_to_nodes


class Problem623(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/average-of-levels-in-binary-tree/"
        self.test_cases = [[3, 9, 20, "null", 15, 7], [3, 9, 20, 15, 7], [1]]
        self.y = [[3.00000, 14.50000, 11.00000], [3.00000, 14.50000, 11.00000], [1]]

    @staticmethod
    def solution(test_case):
        root = list_to_nodes(test_case)

        if not root:
            return [0]
        ans = []
        stack = [root]
        tmp_stack = []
        while stack:
            s = 0
            for node in stack:
                s += node.val
                if node.left:
                    tmp_stack.append(node.left)
                if node.right:
                    tmp_stack.append(node.right)
            ans.append(s / len(stack))
            stack = tmp_stack
            tmp_stack = []
        return ans


if __name__ == '__main__':
    p = Problem623()
    p.submit()
