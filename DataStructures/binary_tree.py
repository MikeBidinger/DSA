class BinaryNode:
    def __init__(self, item, left=None, right=None):
        self.left = left
        self.right = right
        self.item = item


class BinaryTree:
    def __init__(self, root_item, left=None, right=None):
        self.root = BinaryNode(root_item, left, right)

    def add_RLnodes(self, node: BinaryNode):
        node.left = BinaryNode(node.item + "L")
        node.right = BinaryNode(node.item + "R")

    def remove_node(self):
        return None

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

    def printPreOrder(self, node: BinaryNode):
        if node is None:
            return
        else:
            print(node.item, end=" ")
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)

    def printInOrder(self, node: BinaryNode):
        if node is None:
            return
        else:
            self.printInOrder(node.left)
            print(node.item, end=" ")
            self.printInOrder(node.right)

    def printPostOrder(self, node: BinaryNode):
        if node is None:
            return
        else:
            self.printPostOrder(node.left)
            self.printPostOrder(node.right)
            print(node.item, end=" ")

    def printLevelOrder(self, node: BinaryNode):
        h = self.get_node_height(node)
        for i in range(1, h + 1):
            self._printCurrentLevel(node, i)

    def _printCurrentLevel(self, node: BinaryNode, level):
        if node is None:
            return
        if level == 1:
            print(node.item, end=" ")
        elif level > 1:
            self._printCurrentLevel(node.left, level - 1)
            self._printCurrentLevel(node.right, level - 1)

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

    def stackInOrder(self, node: BinaryNode):
        current = node
        stack = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.item, end=" ")
                current = current.right
            else:
                break

    def morrisTraversal(stack, node: BinaryNode):
        current = node
        while current is not None:
            if current.left is None:
                yield current.item
                current = current.right
            else:
                pre = current.left
                while pre.right is not None and pre.right is not current:
                    pre = pre.right
                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    yield current.item
                    current = current.right

    def printMorris(self, node: BinaryNode):
        for v in self.morrisTraversal(node):
            print(v, end=" ")


if __name__ == "__main__":

    # Create a binary tree (root = 1)
    tree = BinaryTree("1",
        left=BinaryNode("10",
            left=BinaryNode("100"), right=BinaryNode("101")),
        right=BinaryNode("11", 
            left=BinaryNode("110"), right=BinaryNode("111")))
    """    1
         /   \ 
       10     11
      / \     / \ 
    100 101 110 111 """

    # Remove node
    tree.root.left = tree.remove_node()

    # Get depth
    print(tree.get_node_height(tree.root))
    print(tree.get_node_height(tree.root.left))
    print(tree.get_node_height(tree.root.right))

    # Print tree using recursion
    print("Pre-Order Recursive Traversal:")
    tree.printPreOrder(tree.root)
    print()
    print("In-Order Recursive Traversal:")
    tree.printInOrder(tree.root)
    print()
    print("Post-Order Recursive Traversal:")
    tree.printPostOrder(tree.root)
    print()
    print("Level-Order Recursive Traversal:")
    tree.printLevelOrder(tree.root)
    print()

    # Print tree without recursion using queue
    print("Level-Order Queue Traversal:")
    tree.printLevelOrder_queue(tree.root)
    print()

    # -----------------------------------------------------

    # Create a binary tree (root = X)
    tree = BinaryTree("X")

    # Add (right and lift) nodes
    tree.add_RLnodes(tree.root)
    tree.add_RLnodes(tree.root.left)
    tree.add_RLnodes(tree.root.right)
    """    X
         /   \ 
       XL     XR
      / \     / \ 
    XLL XLR XRL XRR """

    # Print tree wihtout recursion using stack
    print("Stack Traversal:")
    tree.stackInOrder(tree.root)
    print()

    # Print tree wihtout recursion and without stack
    print("Morris Traversal:")
    tree.printMorris(tree.root)
    print()
