class BinaryNode:
    def __init__(self, item, left=None, right=None):
        self.left = left
        self.right = right
        self.item = item


class BinarySearchTree:
    def __init__(self, root_item, left=None, right=None):
        self.root = BinaryNode(root_item, left, right)

    def insert(self, node: BinaryNode, key):
        if node is None:
            return BinaryNode(key)
        else:
            if node.item == key:
                return node
            elif int(node.item) < int(key):
                node.right = self.insert(node.right, key)
            else:
                node.left = self.insert(node.left, key)
        return node

    def remove_node(self):
        return None
    
    def search(self, node: BinaryNode, key):
        if node is None or node.item == key:
            return node
        if int(node.item) < int(key):
            return self.search(node.right, key)
        return self.search(node.left, key)


if __name__ == "__main__":
    
    # Create a binary search tree
    tree = BinarySearchTree("8")
    tree.insert(tree.root, "3")
    tree.insert(tree.root, "10")
    tree.insert(tree.root, "1")
    tree.insert(tree.root, "6")
    tree.insert(tree.root, "14")
    tree.insert(tree.root, "4")
    tree.insert(tree.root, "7")
    tree.insert(tree.root, "13")
    """   8
        /   \ 
       3     10
      / \      \ 
     1   6      14
        / \     /
       4   7   13 """
    
    # Search a given key in BST
    key = "13"
    print("Search " + key + ":")
    result = tree.search(tree.root, key)
    if result is not None:
        print("Found!")
