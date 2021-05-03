from problem_abc import ProblemAbc
from binary_tree.nodes import list_to_nodes
from binary_tree.nodes import nodes_to_list


class Problem700(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/search-in-a-binary-search-tree/"
        self.test_cases = [([4, 2, 7, 1, 3], 2), ([4, 2, 7, 1, 3], 5)]
        self.y = [[2, 1, 3], []]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        root = list_to_nodes(test_case[0])
        val = test_case[1]

        def recur(root, val):
            if not root:
                return
            if root.val == val:
                return root
            elif root.val > val:
                return recur(root.left, val)
            else:
                return recur(root.right, val)

        return recur(root, val)


if __name__ == '__main__':
    p = Problem700()
    p.submit()
