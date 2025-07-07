# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: "Node"):
    # Base case if the current not is None, we return a negative infinity, which means it is always less
    if root is None:
        return float('-inf')

    # Here, we have the recursive step.
    # We look at the greatest node value in each subtree
    left_max = greatest_node(root.left_child)
    right_max = greatest_node(root.right_child)

    # print(f"root: {root.value}")
    # print(f"left_max: {left_max}")
    # print(f"right_max: {right_max}")

    # With the max, we define which one is the biggest
    return max(root.value, left_max, right_max)

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))