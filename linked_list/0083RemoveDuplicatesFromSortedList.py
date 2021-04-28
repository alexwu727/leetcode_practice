from problem_abc import ProblemAbc
from linked_list.nodes import list_to_nodes
from linked_list.nodes import nodes_to_list


class Problem83(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/remove-duplicates-from-sorted-list/"
        self.test_cases = [[1, 1, 2], [1, 1, 2, 3, 3], [], [1, 1], [1]]
        self.y = [[1, 2], [1, 2, 3], [], [1], [1]]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        head = list_to_nodes(test_case)

        if not head or not head.next:
            return head
        tmp = head
        cur = head
        while tmp:
            if not tmp.next or tmp.val != tmp.next.val:
                cur.next = tmp.next
                cur = cur.next
            tmp = tmp.next
        return head


if __name__ == '__main__':
    p = Problem83()
    p.submit()
