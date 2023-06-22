class BST():

    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None


tree = BST(10)

tree.left = BST(6)
tree.left.left = BST(2)
tree.left.right = BST(7)

tree.right = BST(15)
tree.right.left = BST(12)
tree.right.right = BST(20)


def in_order_traversal(tree, arr = None):
    if arr == None:
        arr = []

    if tree is not None:
        in_order_traversal(tree.left, arr)
        arr.append(tree.value)
        in_order_traversal(tree.right, arr)

    return arr

def post_order_traversal(tree, arr = None):
    if arr == None:
        arr = []

    if tree is not None:
        post_order_traversal(tree.left, arr)
        post_order_traversal(tree.right, arr)
        arr.append(tree.value)


    return arr

def pre_order_traversal(tree, arr = None):
    if arr == None:
        arr = []

    if tree is not None:
        arr.append(tree.value)
        pre_order_traversal(tree.left, arr)
        pre_order_traversal(tree.right, arr)


    return arr


print(in_order_traversal(tree))

print(post_order_traversal(tree))

print(pre_order_traversal(tree))
