from problem_abc import ProblemAbc
from nodes import list_to_nodes
from nodes import nodes_to_list


class Problem19(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/remove-nth-node-from-end-of-list/"
        self.test_cases = [([1, 2, 3, 4, 5], 2), ([1, 2, 3, 4, 5], 1), ([1, 2, 3, 4, 5], 5), ([1], 1), ([1, 2], 1)]
        self.y = [[1, 2, 3, 5], [1, 2, 3, 4], [2, 3, 4, 5], [], [1]]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        head = list_to_nodes(test_case[0])
        n = test_case[1]

        slow = head
        fast = head
        for _ in range(n - 1):
            fast = fast.next
        if not fast.next:
            return head.next
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return head


if __name__ == '__main__':
    p = Problem19()
    p.submit()
