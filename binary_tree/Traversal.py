from binary_tree.nodes import list_to_nodes


def recursive_pre_traversal(node, f):
    if node:
        f(node)
        recursive_pre_traversal(node.left, f)
        recursive_pre_traversal(node.right, f)


def recursive_in_traversal(node, f):
    if node:
        recursive_in_traversal(node.left, f)
        f(node)
        recursive_in_traversal(node.right, f)


def recursive_post_traversal(node, f):
    if node:
        recursive_post_traversal(node.left, f)
        recursive_post_traversal(node.right, f)
        f(node)


def iterative_pre_traversal(root, f):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            f(node)
            stack.append(node.right)
            stack.append(node.left)


def iterative_in_traversal(root, f):
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            f(node)
            root = node.right


def iterative_post_traversal(root, f):
    nodes = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            nodes.append(node)
            stack.append(node.left)
            stack.append(node.right)
    for node in nodes[::-1]:
        f(node)


if __name__ == '__main__':
    print("test for traversal functions")
    print("nodes list: [1, 2, 3, 4, 5, null, 6, null, 7, null, null, 8, 9, 10, 11]")
    n1 = list_to_nodes([1, 2, 3, 4, 5, "null", 6, "null", 7, "null", "null", 8, 9, 10, 11])
    print("================== preorder =================")
    print("recursive:", end=" ")
    recursive_pre_traversal(n1, lambda x: print(x.val, end=", "))
    print()
    print("iterative:", end=" ")
    iterative_pre_traversal(n1, lambda x: print(x.val, end=", "))
    print()

    print("================== inorder ==================")
    print("recursive:", end=" ")
    recursive_in_traversal(n1, lambda x: print(x.val, end=", "))
    print()
    print("iterative:", end=" ")
    iterative_in_traversal(n1, lambda x: print(x.val, end=", "))
    print()

    print("================= postorder =================")
    print("recursive:", end=" ")
    recursive_post_traversal(n1, lambda x: print(x.val, end=", "))
    print()
    print("iterative:", end=" ")
    iterative_post_traversal(n1, lambda x: print(x.val, end=", "))
    print()
