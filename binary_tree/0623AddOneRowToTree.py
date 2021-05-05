from problem_abc import ProblemAbc
from binary_tree.nodes import list_to_nodes
from binary_tree.nodes import nodes_to_list
from binary_tree.nodes import BinaryTreeNode


class Problem623(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/add-one-row-to-tree/"
        self.test_cases = [([4, 2, 6, 3, 1, 5], 1, 2), ([4, 2, "null", 3, 1], 1, 3)]
        self.y = [[4, 1, 1, 2, "null", "null", 6, 3, 1, 5], [4, 2, "null", 1, 1, 3, "null", "null", 1]]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        root = list_to_nodes(test_case[0])
        val = test_case[1]
        depth = test_case[2]

        if depth == 1:
            return BinaryTreeNode(val, root)
        l = []

        def recur(node, n):
            if node:
                if n == depth - 1:
                    l.append(node)
                    return
                else:
                    recur(node.left, n + 1)
                    recur(node.right, n + 1)

        recur(root, 1)
        for prev in l:
            tmp = BinaryTreeNode(val, prev.left)
            prev.left = tmp
            tmp = BinaryTreeNode(val, None, prev.right)
            prev.right = tmp
        return root


if __name__ == '__main__':
    p = Problem623()
    p.submit()
