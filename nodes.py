class SinglyListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nodes_to_list(node: SinglyListNode):
    if not node:
        return []
    l = []
    while node:
        l.append(node.val)
        node = node.next
    return l


def list_to_nodes(arr):
    if not arr:
        return None
    head = SinglyListNode(val=arr[0], next=None)
    cur = head
    for i in arr[1:]:
        cur.next = SinglyListNode(val=i, next=None)
        cur = cur.next
    return head
