from problem_abc import ProblemAbc
from binary_tree.nodes import list_to_nodes
from binary_tree.nodes import nodes_to_list


class Problem114(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/flatten-binary-tree-to-linked-list/"
        self.test_cases = [[1, 2, 5, 3, 4, "null", 6]]
        self.y = [[1, "null", 2, "null", 3, "null", 4, "null", 5, "null", 6]]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        root = list_to_nodes(test_case)

        l = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                l.append(node)
                stack.append(node.right)
                stack.append(node.left)
        for i in range(0, len(l) - 1):
            node = l[i]
            node.left = None
            node.right = l[i + 1]

        return root


if __name__ == '__main__':
    p = Problem114()
    p.submit()
