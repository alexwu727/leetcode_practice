from problem_abc import ProblemAbc
from binary_tree.nodes import list_to_nodes
from binary_tree.nodes import nodes_to_list


class Problem617(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/merge-two-binary-trees/"
        self.test_cases = [([1,3,2,5], [2,1,3,"null",4,"null",7]), ([1], [1,2])]
        self.y = [[3,4,5,5,4,"null",7], [2,2]]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        root1 = list_to_nodes(test_case[0])
        root2 = list_to_nodes(test_case[1])

        if not root1:
            return root2
        if not root2:
            return root1

        def recur(node1, node2):
            if node1:
                node2.val += node1.val
                if not node2.left:
                    node2.left = node1.left
                else:
                    recur(node1.left, node2.left)
                if not node2.right:
                    node2.right = node1.right
                else:
                    recur(node1.right, node2.right)

        recur(root1, root2)
        return root2


if __name__ == '__main__':
    p = Problem617()
    p.submit()
