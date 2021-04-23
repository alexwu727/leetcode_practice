from problem_abc import ProblemAbc
from nodes import list_to_nodes
from nodes import nodes_to_list
from nodes import SinglyListNode


class Problem21(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/merge-two-sorted-lists/"
        self.test_cases = [([1, 2, 4], [1, 3, 4]), ([], []), ([], [0])]
        self.y = [[1, 1, 2, 3, 4, 4], [], [0]]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        l1 = list_to_nodes(test_case[0])
        l2 = list_to_nodes(test_case[1])

        if not l1:
            return l2
        if not l2:
            return l1
        tmp = SinglyListNode()
        tmp_cur = tmp
        l1_cur = l1
        l2_cur = l2
        while l1_cur and l2_cur:
            if l1_cur.val <= l2_cur.val:
                tmp_cur.next = l1_cur
                l1_cur = l1_cur.next
            else:
                tmp_cur.next = l2_cur
                l2_cur = l2_cur.next
            tmp_cur = tmp_cur.next

        if not l1_cur:
            tmp_cur.next = l2_cur
        if not l2_cur:
            tmp_cur.next = l1_cur
        return tmp.next


if __name__ == '__main__':
    p = Problem21()
    p.submit()
