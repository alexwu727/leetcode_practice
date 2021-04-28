from problem_abc import ProblemAbc
from linked_list.nodes import list_to_nodes
from linked_list.nodes import nodes_to_list


class Problem61(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/rotate-list/"
        self.test_cases = [([1, 2, 3, 4, 5], 2), ([1, 2, 3, 4, 5], 3), ([1, 2, 3, 4, 5], 7), ([1, 2, 3, 4, 5], 5),
                           ([1, 2, 3, 4, 5], 10), ([1], 1), ([], 4)]
        self.y = [[4, 5, 1, 2, 3], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1], []]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        head = list_to_nodes(test_case[0])
        k = test_case[1]
        if not head or k == 0:
            return head
        if k == 0:
            return head
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
        tail.next = head
        for _ in range(n - k % n):
            head = head.next
            tail = tail.next
        tail.next = None
        return head


if __name__ == '__main__':
    p = Problem61()
    p.submit()
