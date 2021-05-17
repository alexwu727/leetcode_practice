from problem_abc import ProblemAbc
from binary_tree.nodes import list_to_nodes


class Problem606(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/flatten-binary-tree-to-linked-list/"
        self.test_cases = [[1, 2, 3, 4], [1, 2, 3, "null", 4]]
        self.y = ["1(2(4))(3)", "1(2()(4))(3)"]

    @staticmethod
    def solution(test_case):
        root = list_to_nodes(test_case)

        def recur(node):
            if node:
                if not node.left and node.right:
                    return "(%s()%s)" % (node.val, recur(node.right))
                else:
                    return "(%s%s%s)" % (node.val, recur(node.left), recur(node.right))
            else:
                return ""

        return recur(root)[1:-1]


if __name__ == '__main__':
    p = Problem606()
    p.submit()
