class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def bst_max(top):
    if top is None:
        raise ValueError("Puste drzewo")
    while top.right is not None:
        top = top.right
    return top

def bst_min(top):
    if top is None:
        raise ValueError("Puste drzewo")
    while top.left is not None:
        top = top.left
    return top


node = Node(10)
left = Node(8)
leftleft = Node(4)
leftright = Node(9)
right = Node(15)
rightleft = Node(11)
rightright = Node(69)

node.left = left
node.right = right
left.left = leftleft
left.right = leftright
right.left = rightleft
right.right = rightright

print("bst_min = " + str(bst_min(node).data))
print("bst_max = " + str(bst_max(node).data))