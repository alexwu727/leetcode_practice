from problem_abc import ProblemAbc
from linked_list.nodes import list_to_nodes
from linked_list.nodes import nodes_to_list
from linked_list.nodes import SinglyListNode


class Problem82(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/"
        self.test_cases = [[1, 2, 3, 3, 4, 4, 5], [1, 1, 1, 2, 3], [1, 2, 3, 3, 4, 4, 5, 6, 6],
                           [1, 1, 2, 3, 4, 4, 5, 6, 6, 6], [], [1, 1], [1]]
        self.y = [[1, 2, 5], [2, 3], [1, 2, 5], [2, 3, 5], [], [], [1]]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        head = list_to_nodes(test_case)

        if not head or not head.next:
            return head
        tmp_val = float("inf")
        ans = SinglyListNode()
        ans_cur = ans
        while head and head.next:
            if head.val == tmp_val:
                pass
            elif head.val == head.next.val:
                tmp_val = head.val
            else:
                ans_cur.next = head
                ans_cur = ans_cur.next
            head = head.next

        if head.val != tmp_val:
            ans_cur.next = head
        else:
            ans_cur.next = None
        return ans.next


if __name__ == '__main__':
    p = Problem82()
    p.submit()
