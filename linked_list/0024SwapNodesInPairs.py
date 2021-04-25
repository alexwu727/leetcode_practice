from problem_abc import ProblemAbc
from nodes import list_to_nodes
from nodes import nodes_to_list


class Problem24(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/swap-nodes-in-pairs/"
        self.test_cases = [[1,2,3,4], [1,2,3,4,5], [], [1], [1,2]]
        self.y = [[2,1,4,3], [2,1,4,3,5], [], [1], [2,1]]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        head = list_to_nodes(test_case)

        if not head or not head.next:
            return head
        l1 = []
        l2 = []
        cur = head
        while cur and cur.next:
            l1.append(cur)
            l2.append(cur.next)
            cur = cur.next.next
        if cur:
            l1.append(cur)

        # 1,3,5
        # 2,4

        for i in range(len(l2)):
            l2[i].next = l1[i]
            if i != len(l2) - 1:
                l1[i].next = l2[i + 1]
            elif len(l1) > len(l2):
                l1[i].next = l1[i + 1]
            else:
                l1[i].next = None

        return l2[0]


if __name__ == '__main__':
    p = Problem24()
    p.submit()
