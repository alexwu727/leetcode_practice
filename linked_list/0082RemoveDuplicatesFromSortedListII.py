from problem_abc import ProblemAbc
from nodes import list_to_nodes
from nodes import nodes_to_list
from nodes import SinglyListNode


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
        tmpVal = float("inf")
        ans = SinglyListNode()
        ansCur = ans
        while head and head.next:
            if head.val == tmpVal:
                pass
            elif head.val == head.next.val:
                tmpVal = head.val
            else:
                ansCur.next = head
                ansCur = ansCur.next
            head = head.next

        if head.val != tmpVal:
            ansCur.next = head
        else:
            ansCur.next = None
        return ans.next


if __name__ == '__main__':
    p = Problem82()
    p.submit()
