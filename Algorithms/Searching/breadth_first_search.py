class BinaryNode:
    def __init__(self, item, left=None, right=None):
        self.left = left
        self.right = right
        self.item = item


class BinaryTree:
    def __init__(self, root_item, left=None, right=None):
        self.root = BinaryNode(root_item, left, right)

    def get_node_height(self, node: BinaryNode):
        if node is None:
            return 0
        else:
            lHeight = self.get_node_height(node.left)
            rHeight = self.get_node_height(node.right)
            if lHeight > rHeight:
                return lHeight + 1
            else:
                return rHeight + 1

    def printLevelOrder_queue(self, node: BinaryNode):
        if node is None:
            return
        q = []
        q.append(node)
        while len(q) > 0:
            print(q[0].item, end=" ")
            popped = q.pop(0)
            if popped.left is not None:
                q.append(popped.left)
            if popped.right is not None:
                q.append(popped.right)

    def bfs(self, item):
        if self.root is None:
            return
        q = []
        q.append(self.root)
        while len(q) > 0:
            print(q[0].item, end=" ")
            popped = q.pop(0)
            if popped.item == item:
                return popped
            if popped.left is not None:
                q.append(popped.left)
            if popped.right is not None:
                q.append(popped.right)


if __name__ == "__main__":

    # Create a binary tree (root = 1)
    tree = BinaryTree(
        "1",
        left=BinaryNode("10", left=BinaryNode("100"), right=BinaryNode("101")),
        right=BinaryNode("11", left=BinaryNode("110"), right=BinaryNode("111")),
    )
    """    1
         /   \ 
       10     11
      / \     / \ 
    100 101 110 111 """

    # Print tree without recursion using queue
    print("Level-Order Queue Traversal:\n", end=" ")
    tree.printLevelOrder_queue(tree.root)
    print()

    # Search node
    print("BFS:\n", end=" ")
    node_items = ["10"]
    for node_item in node_items:
        node = tree.bfs(node_item)
        if node is None:
            print()
            print(" Node item", node_item, "is not present in tree")
        else:
            print()
            print(
                " Node item",
                node.item,
                "is present in tree at level",
                tree.get_node_height(node),
            )
