class Node:
    def __init__(self, item):
        self.item = item  # Item
        self.next = None  # Pointer


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def printLList(self):
        if self.isEmpty():
            print("Linked List is empty!")
            return
        print("Linked List:")
        temp = self.head
        while temp:
            print("", temp.item)
            temp = temp.next


if __name__ == "__main__":

    # Create a linked list
    llist = LinkedList()

    # Create nodes (items)
    llist.head = Node(10)
    second = Node(20)
    third = Node(30)

    # Link nodes (pointers)
    llist.head.next = second
    second.next = third

    # Print linked list
    llist.printLList()
