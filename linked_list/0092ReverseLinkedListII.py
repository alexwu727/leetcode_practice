from problem_abc import ProblemAbc
from linked_list.nodes import list_to_nodes
from linked_list.nodes import nodes_to_list


class Problem92(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/reverse-linked-list-ii/"
        self.test_cases = [([1, 2, 3, 4, 5], 2, 4),
                           ([1, 2, 3, 4, 5], 1, 4),
                           ([1, 2, 3, 4, 5], 2, 5),
                           ([1, 2, 3, 4, 5], 1, 5)]
        self.y = [[1, 4, 3, 2, 5], [4, 3, 2, 1, 5], [1, 5, 4, 3, 2], [5, 4, 3, 2, 1]]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        head = list_to_nodes(test_case[0])
        left = test_case[1]
        right = test_case[2]

        if left == right:
            return head
        cur = head
        l = []
        while cur:
            l.append(cur)
            cur = cur.next
        for i in range(left, right):
            l[i].next = l[i - 1]
        if right == len(l):
            l[left - 1].next = None
        else:
            l[left - 1].next = l[right]
        if left != 1:
            l[left - 2].next = l[right - 1]
            return head
        return l[right - 1]


if __name__ == '__main__':
    p = Problem92()
    p.submit()
