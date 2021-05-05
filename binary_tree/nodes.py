class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def nodes_to_list(root: BinaryTreeNode):
    if not root:
        return []
    arr = [root.val]
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            arr.append(node.left.val if node.left else "null")
            arr.append(node.right.val if node.right else "null")
            queue += [node.left, node.right]
    while arr[-2:] == ["null", "null"]:
        arr = arr[:-2]
    while arr[-1] == "null":
        arr.pop()
    return arr


def list_to_nodes(arr):
    if not arr:
        return None
    nodes = list(map(lambda x: BinaryTreeNode(x) if x != "null" else None, arr))
    if len(nodes) % 2 == 0:
        nodes.append(None)
    cur = 0
    for node in nodes:
        if cur >= len(nodes) - 1:
            return nodes[0]
        if node:
            node.left = nodes[cur + 1]
            node.right = nodes[cur + 2]
            cur += 2
    return nodes[0]


if __name__ == '__main__':
    print("test for converting function")
    print("nodes to list:")
    n1 = BinaryTreeNode(1)
    n2 = BinaryTreeNode(2)
    n3 = BinaryTreeNode(3)
    n4 = BinaryTreeNode(4)
    n5 = BinaryTreeNode(5)
    n1.left, n1.right = n2, n3
    n2.left = n4
    n3.right = n5
    print(nodes_to_list(n1))

    print("list to nodes:")
    a = list_to_nodes([1, 2, "null", 3, 4])
    print(a.val, end=", ")
    print(a.left.val, end=", ")
    print(a.right, end=", ")
    print(a.left.left.val, end=", ")
    print(a.left.right.val)
