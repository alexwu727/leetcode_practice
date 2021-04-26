from problem_abc import ProblemAbc
from nodes import list_to_nodes
from nodes import nodes_to_list


class Problem25(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/reverse-nodes-in-k-group/"
        self.test_cases = [([1, 2, 3, 4, 5], 2), ([1, 2, 3, 4, 5], 3), ([1, 2, 3, 4, 5], 1), ([1], 1)]
        self.y = [[2, 1, 4, 3, 5], [3, 2, 1, 4, 5], [1, 2, 3, 4, 5], [1]]
        self.adjust_output = nodes_to_list

    @staticmethod
    def solution(test_case):
        head = list_to_nodes(test_case[0])
        k = test_case[1]
        l = []
        cur = head
        while cur:
            l.append(cur)
            cur = cur.next

        for i in range(k - 1, len(l), k):
            cur_i = i
            for _ in range(k - 1):
                l[cur_i].next = l[cur_i - 1]
                cur_i -= 1
            if i + k >= len(l):
                if i == len(l) - 1:
                    l[cur_i].next = None
                else:
                    l[cur_i].next = l[i + 1]
            else:
                l[cur_i].next = l[i + k]
        return l[k - 1]


if __name__ == '__main__':
    p = Problem25()
    p.submit()
