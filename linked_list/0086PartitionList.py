from problem_abc import ProblemAbc
from linked_list.nodes import list_to_nodes
from linked_list.nodes import nodes_to_list
from linked_list.nodes import SinglyListNode


class Problem86(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/partition-list/"
        self.test_cases = [([1, 4, 3, 2, 5, 2], 3), ([7, 1, 4], 7)]
        self.y = [[1, 2, 2, 4, 3, 5], [1, 4, 7]]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        head = list_to_nodes(test_case[0])
        x = test_case[1]

        cur = head
        left = SinglyListNode()
        right = SinglyListNode()
        left_cur = left
        right_cur = right
        while cur:
            if cur.val < x:
                left_cur.next = cur
                left_cur = left_cur.next
            else:
                right_cur.next = cur
                right_cur = right_cur.next
            cur = cur.next
        left_cur.next = right.next
        right_cur.next = None
        return left.next


if __name__ == '__main__':
    p = Problem86()
    p.submit()
